# MCP 是什么？和 API 有啥区别？

> 5 分钟读完 · AI 工具玩家必读

## 一句话

**MCP（Model Context Protocol）= AI 连接外部世界的标准「USB 口」。**

## 为什么需要 MCP？

以前每个 AI 工具接 Slack、GitHub、数据库都要**单独写一套集成**。  
MCP 统一了接口：写一次 MCP Server，Cursor / Claude Desktop / 其他客户端都能插。

## 和 API 的区别

| | 传统 API | MCP |
|---|----------|-----|
| 谁调用 | 你的代码 | **AI 模型** |
| 协议 | 各厂各样 | 统一标准 |
| 类比 | 每家电不同插头 | 统一 USB-C |

## 典型 MCP Server

- 读 GitHub Issue
- 查数据库
- 操作 Slack
- 跑浏览器

## 在 Cursor 里怎么用？

1. 配置 MCP Server（Settings → MCP）
2. Agent 自动决定何时调用
3. 你自然语言下指令，AI 去「插」工具

## 相关词条

- `./bin/heihua skills`
- `./bin/heihua agent`
- `./bin/heihua function-calling`

[← 返回首页](../README.md)
