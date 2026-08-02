#!/usr/bin/env python3
"""Audit Korean manuscript files for mechanical prose-pattern risks.

This script does not score literary quality. It surfaces locations for human review:
- sentence-length distribution and very long sentences
- short one-line paragraph streaks
- repeated sentence endings
- repeated sentence openings and selected theme words
- dialogue/narration paragraph balance

Usage:
    python scripts/audit_manuscript_style.py manuscript/installment-01/draft/chapter-*.md
    python scripts/audit_manuscript_style.py --output reports/style-audit.md FILE...

Pass only the latest manuscript files. Older versioned drafts should not be mixed with
current files unless comparing versions intentionally.
"""

from __future__ import annotations

import argparse
import collections
import re
import statistics
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?。！？…])\s+|(?<=다\.)\s+|(?<=요\.)\s+")
WORD_RE = re.compile(r"[가-힣A-Za-z0-9]+")
MARKDOWN_PREFIX_RE = re.compile(r"^(#{1,6}\s+|[-*+]\s+|\d+\.\s+|>\s*)")
DIALOGUE_OPENERS = ('"', "'", "“", "‘", "「", "『")
THEME_WORDS = (
    "기록",
    "모르",
    "미확인",
    "확정",
    "가능성",
    "대답하지",
    "그 순간",
    "놀랍게도",
    "사실은",
)


@dataclass(frozen=True)
class Paragraph:
    file: Path
    line: int
    text: str


@dataclass(frozen=True)
class Sentence:
    file: Path
    line: int
    text: str


def strip_frontmatter(lines: list[str]) -> list[tuple[int, str]]:
    """Return numbered lines with a leading YAML frontmatter block removed."""
    numbered = list(enumerate(lines, start=1))
    if not numbered or numbered[0][1].strip() != "---":
        return numbered
    for index, (_, line) in enumerate(numbered[1:], start=1):
        if line.strip() == "---":
            return numbered[index + 1 :]
    return numbered


def load_paragraphs(path: Path) -> list[Paragraph]:
    raw_lines = path.read_text(encoding="utf-8").splitlines()
    lines = strip_frontmatter(raw_lines)
    paragraphs: list[Paragraph] = []
    buffer: list[str] = []
    start_line = 0

    def flush() -> None:
        nonlocal buffer, start_line
        if not buffer:
            return
        text = " ".join(part.strip() for part in buffer if part.strip()).strip()
        buffer = []
        if not text:
            return
        if text.startswith("```") or text.startswith("|"):
            return
        text = MARKDOWN_PREFIX_RE.sub("", text).strip()
        if text:
            paragraphs.append(Paragraph(path, start_line, text))

    in_code_block = False
    for line_number, line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            flush()
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if not stripped:
            flush()
            continue
        if stripped.startswith("#"):
            flush()
            continue
        if not buffer:
            start_line = line_number
        buffer.append(stripped)
    flush()
    return paragraphs


def split_sentences(paragraph: Paragraph) -> list[Sentence]:
    parts = [part.strip() for part in SENTENCE_SPLIT_RE.split(paragraph.text) if part.strip()]
    if not parts:
        return []
    return [Sentence(paragraph.file, paragraph.line, part) for part in parts]


def normalized_length(text: str) -> int:
    return len(re.sub(r"\s+", "", text))


def sentence_ending(text: str, width: int = 6) -> str:
    cleaned = re.sub(r"[\s\"'“”‘’「」『』()\[\]{}.,!?。！？…]+$", "", text)
    return cleaned[-width:] if cleaned else ""


def sentence_opening(text: str, words: int = 2) -> str:
    tokens = WORD_RE.findall(text)
    return " ".join(tokens[:words])


def find_short_paragraph_streaks(
    paragraphs: list[Paragraph], max_chars: int, min_streak: int
) -> list[list[Paragraph]]:
    streaks: list[list[Paragraph]] = []
    current: list[Paragraph] = []
    previous_file: Path | None = None
    previous_line = -10

    for paragraph in paragraphs:
        is_short = normalized_length(paragraph.text) <= max_chars
        is_close = paragraph.file == previous_file and paragraph.line <= previous_line + 3
        if is_short and (not current or is_close):
            current.append(paragraph)
        else:
            if len(current) >= min_streak:
                streaks.append(current)
            current = [paragraph] if is_short else []
        previous_file = paragraph.file
        previous_line = paragraph.line
    if len(current) >= min_streak:
        streaks.append(current)
    return streaks


