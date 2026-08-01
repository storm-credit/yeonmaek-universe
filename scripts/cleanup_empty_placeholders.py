#!/usr/bin/env python3
"""Delete only truly empty/whitespace-only text placeholders and write an audit report.

The cleanup intentionally ignores non-empty files regardless of old audit labels.
It is idempotent and restricted to repository design-document roots.
This file is retained as the reproducible cleanup rule after the one-time run.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "docs/logs/migrations/2026-08-01-empty-placeholder-cleanup-report.md"
SCAN_ROOTS = [
    ROOT / "reviews",
    ROOT / "story",
    ROOT / "research",
    ROOT / "world",
    ROOT / "docs",
    ROOT / "memory",
    ROOT / "publishing",
    ROOT / "tests",
]
TEXT_SUFFIXES = {".md", ".txt", ".yml", ".yaml"}
PROTECTED = {
    REPORT.resolve(),
    (ROOT / "scripts/cleanup_empty_placeholders.py").resolve(),
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_empty_text(path: Path) -> bool:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return False
    try:
        return not path.read_text(encoding="utf-8").strip()
    except UnicodeDecodeError:
        return False


def main() -> int:
    deleted: list[str] = []

    for scan_root in SCAN_ROOTS:
        if not scan_root.exists():
            continue
        for path in sorted(scan_root.rglob("*")):
            if not path.is_file() or path.resolve() in PROTECTED:
                continue
            if is_empty_text(path):
                deleted.append(rel(path))
                path.unlink()

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "---",
        "status: completed",
        "accountable: A00",
        "responsible: [P01, P09]",
        "challenged_by: [A13]",
        "canon: false",
        "---",
        "# 빈 자리표시자 물리 정리 보고서",
        "",
        f"실행일: {date.today().isoformat()}",
        "",
        "## 안전 규칙",
        "",
        "- UTF-8로 읽히며 공백을 제거한 뒤 내용이 전혀 없는 파일만 삭제했다.",
        "- 파일명이나 과거 감사 목록만으로 삭제하지 않았다.",
        "- 한 글자라도 실질 내용이 있으면 보존했다.",
        "- 정본·후보·원고의 내용은 수정하지 않았다.",
        "",
        "## 결과",
        "",
        f"- 삭제한 실제 빈 파일: {len(deleted)}",
        "",
        "## 삭제 목록",
        "",
    ]
    if deleted:
        lines.extend(f"- `{item}`" for item in deleted)
    else:
        lines.append("- 없음 — 이미 정리된 상태")
    lines.extend(["", "## 판정", "", "`empty-placeholder-cleanup-complete`", ""])
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    print(f"Deleted {len(deleted)} empty placeholders. Report: {rel(REPORT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
