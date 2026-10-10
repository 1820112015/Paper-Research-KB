# CachedSearch: Training-Free Cached Exploration for Test-Time Search in Video Diffusion

**收录日期：** 2026-08-04

**分类：** 世界模型 / 内容生成模型

## 摘要

CachedSearch 针对视频扩散模型的测试时搜索成本过高问题，提出先用缓存策略低成本生成多个候选并排序，再只对胜出候选执行全算力重生成。它研究缓存是否会破坏候选排序，实验显示可在保留 best-of-8 大部分收益的同时显著降低计算成本，是一种免训练、可作为插件接入的推理期加速方案。

**关键词：** 视频扩散模型、测试时搜索、缓存加速、候选排序、免训练推理、视频生成效率

## 相关链接

- **PDF：** [论文链接](https://arxiv.org/pdf/2607.23159v2)
- **Project：** 暂无
- **Code：** [代码仓库](https://github.com/shreshthsaini/CachedSearch)
- **Demo：** 暂无
