# Contributing

感谢贡献词条、修正比喻、补充 Cursor Rules。

## 加词条（最快）

1. 编辑 `scripts/terms.json`，追加：

```json
{"id":"your-term","cat":"ai","zh":"中文名","en":"English","one":"一句话","analogy":"比喻"}
```

`cat` 可选：`github` | `ai` | `cursor` | `cs` | `web`

2. 运行：

```bash
python3 scripts/build.py
```

3. 提 PR

## 加 Cursor Rule

在 `cursor-rules/` 新增 `.mdc`，参考现有文件 frontmatter。

## 原则

- **人话优先**：给零基础也能懂的比喻
- **一条一词**：不要一个小作文混多个概念
- **中英对照**：`en` 写常用英文说法
