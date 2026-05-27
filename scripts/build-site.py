#!/usr/bin/env python3
"""Generate searchable GitHub Pages site."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
index = json.loads((ROOT / "glossary" / "index.json").read_text("utf-8"))
terms_json = json.dumps(index["terms"], ensure_ascii=False)

rows = []
for t in index["terms"]:
    cat = t["cat"]
    tid = t["id"]
    zh = html.escape(t["zh"])
    en = html.escape(t["en"])
    one = html.escape(t["one"])
    rows.append(
        f'<tr data-cat="{cat}" data-q="{html.escape(t["zh"] + " " + t["en"] + " " + t["id"] + " " + t["one"]).lower()}">'
        f"<td><b>{zh}</b></td><td>{en}</td><td>{one}</td>"
        f'<td><a href="https://github.com/YqqLikeGit/ai-heihua-zh/blob/main/glossary/{cat}/{tid}.md">详解</a></td></tr>'
    )

page = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="description" content="AI & 编程黑话词典 — {index['count']} 条中英对照，MCP Agent RAG Cursor GitHub Star 速查"/>
<title>AI 黑话词典 · {index['count']} 词条</title>
<style>
:root{{--bg:#0d1117;--fg:#e6edf3;--muted:#8b949e;--border:#30363d;--accent:#238636;--link:#58a6ff}}
*{{box-sizing:border-box}} body{{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif;max-width:980px;margin:0 auto;padding:20px;line-height:1.55;background:var(--bg);color:var(--fg)}}
a{{color:var(--link)}} .hero{{margin-bottom:20px}} .cta{{background:var(--accent);color:#fff;padding:10px 18px;border-radius:8px;text-decoration:none;font-weight:600;display:inline-block}}
.toolbar{{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0;align-items:center}}
#q{{flex:1;min-width:200px;padding:10px 14px;border-radius:8px;border:1px solid var(--border);background:#161b22;color:var(--fg);font-size:16px}}
.chip{{padding:6px 12px;border-radius:999px;border:1px solid var(--border);background:#161b22;color:var(--muted);cursor:pointer;font-size:13px}}
.chip.on{{background:#388bfd33;color:var(--link);border-color:#388bfd}}
table{{width:100%;border-collapse:collapse;font-size:14px}}
th,td{{border:1px solid var(--border);padding:8px;text-align:left;vertical-align:top}}
th{{background:#161b22;position:sticky;top:0}}
tr.hide{{display:none}} .meta{{color:var(--muted);font-size:14px}}
</style>
</head>
<body>
<div class="hero">
<h1>AI 黑话词典</h1>
<p class="meta">{index['count']} 条 · GitHub · MCP · Agent · Cursor · Star … 中英对照 + 人话比喻</p>
<a class="cta" href="https://github.com/YqqLikeGit/ai-heihua-zh">⭐ Star on GitHub</a>
</div>
<div class="toolbar">
<input id="q" type="search" placeholder="搜索：star、mcp、agent、闭包…" autofocus/>
<span class="chip on" data-cat="all">全部</span>
<span class="chip" data-cat="github">GitHub</span>
<span class="chip" data-cat="ai">AI</span>
<span class="chip" data-cat="cursor">Cursor</span>
<span class="chip" data-cat="cs">CS</span>
<span class="chip" data-cat="web">Web</span>
</div>
<p class="meta" id="count">{index['count']} 条显示</p>
<table>
<thead><tr><th>中文</th><th>English</th><th>一句话</th><th></th></tr></thead>
<tbody id="tb">
{''.join(rows)}
</tbody>
</table>
<p class="meta">CLI: <code>git clone https://github.com/YqqLikeGit/ai-heihua-zh && ./bin/heihua mcp</code></p>
<script>
const q=document.getElementById('q'),tb=document.getElementById('tb'),rows=[...tb.querySelectorAll('tr')],countEl=document.getElementById('count');
let cat='all';
function apply(){{
  const s=q.value.trim().toLowerCase();
  let n=0;
  rows.forEach(r=>{{
    const okCat=cat==='all'||r.dataset.cat===cat;
    const okQ=!s||r.dataset.q.includes(s);
    const show=okCat&&okQ;
    r.classList.toggle('hide',!show);
    if(show)n++;
  }});
  countEl.textContent=n+' 条显示';
}}
q.addEventListener('input',apply);
document.querySelectorAll('.chip').forEach(c=>c.addEventListener('click',()=>{{
  document.querySelectorAll('.chip').forEach(x=>x.classList.remove('on'));
  c.classList.add('on'); cat=c.dataset.cat; apply();
}}));
</script>
</body></html>
"""
DOCS.mkdir(exist_ok=True)
(DOCS / "index.html").write_text(page, encoding="utf-8")
(DOCS / "glossary.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Pages -> {DOCS / 'index.html'} ({index['count']} terms)")
