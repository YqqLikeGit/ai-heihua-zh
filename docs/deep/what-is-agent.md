# Agent 不是聊天机器人

> 5 分钟读完 · Claude Code / Cursor Agent 用户

## 聊天 vs Agent

| | 聊天 | Agent |
|---|------|-------|
| 模式 | 问答 | **多步执行** |
| 能力 | 说 | 说 + 读文件 + 改代码 + 跑命令 |
| 类比 | 顾问 | 实习生进公司干活 |

## Agent 典型循环

```
用户目标 → AI 规划步骤 → 读代码 → 改文件 → 跑测试 → 汇报
```

Claude Code、Cursor Agent Mode 都是这个逻辑。

## 和 RAG 的区别

- **RAG**：先查资料再回答（开卷考试）
- **Agent**：查资料 + 动手改 + 验证（开卷 + 交卷）

## 风险

Agent 能删文件、跑 shell — 必须：
- 看 diff 再 accept
- 敏感目录加 rules 限制
- 重要操作人工确认

## 相关

- `./bin/heihua harness`
- `./bin/heihua tool-use`

[← 返回首页](../README.md)
