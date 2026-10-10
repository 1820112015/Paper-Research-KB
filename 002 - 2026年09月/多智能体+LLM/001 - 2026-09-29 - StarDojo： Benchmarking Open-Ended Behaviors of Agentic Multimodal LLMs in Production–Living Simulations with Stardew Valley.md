# StarDojo: Benchmarking Open-Ended Behaviors of Agentic Multimodal LLMs in Production–Living Simulations with Stardew Valley

**收录日期：** 2026-09-29

**分类：** 多智能体+LLM

## 摘要

ECCV 2026。基于《星露谷物语》构建的开放“生产–生活”仿真评测基准：现实社会是生产与社交耦合的系统，而现有游戏基准缺社交、社交基准缺生产、GUI 基准只做软件操作。StarDojo 依托 SMAPI 插件 + Python 封装层直读游戏内部状态，可暂停游戏适配大模型推理、多实例并行；观测融合截图与文本状态，定义 10 项基础动作；覆盖农耕、制作、探索、战斗、社交五大领域共 1000 项任务（另有 100 项精简子集 StarDojo-Lite），按易中难分级并内置自动评估。7 个主流多模态模型测试：最优 GPT-4.1 仅 12.7% 成功率，中高难度几乎全挂；错误归因：视觉理解 42%、多模态推理 21%、长期规划 21%、底层控制 16%；不暂停模拟真实推理延迟时性能显著恶化。已开源。

**关键词：** 智能体基准、生产生活仿真、星露谷物语、多模态大模型、长程规划、开放世界

## 相关链接

- **PDF：** [论文链接](https://arxiv.org/pdf/2507.07445)
- **Project：** [项目主页](https://stardojo-lab.github.io/)
- **Code：** 暂无
- **Demo：** 暂无
