# Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training

**收录日期：** 2026-08-29

**分类：** 世界模型 / 内容生成模型

## 摘要

针对游戏视频中的血条、地图、技能栏等 UI 元素污染世界模型训练数据的问题，提出 GameUI-Taxonomy 把游戏 UI 分为 21 个大类；G2WEngine 自动从游戏视频提取 UI 素材并合成带 UI 与不带 UI 的成对视频；GameCleaner 无需掩码即可识别并删除各类 HUD 元素，同时保持背景与动态连续。构建了含 9.6 万对合成视频与 1079 个真实游戏片段的 Game2World 数据集。GameCleaner 在合成视频上 AAR 达 95.36（高出最强时序掩码基线 57.3%）、真实视频 80.05、背景保留率 99.8%；去掉 UI 后世界模型 VideoReward 提升 6.83%、运动质量提升 18.8%。

**关键词：** 世界模型、游戏UI去除、数据引擎、视频生成、GameCleaner、训练数据清洗

## 相关链接

- **PDF：** [论文链接](https://arxiv.org/pdf/2608.24680)
- **Project：** 暂无
- **Code：** 暂无
- **Demo：** 暂无
