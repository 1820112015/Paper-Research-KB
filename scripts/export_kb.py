#!/usr/bin/env python3
"""Export the canonical Feishu research document to a Markdown repository.

The Feishu document provides the hierarchy and Chinese descriptions. Public paper
URLs are restored from the locally collected source notes; Feishu attachment URLs
are deliberately never exported.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote


SOURCE_URL = "https://zhipu-ai.feishu.cn/wiki/UgnNwpUOniODVBkwdpIcev7EnDc"
INTERNAL_FEISHU_URL = "internal-api-drive-stream.feishu.cn"
MANIFEST_NAME = ".paper-research-manifest.json"


@dataclass
class Research:
    month: str
    category: str
    title: str
    date: str = ""
    abstract: str = ""
    keywords: str = ""
    project: str = ""
    code: str = ""
    demo: str = ""
    has_attachment: bool = False
    pdf: str = ""
    local_fallbacks: dict[str, str] = field(default_factory=dict)


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    return re.sub(r"\s+", " ", value).strip().casefold()


def element_text(element: ET.Element) -> str:
    return "".join(element.itertext()).strip()


def first_http_link(element: ET.Element) -> str:
    for link in element.iter("a"):
        href = (link.attrib.get("href") or "").strip()
        if href.startswith(("https://", "http://")):
            return href
    return ""


def parse_document(payload: dict) -> tuple[list[Research], str]:
    document = payload["data"]["document"]
    content = document["content"]
    revision = str(document.get("revision_id") or payload["data"].get("revision_id") or "未知")
    root = ET.fromstring(f"<root>{content}</root>")

    month = ""
    category = ""
    current: Research | None = None
    entries: list[Research] = []

    for element in root:
        tag = element.tag
        text = element_text(element)
        if tag == "h1":
            month = text
            category = ""
            current = None
        elif tag == "h2":
            category = text
            current = None
        elif tag == "h3":
            if not month or not category:
                raise ValueError(f"条目缺少月份或分类上下文：{text}")
            current = Research(month=month, category=category, title=text)
            entries.append(current)
        elif current is not None and tag == "p":
            for label, attribute in (
                ("收录日期：", "date"),
                ("摘要：", "abstract"),
                ("关键词：", "keywords"),
                ("Project：", "project"),
                ("Code：", "code"),
                ("Demo：", "demo"),
            ):
                if text.startswith(label):
                    value = text[len(label) :].strip()
                    if attribute in {"project", "code", "demo"}:
                        value = first_http_link(element) or value
                    setattr(current, attribute, value)
                    break
        elif current is not None and tag == "figure":
            source = element.find("source")
            if source is not None and source.attrib.get("mime") == "application/pdf":
                current.has_attachment = True

    if not entries:
        raise ValueError("在线文档中没有解析到研究条目")
    return entries, revision


def parse_local_sources(metadata_root: Path) -> dict[str, list[dict[str, str]]]:
    records: dict[str, list[dict[str, str]]] = defaultdict(list)
    patterns = {
        "title": re.compile(r"^- 研究名称：\s*(.+?)\s*$", re.MULTILINE),
        "pdf": re.compile(r"^- 论文 PDF：\s*(https?://\S+)\s*$", re.MULTILINE),
        "project": re.compile(r"^- 项目 project 主页链接：\s*(https?://\S+)\s*$", re.MULTILINE),
        "code": re.compile(r"^- 项目 code 链接：\s*(https?://\S+)\s*$", re.MULTILINE),
        "demo": re.compile(r"^- (?:项目 )?demo 链接：\s*(https?://\S+)\s*$", re.MULTILINE | re.IGNORECASE),
    }

    for note in sorted(metadata_root.rglob("*.md")):
        if note.name == "标准格式.md":
            continue
        text = note.read_text(encoding="utf-8", errors="replace")
        sections = re.split(r"(?=^### 研究 \d+\s*$)", text, flags=re.MULTILINE)
        for section in sections:
            title_match = patterns["title"].search(section)
            if not title_match:
                continue
            record = {"title": title_match.group(1).strip(), "source": str(note)}
            for key in ("pdf", "project", "code", "demo"):
                match = patterns[key].search(section)
                record[key] = match.group(1).strip() if match else ""
            records[normalize(record["title"])].append(record)
    return records


def enrich_from_local(entries: list[Research], local: dict[str, list[dict[str, str]]]) -> list[str]:
    missing_attached: list[str] = []
    for entry in entries:
        candidates = local.get(normalize(entry.title), [])
        candidates.sort(key=lambda row: (bool(row.get("pdf")), row.get("source", "")), reverse=True)
        if candidates:
            best = candidates[0]
            entry.pdf = best.get("pdf", "")
            entry.local_fallbacks = best
            entry.project = entry.project or best.get("project", "")
            entry.code = entry.code or best.get("code", "")
            entry.demo = entry.demo or best.get("demo", "")
        if entry.has_attachment and not entry.pdf:
            missing_attached.append(entry.title)
        if INTERNAL_FEISHU_URL in entry.pdf:
            raise ValueError(f"拒绝导出飞书临时附件地址：{entry.title}")
    return missing_attached


def safe_component(value: str, *, is_file: bool = False) -> str:
    value = unicodedata.normalize("NFKC", value).strip()
    replacements = {
        "/": "／",
        "\\": "-",
        ":": "：",
        "*": "＊",
        "?": "？",
        '"': "＂",
        "<": "＜",
        ">": "＞",
        "|": "｜",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    value = re.sub(r"\s+", " ", value).strip(" .")
    limit = 170 if is_file else 100
    return value[:limit].rstrip(" .") or "未命名"


def month_folder(month: str) -> str:
    match = re.fullmatch(r"(\d{4})年(\d{1,2})月", month.strip())
    if not match:
        return safe_component(month)
    return f"{match.group(1)}年{int(match.group(2)):02d}月"


def markdown_link(label: str, url: str) -> str:
    return f"[{label}]({url})" if url else "暂无"


def entry_markdown(entry: Research) -> str:
    return "\n".join(
        [
            f"# {entry.title}",
            "",
            f"**收录日期：** {entry.date or '暂无'}",
            "",
            f"**分类：** {entry.category}",
            "",
            "## 摘要",
            "",
            entry.abstract or "暂无",
            "",
            f"**关键词：** {entry.keywords or '暂无'}",
            "",
            "## 相关链接",
            "",
            f"- **PDF：** {markdown_link('论文链接', entry.pdf)}",
            f"- **Project：** {markdown_link('项目主页', entry.project)}",
            f"- **Code：** {markdown_link('代码仓库', entry.code)}",
            f"- **Demo：** {markdown_link('在线演示', entry.demo)}",
            "",
        ]
    )


def relative_link(path: Path) -> str:
    return quote(path.as_posix(), safe="/-_.~()")


def build_readme(entries: list[Research], revision: str, paths: dict[int, Path]) -> str:
    by_month: dict[str, list[Research]] = defaultdict(list)
    for entry in entries:
        by_month[entry.month].append(entry)

    lines = [
        "# Paper Research KB",
        "",
        "按收录月份与研究分类整理的论文及项目知识库。每项研究对应一个独立 Markdown 文档；PDF 仅保留公开链接，本仓库不存放 PDF 文件。",
        "",
        f"- 在线文档：[飞书知识库原文]({SOURCE_URL})",
        f"- 最近同步：2026-07-17（飞书修订版 {revision}）",
        f"- 条目总数：{len(entries)}",
        "- 目录结构：`月份倒序编号 - 月份 / 分类 / 倒序编号 - 收录日期 - 研究名称.md`",
        "- 排序规则：月份及分类内条目均以 `001` 表示最新内容，确保 GitHub 文件列表中最新内容显示在最上方",
        "",
        "## 内容统计",
        "",
        "| 月份 | 分类 | 条目数 |",
        "| --- | --- | ---: |",
    ]
    for month, month_entries in by_month.items():
        counts = Counter(entry.category for entry in month_entries)
        for category, count in counts.items():
            lines.append(f"| {month} | {category.replace('|', '\\|')} | {count} |")

    lines.extend(["", "## 目录", ""])
    for month, month_entries in by_month.items():
        lines.extend([f"### {month}", ""])
        by_category: dict[str, list[Research]] = defaultdict(list)
        for entry in month_entries:
            by_category[entry.category].append(entry)
        for category, category_entries in by_category.items():
            lines.extend([f"#### {category}", ""])
            for entry in category_entries:
                path = paths[id(entry)]
                lines.append(f"- {entry.date} · [{entry.title}]({relative_link(path)})")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def clean_previous_export(repo_root: Path) -> None:
    manifest_path = repo_root / MANIFEST_NAME
    if not manifest_path.is_file():
        return
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for relative_name in manifest.get("files", []):
        relative = Path(relative_name)
        if relative.is_absolute() or ".." in relative.parts or relative.suffix.lower() != ".md":
            raise ValueError(f"同步清单中存在不安全路径：{relative_name}")
        target = repo_root / relative
        if target.is_file():
            target.unlink()
        parent = target.parent
        while parent != repo_root:
            try:
                parent.rmdir()
            except OSError:
                break
            parent = parent.parent


def export(entries: list[Research], repo_root: Path, revision: str) -> dict[str, int]:
    clean_previous_export(repo_root)
    paths: dict[int, Path] = {}
    seen_paths: set[str] = set()
    category_ranks: Counter[tuple[str, str]] = Counter()
    month_ranks: dict[str, int] = {}
    for entry in entries:
        month_ranks.setdefault(entry.month, len(month_ranks) + 1)
    for entry in entries:
        folder = Path(f"{month_ranks[entry.month]:03d} - {month_folder(entry.month)}") / safe_component(entry.category)
        category_ranks[(entry.month, entry.category)] += 1
        rank = category_ranks[(entry.month, entry.category)]
        filename = safe_component(
            f"{rank:03d} - {entry.date or '日期未知'} - {entry.title}", is_file=True
        ) + ".md"
        relative = folder / filename
        collision_key = normalize(relative.as_posix())
        if collision_key in seen_paths:
            raise ValueError(f"生成路径冲突：{relative}")
        seen_paths.add(collision_key)
        target = repo_root / relative
        legacy_name = safe_component(f"{entry.date or '日期未知'} - {entry.title}", is_file=True) + ".md"
        legacy_target = repo_root / month_folder(entry.month) / safe_component(entry.category) / legacy_name
        if legacy_target.is_file() and not target.exists():
            legacy_target.rename(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(entry_markdown(entry), encoding="utf-8")
        paths[id(entry)] = relative

    (repo_root / "README.md").write_text(build_readme(entries, revision, paths), encoding="utf-8")
    (repo_root / MANIFEST_NAME).write_text(
        json.dumps(
            {
                "source": SOURCE_URL,
                "revision": revision,
                "files": [paths[id(entry)].as_posix() for entry in entries],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return {
        "entries": len(entries),
        "pdf_links": sum(bool(entry.pdf) for entry in entries),
        "project_links": sum(bool(entry.project) for entry in entries),
        "code_links": sum(bool(entry.code) for entry in entries),
        "demo_links": sum(bool(entry.demo) for entry in entries),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, help="lark-cli docs +fetch JSON; defaults to stdin")
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--metadata-root", type=Path, required=True)
    args = parser.parse_args()

    raw = args.input.read_text(encoding="utf-8") if args.input else sys.stdin.read()
    payload = json.loads(raw)
    entries, revision = parse_document(payload)
    local = parse_local_sources(args.metadata_root.resolve())
    missing_attached = enrich_from_local(entries, local)
    if missing_attached:
        print("以下在线附件没有匹配到公开 PDF 链接：", file=sys.stderr)
        for title in missing_attached:
            print(f"- {title}", file=sys.stderr)
        return 2

    duplicate_titles = [title for title, count in Counter(normalize(e.title) for e in entries).items() if count > 1]
    if duplicate_titles:
        raise ValueError(f"在线文档仍有重复标题：{duplicate_titles}")
    invalid_dates = [entry.title for entry in entries if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", entry.date)]
    if invalid_dates:
        raise ValueError(f"收录日期格式异常：{invalid_dates}")

    stats = export(entries, args.repo_root.resolve(), revision)
    print(json.dumps({"revision": revision, **stats}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
