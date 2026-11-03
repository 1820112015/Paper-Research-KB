# LongLive-Plug: Once-for-All Distillation for Video Generation

**收录日期：** 2026-10-10

**分类：** 世界模型 / 内容生成模型

## 摘要

NVIDIA 提出的 once-for-all 蒸馏框架：把视频生成能力做成可复用的“插件”。在基础视频模型上把少步采样、CFG、长上下文等能力一次性蒸馏成 LoRA 插件，之后无需再训练、即插即用地迁移到众多下游视频生成模型（覆盖 54 个下游模型），让同一个能力在多个基座间复用，而不必在每个模型上分别重新蒸馏。

**关键词：** 视频生成、知识蒸馏、LoRA插件、免训练复用、少步采样、能力迁移

## 相关链接

- **PDF：** [论文链接](https://arxiv.org/pdf/2609.38154)
- **Project：** 暂无
- **Code：** [代码仓库](https://github.com/NVlabs/LongLive)
- **Demo：** 暂无
