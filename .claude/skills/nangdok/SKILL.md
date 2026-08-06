---
name: nangdok
description: Use when the user asks to 낭독-check a manuscript chapter (read it line by line aloud-style) or says /nangdok. Applies the project's read-aloud line criteria to a chapter file and reports per-line verdicts with fix suggestions.
---

# 낭독 검사 스킬

원고 장을 한 줄씩 "소리 내어 읽는" 기준으로 검사한다.

## 입력

- 인자로 장 번호나 파일 경로를 받는다 (예: `/nangdok 7`, `/nangdok manuscript/part1/chapter07-missing-signpost-v0.1.md`).
- 인자가 없으면 `manuscript/00-status/manuscript-progress.md`에서 가장 최근 완료 장을 대상으로 한다.

## 절차

1. `writing/60-recitation/read-aloud-line-criteria-v0.1.md`를 읽는다. 이 문서가 판정 기준의 정본이다.
2. `writing/10-style/voice-and-prose-guide-v1.0.md`와 `writing/20-dialogue/character-voice-matrix-v1.0.md`를 참조 기준으로 함께 읽는다.
3. 대상 장 파일을 읽고, 빈 줄을 제외한 모든 줄(문장/대사)을 위에서부터 순서대로 검사한다.
4. 각 줄에 기준 문서의 A(호흡)·B(한국어 자연성)·C(소리)·D(톤·정보)·E(대사) 항목을 적용해 `통과 / 제안 / 질문` 중 하나로 판정한다.
5. `제안` 판정에는 반드시 사유 태그(A1~E3)와 대안 문장을 붙인다. 대안은 원문의 의미·정보량·복선을 보존해야 한다.
6. `질문` 판정은 의도적 위반 가능성이 있는 경우다. 고치지 말고 작가에게 넘긴다.

## 보고 형식

기준 문서의 「검사 후 보고 형식」을 따른다:

1. 낭독 소요 추정과 호흡 곡선 요약(감속·가속 구간)
2. 판정 통계
3. 제안 목록: `줄 번호 | 원문 | 태그 | 대안`
4. 질문 목록

## 수정 적용

- 기본은 보고만 한다. 원고를 수정하지 않는다.
- 작가가 "적용해" 또는 자동 진행을 지시한 경우에만 `제안` 항목을 원고에 반영하고, 반영 내역을 장별 검수 문서에 `낭독 검수` 절로 추가한 뒤 커밋한다.
- `질문` 항목은 자동 진행 중에도 적용하지 않는다.

## 금지

- 문체 기준(담담한 관찰, 감정의 신체화, 경이의 평범한 어휘)을 낭독 편의를 이유로 무너뜨리지 않는다.
- 의도된 짧은 문장 연타(위기 가속 구간)를 획일적으로 늘이지 않는다.
- 대사의 인물 음성을 표준어 문어체로 "교정"하지 않는다.
