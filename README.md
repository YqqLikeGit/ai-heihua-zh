# AI 黑话词典 · 5 分钟搞懂一个概念

[![GitHub stars](https://img.shields.io/github/stars/YqqLikeGit/ai-heihua-zh?style=for-the-badge&logo=github)](https://github.com/YqqLikeGit/ai-heihua-zh/stargazers)
[![Terms](https://img.shields.io/badge/词条-100+-blue?style=for-the-badge)](#速查表)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![CLI](https://img.shields.io/badge/CLI-终端查词-orange?style=for-the-badge)](#终端查词)

> **程序员 & AI 时代黑话图解** — GitHub、Star、MCP、Agent、RAG、Cursor… 收藏这一个仓库就够了。

[English TL;DR](#english) · [深度文章](#深度文章-5-分钟) · [贡献词条](#贡献) · [在线阅读](https://yqqlikegit.github.io/ai-heihua-zh/)

---

## 为什么做这个？

- 抖音「编程名词扫盲」单条 **6000+ 收藏** — 说明大家真的需要
- [computerese-cross-references](https://github.com/EarsEyesMouth/computerese-cross-references) **1000+ Star** — 经典术语对照依然缺 **2026 AI 新词**
- [one-small-step](https://github.com/karminski/one-small-step) **6900+ Star** — 证明「5 分钟搞懂一个概念」模式有效

**本项目 = 经典 CS + GitHub 必备 + AI/Cursor 2026 热词 + 中文 Cursor Rules，中英对照 + 人话比喻 + 终端 CLI 查词。**

---

## Cursor Rules 一键安装

```bash
git clone https://github.com/YqqLikeGit/ai-heihua-zh.git
cd ai-heihua-zh
bash scripts/install-cursor-rules.sh          # -> ~/.cursor/rules
# 或项目级：bash scripts/install-cursor-rules.sh .cursor/rules
```

含：通用中文规范 · Python · TypeScript/React · Git Commit · 见 `cursor-rules/`

---

## Cursor MCP 一键配置（姊妹仓库 · 2026 热点）

配不好 `mcp.json`？用这个：

👉 **[cursor-mcp-starter-zh](https://github.com/YqqLikeGit/cursor-mcp-starter-zh)** — 模板 + `install.sh` + `doctor.sh`

```bash
git clone https://github.com/YqqLikeGit/cursor-mcp-starter-zh.git
cd cursor-mcp-starter-zh && bash scripts/install.sh minimal
```

## 终端查词

```bash
# 方式 1：克隆（推荐）
git clone https://github.com/YqqLikeGit/ai-heihua-zh.git
cd ai-heihua-zh
./bin/heihua star          # 查「Star 是什么」
./bin/heihua mcp           # 查 MCP

# 方式 2：npx 免安装（需 Node）
npx --yes github:YqqLikeGit/ai-heihua-zh heihua mcp
```

---

## 深度文章（5 分钟）

| 文章 | 适合谁 |
|------|--------|
| [GitHub 到底是什么？](docs/deep/what-is-github.md) | 完全零基础 |
| [Star 能当简历吗？怎么涨到 1000？](docs/deep/github-stars-guide.md) | 想涨 Star 的开发者 |
| [MCP 是什么？和 API 有啥区别？](docs/deep/what-is-mcp.md) | AI 工具玩家 |
| [Agent 不是聊天机器人](docs/deep/what-is-agent.md) | 想用 Claude Code / Cursor Agent 的人 |
| [Vibe Coding 会取代程序员吗？](docs/deep/vibe-coding.md) | 焦虑的 coder |

---

## 速查表

<!-- AUTO-GENERATED TABLE START -->

### GitHub & 开源 (22 条)

| 术语 | English | 一句话 | 详解 |
|------|---------|--------|------|
| **Branch / 分支** | Branch | 平行开发线，互不影响 | [📖](glossary/github/branch.md) |
| **Clone / 克隆** | Clone | 把远程仓库完整下载到本机 | [📖](glossary/github/clone.md) |
| **Commit / 提交** | Commit | 保存一次代码快照，附带说明 | [📖](glossary/github/commit.md) |
| **Contributor / 贡献者** | Contributor | 参与过项目代码或文档的人 | [📖](glossary/github/contributor.md) |
| **Discussions** | Discussions | 仓库内的论坛式讨论区 | [📖](glossary/github/discussions.md) |
| **Fork / 复刻** | Fork | 复制别人的仓库到你账号下，可自由修改 | [📖](glossary/github/fork.md) |
| **Gist** | Gist | GitHub 的代码片段分享 | [📖](glossary/github/gist.md) |
| **GitHub** | GitHub | 全球最大的代码托管与开源协作平台，程序员的「代码朋友圈」 | [📖](glossary/github/github.md) |
| **GitHub Actions** | GitHub Actions | 在 GitHub 上自动跑 CI/CD 流水线 | [📖](glossary/github/actions.md) |
| **Issue / 议题** | Issue | 提 Bug、提需求、讨论问题的工单 | [📖](glossary/github/issue.md) |
| **Markdown** | Markdown | 轻量标记语言，README 常用 | [📖](glossary/github/markdown.md) |
| **Merge / 合并** | Merge | 把分支改动合进主分支 | [📖](glossary/github/merge.md) |
| **Pull Request / PR** | Pull Request | 请求把你的改动合并进原项目 | [📖](glossary/github/pull-request.md) |
| **README** | README | 项目首页说明，第一眼看到的内容 | [📖](glossary/github/readme.md) |
| **Release / 发行版** | Release | 打包标记的稳定版本，方便下载 | [📖](glossary/github/release.md) |
| **Repository / 仓库** | Repository | 存放项目全部文件与历史的文件夹 | [📖](glossary/github/repository.md) |
| **Star / 星星** | Star | 给项目点赞收藏，表示「这个有用」 | [📖](glossary/github/star.md) |
| **Watch / 关注** | Watch | 订阅仓库动态通知 | [📖](glossary/github/watch.md) |
| **上游** | Upstream | 你 Fork 的原仓库 | [📖](glossary/github/upstream.md) |
| **下游** | Downstream | 从你的仓库 Fork 出去的副本 | [📖](glossary/github/downstream.md) |
| **开源** | Open Source | 公开源代码，他人可查看、使用、贡献 | [📖](glossary/github/open-source.md) |
| **开源协议** | License | 规定别人如何使用你的代码 | [📖](glossary/github/license.md) |

### AI & 大模型 (32 条)

| 术语 | English | 一句话 | 详解 |
|------|---------|--------|------|
| **A2A** | Agent2Agent | 多个 AI Agent 互相通信的协议 | [📖](glossary/ai/a2a.md) |
| **AI 工作流** | AI Workflow | 多个 AI 步骤串联的自动化流程 | [📖](glossary/ai/workflow.md) |
| **Agent / 智能体** | Agent | 能自己规划步骤、调用工具的 AI | [📖](glossary/ai/agent.md) |
| **Computer Use** | Computer Use | AI 直接操控鼠标键盘操作电脑 | [📖](glossary/ai/computer-use.md) |
| **Harness / 驾驭工程** | Harness Engineering | 给 AI Agent 设计可控、可验证的工作环境 | [📖](glossary/ai/harness.md) |
| **MCP** | Model Context Protocol | AI 连接外部工具和数据的标准「插座」 | [📖](glossary/ai/mcp.md) |
| **RAG / 检索增强** | RAG | 先查资料再回答，减少胡编 | [📖](glossary/ai/rag.md) |
| **Skills / 技能** | Skills | 教 AI 在特定场景下怎么做事的说明书 | [📖](glossary/ai/skills.md) |
| **Token / 词元** | Token | 模型处理文本的最小单位，影响计费与长度 | [📖](glossary/ai/token.md) |
| **上下文工程** | Context Engineering | 设计喂给模型的信息与结构 | [📖](glossary/ai/context-engineering.md) |
| **上下文窗口** | Context Window | 模型一次能「记住」的对话长度上限 | [📖](glossary/ai/context-window.md) |
| **事实锚定** | Grounding | 让回答基于可验证事实而非纯生成 | [📖](glossary/ai/grounding.md) |
| **函数调用** | Function Calling | AI 决定调用哪个 API 并传参数 | [📖](glossary/ai/function-calling.md) |
| **向量嵌入** | Embedding | 把文字变成数字向量，便于语义搜索 | [📖](glossary/ai/embedding.md) |
| **多模态** | Multimodal | 同时理解文字、图片、音频等 | [📖](glossary/ai/multimodal.md) |
| **大语言模型** | LLM | 读懂并生成人类语言的 AI 模型 | [📖](glossary/ai/llm.md) |
| **子 Agent** | Sub-agent | 主 Agent 派生的专项小 Agent | [📖](glossary/ai/subagent.md) |
| **工具使用** | Tool Use | AI 调用搜索、代码执行等外部能力 | [📖](glossary/ai/tool-use.md) |
| **幻觉** | Hallucination | AI 自信地编造不存在的事实 | [📖](glossary/ai/hallucination.md) |
| **微调** | Fine-tuning | 在通用模型上继续训练以适应特定任务 | [📖](glossary/ai/fine-tuning.md) |
| **思维链** | Chain-of-Thought | 让 AI 分步推理，提高复杂题正确率 | [📖](glossary/ai/chain-of-thought.md) |
| **护栏** | Guardrails | 限制 AI 输出范围的安全规则 | [📖](glossary/ai/guardrails.md) |
| **推理** | Inference | 模型运行生成结果的过程 | [📖](glossary/ai/inference.md) |
| **推理模型** | Reasoning Model | 花更多思考步骤换更高正确率 | [📖](glossary/ai/reasoning-model.md) |
| **提示词** | Prompt | 你给 AI 的指令或问题 | [📖](glossary/ai/prompt.md) |
| **氛围编程** | Vibe Coding | 用自然语言描述意图，让 AI 写大部分代码 | [📖](glossary/ai/vibe-coding.md) |
| **温度** | Temperature | 控制输出随机性，越高越发散 | [📖](glossary/ai/temperature.md) |
| **系统提示** | System Prompt | 设定 AI 角色与行为边界的隐藏指令 | [📖](glossary/ai/system-prompt.md) |
| **蒸馏** | Distillation | 大模型教小模型，保留部分能力 | [📖](glossary/ai/distillation.md) |
| **训练** | Training | 用数据调整模型参数的学习过程 | [📖](glossary/ai/training.md) |
| **评测** | Evals | 系统化测试 AI 输出质量 | [📖](glossary/ai/evals.md) |
| **量化** | Quantization | 降低模型精度以减小体积、加速推理 | [📖](glossary/ai/quantization.md) |

### Cursor & Claude Code (15 条)

| 术语 | English | 一句话 | 详解 |
|------|---------|--------|------|
| **Agent 模式** | Agent Mode | AI 自动多步执行：读文件、改代码、跑命令 | [📖](glossary/cursor/agent-mode.md) |
| **Claude Code** | Claude Code | Anthropic 的终端 AI 编程 Agent | [📖](glossary/cursor/claude-code.md) |
| **Claude Desktop** | Claude Desktop | Anthropic 官方桌面聊天客户端 | [📖](glossary/cursor/claude-desktop.md) |
| **Composer** | Composer | Cursor 中多文件协同编辑的 AI 模式 | [📖](glossary/cursor/composer.md) |
| **Copilot / 副驾驶** | Copilot | AI 在编码时实时补全与建议 | [📖](glossary/cursor/copilot.md) |
| **Cursor** | Cursor | 内置 AI 的代码编辑器，基于 VS Code | [📖](glossary/cursor/cursor.md) |
| **Diff** | Diff | 修改前后的代码对比 | [📖](glossary/cursor/diff.md) |
| **MCP 服务器** | MCP Server | 对外暴露工具能力，供 AI 客户端连接 | [📖](glossary/cursor/mcp-server.md) |
| **MDC 规则** | MDC Rules | Cursor 的规则文件格式 .mdc | [📖](glossary/cursor/mdc.md) |
| **Rules / 规则** | Rules | 持久化告诉 AI 项目规范与偏好 | [📖](glossary/cursor/rules.md) |
| **Tab 补全** | Tab Completion | 按 Tab 接受 AI 生成的代码建议 | [📖](glossary/cursor/tab-complete.md) |
| **上下文** | Context | AI 当前能看到的代码与对话 | [📖](glossary/cursor/context.md) |
| **代码库索引** | Codebase Index | AI 理解整个项目结构的预处理 | [📖](glossary/cursor/codebase-index.md) |
| **后台 Agent** | Background Agent | 在云端继续跑的 Agent 任务 | [📖](glossary/cursor/background-agent.md) |
| **行内编辑** | Inline Edit | 在编辑器里直接让 AI 改选中代码 | [📖](glossary/cursor/inline-edit.md) |

### 计算机基础 (40 条)

| 术语 | English | 一句话 | 详解 |
|------|---------|--------|------|
| **API** | API | 程序之间对话的约定接口 | [📖](glossary/cs/api.md) |
| **CI/CD** | CI/CD | 自动测试构建并部署代码流水线 | [📖](glossary/cs/ci-cd.md) |
| **Docker** | Docker | 把应用和环境打包成容器运行 | [📖](glossary/cs/docker.md) |
| **Git** | Git | 分布式版本控制工具，跟踪代码变更 | [📖](glossary/cs/git.md) |
| **JSON** | JSON | 轻量数据交换格式，键值对嵌套 | [📖](glossary/cs/json.md) |
| **JWT** | JWT | 自包含的加密身份令牌 | [📖](glossary/cs/jwt.md) |
| **K8s** | Kubernetes | 编排大量容器的集群管理系统 | [📖](glossary/cs/kubernetes.md) |
| **Lint** | Lint | 静态检查代码风格与常见错误 | [📖](glossary/cs/lint.md) |
| **NoSQL** | NoSQL | 非关系型数据库，灵活 schema | [📖](glossary/cs/nosql.md) |
| **OAuth** | OAuth | 第三方授权登录，不暴露密码 | [📖](glossary/cs/oauth.md) |
| **REST** | REST | 用 HTTP 动词操作资源的 API 风格 | [📖](glossary/cs/rest.md) |
| **SQL** | SQL | 操作关系型数据库的语言 | [📖](glossary/cs/sql.md) |
| **中间件** | Middleware | 请求处理链中的通用逻辑层 | [📖](glossary/cs/middleware.md) |
| **依赖** | Dependency | 项目运行需要引用的第三方库 | [📖](glossary/cs/dependency.md) |
| **函数式** | Functional | 用纯函数组合构建程序 | [📖](glossary/cs/functional.md) |
| **单体应用** | Monolith | 所有功能在一个程序里 | [📖](glossary/cs/monolith.md) |
| **单例** | Singleton | 全局只允许一个实例的设计模式 | [📖](glossary/cs/singleton.md) |
| **单元测试** | Unit Test | 测试最小代码单元是否正确 | [📖](glossary/cs/unit-test.md) |
| **可扩展性** | Scalability | 系统应对流量增长的能力 | [📖](glossary/cs/scalability.md) |
| **同步** | Sync | 一步一步等前一步完成 | [📖](glossary/cs/sync.md) |
| **吞吐量** | Throughput | 单位时间处理的请求量 | [📖](glossary/cs/throughput.md) |
| **库** | Library | 可复用的函数/组件集合 | [📖](glossary/cs/library.md) |
| **延迟** | Latency | 请求发出到收到响应的时间 | [📖](glossary/cs/latency.md) |
| **开发容器** | Dev Container | 标准化 Docker 开发环境 | [📖](glossary/cs/devcontainer.md) |
| **异步** | Async | 不阻塞等待，完成后回调 | [📖](glossary/cs/async.md) |
| **微服务** | Microservice | 把大系统拆成多个小服务独立部署 | [📖](glossary/cs/microservice.md) |
| **技术债** | Technical Debt | 为赶进度留下的需日后偿还的代码问题 | [📖](glossary/cs/technical-debt.md) |
| **数据库** | Database | 结构化存储与查询数据 | [📖](glossary/cs/database.md) |
| **框架** | Framework | 半成品脚手架，规定代码组织方式 | [📖](glossary/cs/framework.md) |
| **死锁** | Deadlock | 两个任务互相等待对方释放资源 | [📖](glossary/cs/deadlock.md) |
| **环境变量** | Environment Variable | 程序外配置，如 API Key | [📖](glossary/cs/env-var.md) |
| **竞态条件** | Race Condition | 多线程时序不确定导致结果异常 | [📖](glossary/cs/race-condition.md) |
| **缓存** | Cache | 把常用数据放近处加速读取 | [📖](glossary/cs/cache.md) |
| **语义化版本** | SemVer | 主.次.补丁 版本号约定 | [📖](glossary/cs/semver.md) |
| **调试** | Debug | 定位并修复程序错误 | [📖](glossary/cs/debug.md) |
| **递归** | Recursion | 函数调用自身 | [📖](glossary/cs/recursion.md) |
| **重构** | Refactor | 不改功能前提下优化代码结构 | [📖](glossary/cs/refactor.md) |
| **闭包** | Closure | 函数记住定义时的外部变量 | [📖](glossary/cs/closure.md) |
| **集成测试** | Integration Test | 测试多个模块联调是否正常 | [📖](glossary/cs/integration-test.md) |
| **面向对象** | OOP | 用对象封装数据与行为 | [📖](glossary/cs/oop.md) |

### Web & 网络 (24 条)

| 术语 | English | 一句话 | 详解 |
|------|---------|--------|------|
| **Bearer Token** | Bearer Token | HTTP 头里带令牌的身份验证 | [📖](glossary/web/jwt-auth.md) |
| **CDN** | CDN | 就近缓存静态资源加速访问 | [📖](glossary/web/cdn.md) |
| **CORS** | CORS | 浏览器跨域访问安全策略 | [📖](glossary/web/cors.md) |
| **CSS** | CSS | 控制网页样式与布局 | [📖](glossary/web/css.md) |
| **DNS** | DNS | 域名翻译成 IP 地址 | [📖](glossary/web/dns.md) |
| **GraphQL** | GraphQL | 客户端指定要哪些字段的查询语言 | [📖](glossary/web/graphql.md) |
| **HTML** | HTML | 网页结构的标记语言 | [📖](glossary/web/html.md) |
| **HTTP** | HTTP | 浏览器与服务器通信协议 | [📖](glossary/web/http.md) |
| **HTTPS** | HTTPS | 加密的 HTTP | [📖](glossary/web/https.md) |
| **JavaScript** | JavaScript | 浏览器与 Node 的脚本语言 | [📖](glossary/web/javascript.md) |
| **Node.js** | Node.js | 服务器端运行 JavaScript | [📖](glossary/web/nodejs.md) |
| **React** | React | 组件化 UI 库，Facebook 出品 | [📖](glossary/web/react.md) |
| **SEO** | SEO | 让搜索引擎更好收录网站 | [📖](glossary/web/seo.md) |
| **TCP** | TCP | 可靠有序的数据传输协议 | [📖](glossary/web/tcp.md) |
| **TypeScript** | TypeScript | 带类型的 JavaScript 超集 | [📖](glossary/web/typescript.md) |
| **UDP** | UDP | 快速但可能丢包传输 | [📖](glossary/web/udp.md) |
| **Vue** | Vue | 渐进式前端框架，国内流行 | [📖](glossary/web/vue.md) |
| **WebSocket** | WebSocket | 浏览器与服务器双向实时通道 | [📖](glossary/web/websocket.md) |
| **单页应用** | SPA | 一个 HTML 页内切换视图 | [📖](glossary/web/spa.md) |
| **反向代理** | Reverse Proxy | 挡在服务器前统一接流量 | [📖](glossary/web/reverse-proxy.md) |
| **打包工具** | Bundler | 合并压缩前端资源 | [📖](glossary/web/webpack.md) |
| **服务端渲染** | SSR | 服务器生成 HTML 再发给浏览器 | [📖](glossary/web/ssr.md) |
| **本地主机** | Localhost | 本机地址 127.0.0.1 | [📖](glossary/web/localhost.md) |
| **负载均衡** | Load Balancer | 把流量分到多台服务器 | [📖](glossary/web/load-balancer.md) |

<!-- AUTO-GENERATED TABLE END -->

---

## English

**AI Heihua Dictionary** — Plain-language glossary for programmers entering the AI era.  
100+ terms in Chinese with English names, analogies, CLI lookup, and 5-min deep dives.  
Star ⭐ if this saves you one Google search.

---

## 贡献

1. Fork 本仓库
2. 编辑 `scripts/terms.json` 增加词条
3. 运行 `python3 scripts/build.py`
4. 提 PR

---

## License

MIT · Copyright (c) 2026 RUDY YU / YqqLikeGit

**如果觉得有用，请 Star ⭐ — 这是对中国开发者最友好的 AI 黑话词典之一。**
