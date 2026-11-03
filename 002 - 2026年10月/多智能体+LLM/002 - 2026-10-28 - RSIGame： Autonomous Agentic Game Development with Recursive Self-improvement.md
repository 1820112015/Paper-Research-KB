# RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement

**收录日期：** 2026-10-28

**分类：** 多智能体+LLM

## 摘要

RSIGame 把自动游戏生成的关键难题定位为“能否可靠改进”而非“能否生成”：框架含两个互补循环——局部 explore-diagnose-improve 在可执行游戏本体上广泛探索、诊断并排序问题，做基于证据的修改，并用不断演进的 checklist 累积测试要点；全局循环跟踪质量趋势、保存最优 checkpoint、检测饱和与回退，避免越改越差。它还把成功经验内化进生成器模型，而非只依赖外挂 agent。在 140 个 GameCraft-Bench 任务、两个引擎（Godot/Phaser）与五个生成器上，同等预算下持续提升质量；Qwen3.8-27B 训练后在 Godot 达 61.38、Phaser 达 58.53，超过 GPT-5.5 一次性生成，同时生成 token 消耗降低 11 倍。

**关键词：** 游戏生成、递归自我改进、GameCraft-Bench、经验内化、长周期迭代

## 相关链接

- **PDF：** [论文链接](https://arxiv.org/pdf/2609.39045)
- **Project：** 暂无
- **Code：** 暂无
- **Demo：** 暂无
