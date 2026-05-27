#!/usr/bin/env python3
"""Build glossary pages, index.json, and README tables from terms.json."""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TERMS = json.loads((Path(__file__).parent / "terms.json").read_text("utf-8"))
CAT_NAMES = {
    "github": "GitHub & 开源",
    "ai": "AI & 大模型",
    "cursor": "Cursor & Claude Code",
    "cs": "计算机基础",
    "web": "Web & 网络",
}


def write_glossary_pages() -> None:
    by_cat: dict[str, list] = defaultdict(list)
    for t in TERMS:
        by_cat[t["cat"]].append(t)

    for cat, items in by_cat.items():
        cat_dir = ROOT / "glossary" / cat
        cat_dir.mkdir(parents=True, exist_ok=True)
        for t in sorted(items, key=lambda x: x["id"]):
            path = cat_dir / f"{t['id']}.md"
            body = f"""# {t['zh']}

> **{t['en']}** · #{cat}

## 一句话

{t['one']}

## 打个比方

{t['analogy']}

## 为什么重要

- 面试、读文档、看 GitHub 项目时会反复遇到
- 搞懂黑话 = 少踩坑、少被 AI 忽悠

## 相关

- 返回 [词典首页](../../README.md)
- 命令行查词：`./bin/heihua {t['id']}`

---
*贡献：发现解释不准？[提 Issue](https://github.com/YqqLikeGit/ai-heihua-zh/issues)*
"""
            path.write_text(body, encoding="utf-8")


def write_index_json() -> None:
    out = ROOT / "glossary" / "index.json"
    payload = {
        "version": 1,
        "count": len(TERMS),
        "categories": CAT_NAMES,
        "terms": TERMS,
    }
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_readme_table() -> None:
    lines = ["<!-- AUTO-GENERATED TABLE START -->", ""]
    by_cat: dict[str, list] = defaultdict(list)
    for t in TERMS:
        by_cat[t["cat"]].append(t)

    for cat in ["github", "ai", "cursor", "cs", "web"]:
        lines.append(f"### {CAT_NAMES[cat]} ({len(by_cat[cat])} 条)")
        lines.append("")
        lines.append("| 术语 | English | 一句话 | 详解 |")
        lines.append("|------|---------|--------|------|")
        for t in sorted(by_cat[cat], key=lambda x: x["zh"]):
            link = f"[📖](glossary/{cat}/{t['id']}.md)"
            one = t["one"].replace("|", "\\|")
            lines.append(f"| **{t['zh']}** | {t['en']} | {one} | {link} |")
        lines.append("")
    lines.append("<!-- AUTO-GENERATED TABLE END -->")
    marker_start = "<!-- AUTO-GENERATED TABLE START -->"
    marker_end = "<!-- AUTO-GENERATED TABLE END -->"
    readme = (ROOT / "README.template.md").read_text("utf-8")
    before = readme.split(marker_start)[0]
    after = readme.split(marker_end)[1]
    table_block = "\n".join(lines)
    (ROOT / "README.md").write_text(before + table_block + after, encoding="utf-8")


def main() -> None:
    write_glossary_pages()
    write_index_json()
    write_readme_table()
    import subprocess
    subprocess.run([sys.executable, str(Path(__file__).parent / "build-site.py")], check=True)
    print(f"Built {len(TERMS)} terms")


if __name__ == "__main__":
    main()