def markdown_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def build_report(
    files: list[Path],
    long_sentence: int,
    short_paragraph: int,
    short_streak: int,
    top_n: int,
) -> str:
    paragraphs: list[Paragraph] = []
    missing: list[Path] = []
    for path in files:
        if not path.exists():
            missing.append(path)
            continue
        paragraphs.extend(load_paragraphs(path))

    sentences = [sentence for paragraph in paragraphs for sentence in split_sentences(paragraph)]
    lengths = [normalized_length(sentence.text) for sentence in sentences]
    long_sentences = [sentence for sentence in sentences if normalized_length(sentence.text) >= long_sentence]
    short_streaks = find_short_paragraph_streaks(paragraphs, short_paragraph, short_streak)

    ending_counter = collections.Counter(
        ending for sentence in sentences if (ending := sentence_ending(sentence.text))
    )
    opening_counter = collections.Counter(
        opening for sentence in sentences if (opening := sentence_opening(sentence.text))
    )
    theme_counts = {
        word: sum(paragraph.text.count(word) for paragraph in paragraphs) for word in THEME_WORDS
    }
    dialogue_count = sum(paragraph.text.startswith(DIALOGUE_OPENERS) for paragraph in paragraphs)

    report: list[str] = [
        "# 원고 문장·문단 기계적 패턴 감사",
        "",
        "> 이 보고서는 문학적 품질 점수가 아니다. 반복·과분절·장문 혼탁 후보를 사람이 다시 읽기 위한 위치표다.",
        "",
        "## 입력",
        "",
        f"- 요청 파일: {len(files)}",
        f"- 읽은 파일: {len(files) - len(missing)}",
        f"- 누락 파일: {len(missing)}",
        f"- 분석 문단: {len(paragraphs)}",
        f"- 분석 문장: {len(sentences)}",
        "",
    ]

    if missing:
        report.extend(["### 누락", ""] + [f"- `{path}`" for path in missing] + [""])

    if lengths:
        sorted_lengths = sorted(lengths)
        p90_index = min(len(sorted_lengths) - 1, int(len(sorted_lengths) * 0.9))
        report.extend(
            [
                "## 문장 길이",
                "",
                f"- 평균: {statistics.mean(lengths):.1f}자(공백 제외)",
                f"- 중앙값: {statistics.median(lengths):.1f}자",
                f"- 90백분위: {sorted_lengths[p90_index]}자",
                f"- 최장: {max(lengths)}자",
                f"- {long_sentence}자 이상 후보: {len(long_sentences)}",
                "",
            ]
        )

    report.extend(["## 긴 문장 후보", "", "| 파일:줄 | 길이 | 문장 |", "|---|---:|---|"])
    for sentence in sorted(long_sentences, key=lambda item: normalized_length(item.text), reverse=True)[:top_n]:
        preview = sentence.text[:180] + ("…" if len(sentence.text) > 180 else "")
        report.append(
            f"| `{sentence.file}:{sentence.line}` | {normalized_length(sentence.text)} | {markdown_escape(preview)} |"
        )
    if not long_sentences:
        report.append("| - | - | 없음 |")

    report.extend(["", "## 짧은 한 줄 문단 연속 후보", ""])
    if short_streaks:
        for streak in short_streaks[:top_n]:
            report.append(
                f"- `{streak[0].file}:{streak[0].line}`부터 {len(streak)}개: "
                + " / ".join(markdown_escape(item.text[:45]) for item in streak[:5])
            )
    else:
        report.append("- 없음")

    report.extend(["", "## 반복 종결 후보", "", "| 끝부분 | 횟수 |", "|---|---:|"])
    for ending, count in ending_counter.most_common(top_n):
        if count >= 3:
            report.append(f"| `{markdown_escape(ending)}` | {count} |")

    report.extend(["", "## 반복 시작 후보", "", "| 시작 | 횟수 |", "|---|---:|"])
    for opening, count in opening_counter.most_common(top_n):
        if count >= 3:
            report.append(f"| `{markdown_escape(opening)}` | {count} |")

    report.extend(["", "## 주제어·상투 전환어", "", "| 표현 | 횟수 |", "|---|---:|"])
    for word, count in theme_counts.items():
        report.append(f"| `{word}` | {count} |")

    dialogue_ratio = dialogue_count / len(paragraphs) * 100 if paragraphs else 0.0
    report.extend(
        [
            "",
            "## 문단 유형 참고",
            "",
            f"- 대사로 시작하는 문단: {dialogue_count}/{len(paragraphs)} ({dialogue_ratio:.1f}%)",
            "- 적정 비율 판정은 장르·장면별 인간 검토가 필요하다.",
            "",
            "## 해석 규칙",
            "",
            "- 긴 문장 자체는 오류가 아니다. 주체·시간·공간 방향을 잃을 때만 수정한다.",
            "- 짧은 문단 자체는 오류가 아니다. 충격·판단·전환 의도가 없는데 기계적으로 연속될 때 수정한다.",
            "- 핵심 주제어는 동의어로 무조건 치환하지 않는다. 같은 기능을 반복 설명하는지 확인한다.",
            "- 수치만으로 원고를 자동 변경하지 않는다.",
            "",
        ]
    )
    return "\n".join(report)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="Latest manuscript Markdown files")
    parser.add_argument("--output", type=Path, help="Write Markdown report to this path")
    parser.add_argument("--long-sentence", type=int, default=95, help="Long sentence threshold")
    parser.add_argument("--short-paragraph", type=int, default=28, help="Short paragraph threshold")
    parser.add_argument("--short-streak", type=int, default=5, help="Consecutive short paragraph threshold")
    parser.add_argument("--top", type=int, default=30, help="Maximum candidates per section")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(
        files=args.files,
        long_sentence=args.long_sentence,
        short_paragraph=args.short_paragraph,
        short_streak=args.short_streak,
        top_n=args.top,
    )
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(args.output)
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
