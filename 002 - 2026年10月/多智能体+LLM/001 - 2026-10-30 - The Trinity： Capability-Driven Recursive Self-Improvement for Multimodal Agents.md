# The Trinity: Capability-Driven Recursive Self-Improvement for Multimodal Agents

**收录日期：** 2026-10-30

**分类：** 多智能体+LLM

## 摘要

The Trinity 冻结 Claude Opus 5 权重，把递归自我改进（RSI）的对象从“任务流程”换成“按底层能力组织的 Harness”：Evolver 从任务规范与验证轨迹中抽取状态跟踪、约束检查、证据验证等共同要求，把任务树重排为能力树；Creator 把同一节点的异构任务抽象成小型可验证模拟世界；Explorer 找失败轨迹并改进模块；子节点选择性继承父节点已验证的感知、记忆、推理、规划与循环控制模块，四轮迭代形成专用 Harness 树，部署时由 Capability-Aware Router 选分支。28 个训练 benchmark 均分 39.06→73.16，18 个未见 benchmark 37.45→63.61，完整自路由 71.27/60.96 接近 Oracle 的 73.16/63.61；两项真实机器人任务各 10 次测试均由 0% 升到 60%。作者亦指出提升含单独准备的技能、最终分数使用了 Oracle、机器人样本小，更准确的定位是“可审计的 Harness 自进化框架”而非通用 RSI。

**关键词：** 多模态Agent、递归自我改进、能力树、Harness、自路由、模拟环境

## 相关链接

- **PDF：** [论文链接](https://arxiv.org/pdf/2610.36077)
- **Project：** [项目主页](https://trinity-rsi.github.io/)
- **Code：** [代码仓库](https://github.com/InfRec-Cardinal/The-Trinity)
- **Demo：** 暂无
