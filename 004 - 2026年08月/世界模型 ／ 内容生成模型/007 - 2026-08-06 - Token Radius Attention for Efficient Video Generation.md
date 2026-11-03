# Token Radius Attention for Efficient Video Generation

**收录日期：** 2026-08-06

**分类：** 世界模型 / 内容生成模型

## 摘要

Token Radius Attention（TRA）面向视频扩散 Transformer 的注意力计算瓶颈，利用每个 token 的注意力熵估计其独立预算，并将预算转换为以查询 token 为中心、随时间衰减的半径掩码。该方法无需训练，可在 Wan、HunyuanVideo 等配置上减少大部分注意力交互，在画质基本保持的前提下获得约 1.56–2.05 倍加速。

**关键词：** 视频生成加速、稀疏注意力、Token Radius、VDiT、免训练、注意力熵

## 相关链接

- **PDF：** [论文链接](https://arxiv.org/pdf/2608.02504v1)
- **Project：** 暂无
- **Code：** 暂无
- **Demo：** 暂无
