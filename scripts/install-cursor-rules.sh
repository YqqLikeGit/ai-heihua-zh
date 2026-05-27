#!/usr/bin/env bash
# 一键安装 cursor-rules 到 ~/.cursor/rules 或项目 .cursor/rules
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-$HOME/.cursor/rules}"

mkdir -p "$TARGET"
cp -f "$ROOT/cursor-rules/"*.mdc "$TARGET/"
echo "已安装 $(ls "$ROOT/cursor-rules/"*.mdc | wc -l | tr -d ' ') 条规则 -> $TARGET"
ls -1 "$TARGET"/*.mdc 2>/dev/null | tail -5
