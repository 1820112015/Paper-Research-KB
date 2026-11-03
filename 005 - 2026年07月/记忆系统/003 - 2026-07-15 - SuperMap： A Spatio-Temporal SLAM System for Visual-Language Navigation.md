# SuperMap: A Spatio-Temporal SLAM System for Visual-Language Navigation

**收录日期：** 2026-07-15

**分类：** 记忆系统

## 摘要

SuperMap 是 CMU AirLab 提出的实时开放词汇时空 SLAM 系统，目标是为机器人构建可持续更新的长期空间记忆。系统把高频几何 SLAM 与异步开放词汇感知结合，通过三维感知的实例关联与重新激活、对象存在性和标签置信度更新，在遮挡、漏检、物体搬移、出现或消失时维持稳定身份并清理过期语义。最终地图被组织为可查询的 4D 实例级场景图，记录对象的语义、空间关系与变化历史，可直接支持视觉语言导航和具身推理。论文在 ScanNet、动态变化场景及真实机器人上进行评测，展示了在线运行、实例级分割和变化检测能力，并完成连续两小时的 CMU 校园室内外部署。当前局限包括对高度动态物体的跟踪能力有限，以及开放词汇检测仍依赖预定义提示词；项目已公开系统代码和交互式三维地图。

**关键词：** 时空SLAM、开放词汇感知、4D场景图、持久空间记忆、视觉语言导航、具身智能

## 相关链接

- **PDF：** [论文链接](https://www.roboticsproceedings.org/rss22/p052.pdf)
- **Project：** [项目主页](https://superodometry.com/supermap)
- **Code：** [代码仓库](https://github.com/superxslam/SuperMap)
- **Demo：** 暂无
