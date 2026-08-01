#!/usr/bin/env python3
"""Migrate the active protagonist working name from 서이안/이안 to 서하진/하진.

Historical migration statements are preserved. The script is idempotent and writes
an auditable report. It does not change GitHub issue bodies or binary files.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "docs/logs/migrations/2026-08-01-protagonist-name-migration-report.md"
EXTENSIONS = {".md", ".yml", ".yaml", ".txt"}
SKIP_PREFIXES = (
    ".git/",
    "docs/logs/deviations/",
    "docs/logs/migrations/",
)
SKIP_FILES = {
    "scripts/migrate_protagonist_name.py",
    ".github/workflows/protagonist-name-migration.yml",
}
HISTORY_MARKERS = (
    "→",
    "이전 작업명",
    "옛 작업명",
    "구 작업명",
    "변경 전",
    "superseded",
    "마이그레이션",
    "name migration",
)


@dataclass
class Change:
    path: str
    full_name_count: int
    short_name_count: int
    preserved_history_lines: int


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def should_scan(path: Path) -> bool:
    rel = relative(path)
    if path.suffix.lower() not in EXTENSIONS:
        return False
    if rel in SKIP_FILES:
        return False
    return not any(rel.startswith(prefix) for prefix in SKIP_PREFIXES)


def preserve_history_line(line: str) -> bool:
    if "서이안" not in line and "이안" not in line and "CHR-IAN-001" not in line:
        return False
    return any(marker.lower() in line.lower() for marker in HISTORY_MARKERS)


def migrate_text(text: str) -> tuple[str, int, int, int]:
    output: list[str] = []
    full_count = 0
    short_count = 0
    preserved = 0

    for line in text.splitlines(keepends=True):
        if preserve_history_line(line):
            preserved += 1
            output.append(line)
            continue

        full_count += line.count("서이안")
        short_count += line.count("이안") - line.count("서이안")
        line = line.replace("서이안", "서하진")
        line = line.replace("이안", "하진")
        line = line.replace("CHR-IAN-001", "CHR-HAJIN-001")
        output.append(line)

    return "".join(output), full_count, short_count, preserved


def active_old_name_hits() -> list[str]:
    hits: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or not should_scan(path):
            continue
        text = path.read_text(encoding="utf-8")
        for number, line in enumerate(text.splitlines(), start=1):
            if preserve_history_line(line):
                continue
            if "서이안" in line or "이안" in line or "CHR-IAN-001" in line:
                hits.append(f"{relative(path)}:{number}: {line.strip()}")
    return hits


def write_report(changes: list[Change], remaining: list[str]) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    full_total = sum(item.full_name_count for item in changes)
    short_total = sum(item.short_name_count for item in changes)
    preserved_total = sum(item.preserved_history_lines for item in changes)

    lines = [
        "---",
        "status: completed",
        "issue: 94",
        "accountable: A00",
        "responsible: [P02, N16, P09]",
        "challenged_by: [A13]",
        "canon: false",
        "---",
        "# 주인공 서이안→서하진 이름 마이그레이션 보고서",
        "",
        f"실행일: {date.today().isoformat()}",
        "",
        "## 결과",
        "",
        f"- 변경 파일: {len(changes)}",
        f"- 전체 이름 변경: {full_total}",
        f"- 단독 호칭 변경: {short_total}",
        f"- 변경 이력으로 보존한 줄: {preserved_total}",
        f"- 활성 옛 이름 잔재: {len(remaining)}",
        "",
        "## 변경 파일",
        "",
    ]
    if changes:
        for item in changes:
            lines.append(
                f"- `{item.path}` — 서이안 {item.full_name_count}, 이안 {item.short_name_count}, 역사 보존 {item.preserved_history_lines}"
            )
    else:
        lines.append("- 없음 — 이미 마이그레이션 완료 상태")

    lines.extend(["", "## 활성 잔재", ""])
    if remaining:
        lines.extend(f"- `{hit}`" for hit in remaining)
    else:
        lines.append("- 없음")

    lines.extend(
        [
            "",
            "## 보존 정책",
            "",
            "- `서이안→서하진`, `이전 작업명`, `superseded`, `마이그레이션` 등 변경 이력을 설명하는 줄은 보존한다.",
            "- 최신 원고·설정집·설계도에서 사용되는 이름과 호칭만 변경한다.",
            "- 사건·성격·관계·복선·성별·가족 구조는 이 스크립트가 변경하지 않는다.",
            "",
        ]
    )
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    changes: list[Change] = []

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or not should_scan(path):
            continue
        original = path.read_text(encoding="utf-8")
        migrated, full_count, short_count, preserved = migrate_text(original)
        if migrated != original:
            path.write_text(migrated, encoding="utf-8")
            changes.append(Change(relative(path), full_count, short_count, preserved))

    remaining = active_old_name_hits()
    write_report(changes, remaining)

    if remaining:
        print("Active old-name references remain:")
        print("\n".join(remaining))
        return 1

    print(f"Migrated {len(changes)} files. Report: {relative(REPORT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
