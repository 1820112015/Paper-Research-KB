# Reward-Decomposed Reinforcement Learning for Immersive Video Role-Playing（EBM-RL）

**收录日期：** 2026-09-25

**分类：** 多智能体+LLM

## 摘要

EMNLP 2026 Oral。让 AI 先看懂眼前发生了什么、再以角色身份说话：提出 EBM-RL（Eye–Brain–Mouth），把视频角色扮演的生成过程拆成“看—想—说”——观察视频人物环境与事件、结合视觉对话历史与人设判断如何回应、生成符合角色贴合情境的台词；用 GRPO 分阶段奖励，让模型看得有依据、想得有帮助、说得符合角色。训练后的 7B 模型对 InternVL3-14B 净胜率 +12.6/+8.6/+16.4 个百分点，对 Qwen2.5-VL-32B 视觉依据净胜率 +9.0 显著；零样本迁移外部 VideoQA（NExT-QA +1.93、PororoQA +2.60、ActivityNet-QA +2.50）。同时发布首个面向电影叙事情境的开源视频角色扮演对话数据集（约 3.4 万条），面向 VR 游戏 NPC、互动叙事与沉浸式角色扮演。

**关键词：** 视频角色扮演、EMNLP、看想说分解、GRPO、强化学习、VR游戏NPC、沉浸式互动

## 相关链接

- **PDF：** [论文链接](https://arxiv.org/pdf/2605.04733)
- **Project：** 暂无
- **Code：** [代码仓库](https://github.com/ebm-rl/RP-See-Think-Speak-RL)
- **Demo：** 暂无
