#!/usr/bin/env python3
"""Generate static site for GitHub Pages."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
index = json.loads((ROOT / "glossary" / "index.json").read_text("utf-8"))

rows = []
for t in index["terms"]:
    rows.append(
        f"<tr><td><b>{html.escape(t['zh'])}</b></td>"
        f"<td>{html.escape(t['en'])}</td>"
        f"<td>{html.escape(t['one'])}</td>"
        f"<td><a href='https://github.com/YqqLikeGit/ai-heihua-zh/blob/main/glossary/{t['cat']}/{t['id']}.md'>详解</a></td></tr>"
    )

page = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>AI 黑话词典 · {index['count']} 词条</title>
<style>
body{{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif;max-width:960px;margin:0 auto;padding:24px;line-height:1.6;background:#0d1117;color:#e6edf3}}
a{{color:#58a6ff}} h1{{font-size:1.8rem}} table{{width:100%;border-collapse:collapse;font-size:14px}}
th,td{{border:1px solid #30363d;padding:8px;text-align:left}} th{{background:#161b22}}
.cta{{background:#238636;color:#fff;padding:12px 20px;border-radius:8px;text-decoration:none;display:inline-block;margin:16px 0;font-weight:600}}
</style>
</head>
<body>
<h1>AI 黑话词典</h1>
<p>程序员 & AI 时代 · {index['count']} 条中英对照 · <a href="https://github.com/YqqLikeGit/ai-heihua-zh">GitHub 仓库</a></p>
<a class="cta" href="https://github.com/YqqLikeGit/ai-heihua-zh">⭐ Star on GitHub</a>
<table>
<thead><tr><th>中文</th><th>English</th><th>一句话</th><th></th></tr></thead>
<tbody>
{''.join(rows)}
</tbody>
</table>
<p>CLI: <code>git clone ... && ./bin/heihua star</code></p>
</body></html>
"""
SITE.mkdir(exist_ok=True)
(SITE / "index.html").write_text(page, encoding="utf-8")
print(f"Site -> {SITE / 'index.html'}")
