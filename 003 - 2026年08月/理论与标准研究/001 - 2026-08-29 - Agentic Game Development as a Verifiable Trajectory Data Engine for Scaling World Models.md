# Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models

**收录日期：** 2026-08-29

**分类：** 理论与标准研究

## 摘要

NUS、Berkeley 与 HKUST 的 position paper，回答“游戏开发为何对世界模型规模化重要”：AI 造游戏最有价值的不是最终的游戏，而是不断造错、基于引擎查出、纠正、修好并最终被接受的全过程。提出 RLHEV（Reinforcement Learning with Human-Engine Verification）后训练范式，用 AWoMo 全模态智能体按 UWDP 统一工作流协议串起 Unity、Unreal、Godot 中的编辑动作、状态、引擎检查与人工验收，形成“硬门+引擎分+人类分”三层反馈，把真实开发的长程轨迹变成世界模型的训练数据。UnitySceneBench（720 训练/80 验证/200 测试）上 Full RLHEV 最好 primary score 达 0.681，比最强非融合基线高 0.098；保存完整工具调用与检查链的协议把失败诊断从约 0.16 提升到约 0.72；跨引擎迁移（Unity→Unreal 0.25→0.35、Unity→Godot 0.15→0.35）亦有正信号。结论：游戏开发不只是世界模型的下游应用，而是它缺失的上游数据引擎。

**关键词：** 世界模型数据引擎、RLHEV、AWoMo、UWDP协议、游戏开发智能体、引擎验证、长程轨迹

## 相关链接

- **PDF：** [论文链接](https://arxiv.org/pdf/2608.25518)
- **Project：** 暂无
- **Code：** 暂无
- **Demo：** 暂无
