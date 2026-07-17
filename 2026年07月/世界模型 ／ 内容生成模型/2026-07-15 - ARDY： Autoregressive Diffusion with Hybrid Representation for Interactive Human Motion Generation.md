# ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation

**收录日期：** 2026-07-15  
**分类：** 世界模型 / 内容生成模型

## 摘要

ARDY 是面向动画、仿真和人形机器人的实时交互式三维人体动作生成框架，解决离线方法控制精确但速度不足、在线方法实时却难以理解复杂文本和长程约束的问题。它采用“显式根节点特征 + 身体潜变量”的混合表示，在轨迹控制精度与生成效率之间取得平衡，并设计带可变历史上下文的两阶段自回归 Transformer 去噪器，使模型能够在线接受文字提示、根节点路径、全身关键帧以及稀疏关节位置和旋转等约束。模型在 HumanML3D 与约 700 小时的 Bones Rigplay 高质量动捕数据上验证，四步扩散平均生成延迟约 33 ms，可实时响应鼠标和键盘输入并持续修改动作。论文也指出其超长历史上下文仍有计算开销，纯运动学建模可能产生脚滑和抖动，后续需要更高效的记忆结构、快捷扩散和物理动力学约束。

**关键词：** 交互式人体动作生成、自回归扩散、混合表示、流式生成、运动学约束、实时控制

## 相关链接

- **PDF：** [论文链接](https://arxiv.org/pdf/2607.08741)
- **Project：** [项目主页](https://research.nvidia.com/labs/sil/projects/ardy/)
- **Code：** [代码仓库](https://github.com/nv-tlabs/ardy)
- **Demo：** 暂无
