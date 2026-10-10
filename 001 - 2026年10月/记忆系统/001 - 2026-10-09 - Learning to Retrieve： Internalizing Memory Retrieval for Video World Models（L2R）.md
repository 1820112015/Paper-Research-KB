# Learning to Retrieve: Internalizing Memory Retrieval for Video World Models（L2R）

**收录日期：** 2026-10-09

**分类：** 记忆系统

## 摘要

解决“镜头转回来，物体或场景还能维持吗”的记忆问题：不计算相机 FoV overlap（不可学）、不建 3D 点云（太慢）、也不用外部 query 检索上下文（记忆与生成被隔离），而是在 video diffusion 内部做记忆检索。受 RNN 循环状态与线性注意力启发，L2R 把模型内部状态转化为存储过往上下文的记忆，由摄像机输入控制的门控学习“检索什么”、二值触发器学习“何时检索”。在 Echo-Memory 上域内域外均优于已有记忆模块，VBench 证明显著提升场景一致性且不降视觉质量；代码两周内开源。

**关键词：** 视频世界模型、内生记忆检索、注意力内部记忆、场景一致性、门控检索、视频扩散

## 相关链接

- **PDF：** [论文链接](https://arxiv.org/pdf/2610.11444)
- **Project：** 暂无
- **Code：** 暂无
- **Demo：** 暂无
