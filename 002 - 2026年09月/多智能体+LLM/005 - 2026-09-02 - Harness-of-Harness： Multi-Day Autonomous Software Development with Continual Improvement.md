# Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement

**收录日期：** 2026-09-02

**分类：** 多智能体+LLM

## 摘要

让 coding agent 在无人干预下持续数天、从零自主构建并不断完善生产级软件的框架：在已有 agent harness 之上引入 Plan—Code—Test 迭代闭环，核心挑战是随迭代增加让软件持续变好而非反复修补、原地打转。关键机制包括：平衡问题修复与功能增长、把开发拆成小而可验证的增量、约束可验证的交付结果而非限定工作流、为不同角色封装专业工具和模型并鼓励复用开源实现、分离开发验证与独立测试、上下文只暴露本地文档索引、维护版本化项目历史支持回退。GameCraft-Bench、FrontierSWE、ProgramBench 上 Codex+GPT-5.5、OpenCode+DeepSeek-V4-Pro、Pi+MiniMax-M3 三组 harness–model 组合经三轮迭代平均相对提升 52.25%、最高 82.86%；在 5 天全程无人干预的部署中，仅凭一份游戏产品需求文档自主开发出包含完整剧情、核心战斗机制和视觉效果的第一人称射击游戏，游戏与完整开发轨迹已公开。

**关键词：** 智能体框架、自主软件开发、持续改进、多天无人干预、coding agent、游戏生成

## 相关链接

- **PDF：** [论文链接](https://arxiv.org/pdf/2609.01481)
- **Project：** [项目主页](https://flesymeb.github.io/HarnessOfHarness/)
- **Code：** 暂无
- **Demo：** 暂无
