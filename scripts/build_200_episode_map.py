#!/usr/bin/env python3
"""Generate the deterministic 200-episode serialization ledger.

Narrative chapters and scene cards remain the source of truth. This script only
maps them to serial-release episode numbers; it does not invent or expand story.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Installment:
    number: int
    titles: tuple[str, ...]
    merged_chapters: frozenset[int]


INSTALLMENTS: tuple[Installment, ...] = (
    Installment(1, (
        "첫 어긋남", "집으로 가져온 빈칸", "늦어진 신고", "관찰의 조건",
        "가장 짧은 길의 거부", "닫힌 길이 옮긴 것", "움직이는 가족군",
        "비가 먼저 닫는 길", "누구의 기록인가", "취소할 수 없는 공사",
        "철수", "여러 길을 준비하는 사람들", "거부가 남긴 정보",
        "선택된 경로", "달라진 통학로",
    ), frozenset({2, 15})),
    Installment(2, (
        "움직이는 아침 지도", "세 길과 하나의 봉화", "닳은 장비가 알려 주는 것",
        "잘한 교대", "보호실의 성공", "학교가 자랑하는 것", "두 번째 호출",
        "옮겨간 균열", "같은 팀의 다른 답", "경고를 이용하는 법",
        "취소할 수 없는 하루", "첫 철수 기록자", "학교가 사랑받는 날",
        "열린 봉화", "멈춤종", "남아 있는 학교",
    ), frozenset({1, 4, 8, 14})),
    Installment(3, (
        "같은 나라의 다른 시간표", "지도 밖으로 갈라진 길", "고립을 줄이는 직선",
        "물이 아니라 경계", "먼 길이 빠른 날", "빈칸은 모르는 곳이 아니다",
        "길이 열린 오후", "성공한 지도", "하루 먼저 움직인 물",
        "줄어든 부담의 행선지", "공통이라는 말의 힘", "돌려줄 수 없는 물건",
        "다시 놓는 표식", "다음 계절에 닫히는 길", "합쳐지지 않은 지도",
    ), frozenset({1, 5, 12, 13})),
    Installment(4, (
        "출국 전에 정해지는 것", "물 위의 교차로", "빨라진 연락",
        "대답하지 않는 배열", "하나가 된 위험", "자동으로 움직이는 절차",
        "닫히는 운영 창", "말하지 않는 것도 결정이다", "먼저 보이는 기록",
        "보내야 하는 것만", "성공한 수정", "남아 버린 위험",
        "화면에서 사라지는 권한", "가장 짧은 경보",
        "문을 여는 사람이 아닌 사람", "번역 뒤에 남은 서명",
    ), frozenset({1, 3, 13, 16})),
    Installment(5, (
        "돌아온 사람의 자리", "닫힌 환승선", "소리가 사라진 구간",
        "찍으러 오는 사람들", "학교 안의 빈칸", "다른 곳으로 간 부담",
        "지운 사람을 찾는 도구가 아니다", "함께 사라진 책임",
        "공개하면 고칠 수 있다", "퍼지는 지도", "누구의 사진인가",
        "위험을 아는 권리", "같은 편이 아닌 협력", "보이는 것과 남겨야 할 것",
        "열리는 구간, 닫히는 위치", "학교를 지키는 방식", "두 개의 기록",
    ), frozenset({1, 7, 12, 13, 17})),
    Installment(6, (
        "졸업 전의 선택들", "우선 연결자", "서로 기다리는 경보", "옮겨진 부담",
        "더 많이 보는 화면", "화면 아래의 균열", "성공을 설명하는 사람",
        "하나의 순서", "완전한 성공", "사건 뒤에 남은 장소",
        "안정 자원이라는 이름", "같은 성공을 다르게 보는 사람들", "연장할 이유",
        "한 번만 더", "나눈 화면", "느린 구조", "성공을 남기는 법",
        "만료 뒤의 책임",
    ), frozenset({1, 5, 10, 12, 17, 18})),
    Installment(7, (
        "마지막 학기의 첫날", "네 가지 끝내는 법", "한 번만 쓰는 권한",
        "취소되는 것들", "같은 시간, 다른 이유", "가장 빠른 방법", "성공한 연장",
        "모두가 기다리는 사람", "먼저 고를 수 없는 것", "마지막 연결점",
        "느리게 가는 길", "지연이라는 선택", "하나의 성공이 없는 화면",
        "남아 달라는 말", "돌아오지 않을 권한", "나누는 일의 시작",
        "명령 없는 임무", "마지막으로 여는 것", "공개되지 않은 진실", "다음 통학",
    ), frozenset({1, 2, 3, 6, 10, 13, 18, 19, 20})),
)


def build_markdown() -> str:
    episode = 1
    output: list[str] = [
        "# 200화 연재 상세 번호표",
        "",
        "두 장면 카드를 가진 장은 기본적으로 카드별 1화로 나눈다. "
        "`merged_chapters`에 든 장만 두 카드를 1화로 결합한다.",
        "",
    ]

    for installment in INSTALLMENTS:
        start_episode = episode
        rows: list[str] = []
        for chapter, title in enumerate(installment.titles, start=1):
            count = 1 if chapter in installment.merged_chapters else 2
            end_episode = episode + count - 1
            episode_range = str(episode) if count == 1 else f"{episode}~{end_episode}"
            split = "결합 1화" if count == 1 else "카드별 2화"
            rows.append(f"| {chapter} | {title} | {episode_range} | {split} |")
            episode = end_episode + 1

        output.extend([
            f"## 부제작 {installment.number} — {start_episode}~{episode - 1}화",
            "",
            "| 장 | 작업 제목 | 연재 화 | 방식 |",
            "|---:|---|---:|---|",
            *rows,
            "",
        ])

    total = episode - 1
    if total != 200:
        raise RuntimeError(f"Expected exactly 200 episodes, got {total}")

    output.extend(["## 검증", "", f"- 총 연재 화: **{total}**", "- 새 사건 추가: 0", ""])
    return "\n".join(output)


def main() -> None:
    destination = Path("story/00-series/two-hundred-episode-ledger-generated.md")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(build_markdown(), encoding="utf-8")
    print(destination)


if __name__ == "__main__":
    main()
