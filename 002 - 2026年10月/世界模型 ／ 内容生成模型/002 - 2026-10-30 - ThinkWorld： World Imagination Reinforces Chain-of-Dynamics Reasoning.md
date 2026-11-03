# ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning

**收录日期：** 2026-10-30

**分类：** 世界模型 ／ 内容生成模型

## 摘要

ThinkWorld（NVIDIA、KAIST）针对 VLA 泛化受限于带动作标注的机器人示教、而人类视频缺少可执行动作的问题，把动作写成跨本体共享的离散“动态链”（CoD）：统一末端增量动作与 FAST 式 tokenizer，将人手轨迹与机器人动作映射到同一运动词表；VLM 在 CoD 后接可学习 future query，在冻结 DINOv3 特征空间预测未来，以“想象未来与真实未来是否一致”作为 world-imagination reward 做 GRPO 强化。LIBERO 平均 97.3%、LIBERO-PRO 55.6%，优于 π0.5、VLA-JEPA；人类视频占比从 0 升到 50% 使 LIBERO-PRO 由 45.4% 升至 47.8%，部署时无需生成 CoD 或预测未来。

**关键词：** VLA、世界想象、动态链推理、跨本体动作、GRPO、机器人

## 相关链接

- **PDF：** [论文链接](https://arxiv.org/pdf/2610.37666)
- **Project：** 暂无
- **Code：** 暂无
- **Demo：** 暂无
