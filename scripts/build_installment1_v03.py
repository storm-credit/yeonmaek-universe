#!/usr/bin/env python3
"""Build the installment 1 v0.3 review copy from preserved chapter files.

The builder applies the exact replacement manifest and fails safely when an expected
source sentence is missing or appears more than once. It never modifies source drafts.

Usage:
    python scripts/build_installment1_v03.py
    python scripts/build_installment1_v03.py --output build/installment-01-v0.3
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

DEFAULT_MANIFEST = Path("manuscript/installment-01/v0.3-patch-manifest.json")
DEFAULT_OUTPUT = Path("build/manuscript/installment-01-v0.3")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--allow-existing",
        action="store_true",
        help="Replace an existing build directory. Source drafts remain untouched.",
    )
    return parser.parse_args()


def apply_replacements(text: str, replacements: list[dict[str, object]], chapter: int) -> tuple[str, list[str]]:
    applied: list[str] = []
    result = text
    for replacement in replacements:
        if int(replacement["chapter"]) != chapter:
            continue
        patch_id = str(replacement["id"])
        old = str(replacement["old"])
        new = str(replacement["new"])
        count = result.count(old)
        if count != 1:
            raise ValueError(
                f"{patch_id} chapter {chapter}: expected exactly one source match, found {count}"
            )
        if new in result:
            raise ValueError(f"{patch_id} chapter {chapter}: replacement text already exists")
        result = result.replace(old, new, 1)
        applied.append(patch_id)
    return result, applied


def main() -> int:
    args = parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    output: Path = args.output

    if output.exists():
        if not args.allow_existing:
            raise FileExistsError(
                f"Output directory already exists: {output}. Use --allow-existing to replace it."
            )
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=False)

    replacements = list(manifest["replacements"])
    all_applied: list[str] = []
    built_files: list[str] = []

    for chapter_entry in manifest["chapters"]:
        chapter = int(chapter_entry["chapter"])
        source = Path(str(chapter_entry["source"]))
        if not source.exists():
            raise FileNotFoundError(f"Missing source chapter: {source}")
        text = source.read_text(encoding="utf-8")
        patched, applied = apply_replacements(text, replacements, chapter)
        target = output / f"chapter-{chapter:02d}.md"
        target.write_text(patched, encoding="utf-8")
        all_applied.extend(applied)
        built_files.append(str(target))

    expected_ids = [str(item["id"]) for item in replacements]
    if sorted(all_applied) != sorted(expected_ids):
        missing = sorted(set(expected_ids) - set(all_applied))
        extra = sorted(set(all_applied) - set(expected_ids))
        raise RuntimeError(f"Patch accounting mismatch. missing={missing}, extra={extra}")

    build_meta = {
        "version": manifest["version"],
        "base": manifest["base"],
        "chapters": len(built_files),
        "patches": all_applied,
        "files": built_files,
    }
    (output / "build-manifest.json").write_text(
        json.dumps(build_meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(f"Built {len(built_files)} chapters with {len(all_applied)} patches at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
