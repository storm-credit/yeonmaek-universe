# CLAUDE.md

## 프로젝트 목적

이 저장소는 《겹길의 아이들》의 세계관·설정집·이야기 설계도·원고·검수 기록을 **정본 우선 계층형 스토리 오케스트라**로 관리한다.

## 정본 우선순위

1. 현재 사용자가 직접 확정한 내용
2. 사용자가 이후 명시적으로 승인한 결정
3. `canon/CANON_CONSTITUTION.md`
4. `canon/CANON_AMENDMENTS.md`와 `canon/DECISION_LOG.md`
5. `ledgers/` 상태 장부
6. `world/`, `characters/` 분야별 설정집
7. `story/` 전체 이야기 설계도
8. Context Pack과 작법 배치
9. `manuscript/` 원고
10. 폐기·참고 자료

`CLAUDE.md`, `AGENTS.md`, 스킬, 프롬프트, Context Pack은 상위 정본을 변경할 수 없다.

## 현재 원고 잠금 상태

**LOCKED — 신규 원고·대사·장면 본문 작성 금지.**

- 기존 제1부 1~11장과 검수·Act 감사는 보존한다.
- 사용자가 다시 명시적으로 집필을 허가하고 대상 단위 S0=0, S1=0, Context Pack이 준비될 때까지 후속 원고를 작성하지 않는다.
- 분량 정책은 최소 기준만 두고 상한은 두지 않는다: `writing/00-system/chapter-length-policy-v0.1.md`.

## 공식 이야기 계층

`Series → Grand Act → Volume Act → Arc → Subact → Episode → Scene`

기존 5부·15 Act·45 Subact·90장은 보존한다. 상세 매핑은 `story/00-series/OFFICIAL_HIERARCHY_MAPPING.md`를 따른다.

각 계층 필수 필드:

`Promise / Goal / Opposition / Choice / Cost / Revelation / Reward / Loss / State Change / Next Cause / Anti-Repeat`

Subact는 국소 문제를 해결하거나 명확히 실패해야 하며, 그 비용·손실·실패가 다음 Subact의 직접 원인이어야 한다.

## 시작 전 필수 정본 확인

1. `canon/CANON_CONSTITUTION.md`
2. `canon/CANON_AMENDMENTS.md`
3. `canon/DECISION_LOG.md`
4. `docs/00-project/current-work-status.md`
5. `manuscript/00-status/manuscript-progress.md`
6. 관련 `ledgers/`
7. 작업 범위의 `world/`, `characters/`, `story/`, `writing/`, `reviews/`

기억이나 이전 대화 요약만으로 작업하지 않는다.

## 오케스트레이션 진입점

- 역할: `orchestration/AGENT_ROLES.md`
- 강제 순서: `orchestration/WORKFLOW_HARNESS.md`
- 완료 판정: `orchestration/COMPLETION_GATES.md`
- 작법 선택: `orchestration/STORYCRAFT_SELECTION.md`
- Context Pack: `orchestration/CONTEXT_PACK_PROTOCOL.md`

실제 다중 에이전트 실행이 가능하면 역할을 분리한다. 불가능하면 단일 총괄 모델이 역할을 순차 적용하고 교차 검증한다. 실행하지 않은 에이전트를 실행했다고 보고하지 않는다.

## Context Pack 의무

구조·회차·원고 작업은 대상 계층 CP 없이 시작하지 않는다. CP는 정본이 아니며 모든 주장에 원본 경로를 기록한다. 설정이 부족하면 원고에서 만들지 말고 해당 전문 분야로 되돌아간다.

## 완료 게이트

- `orchestration/COMPLETION_GATES.md`의 분야별 게이트 통과
- S0=0, S1=0
- 관련 장부와 상태 문서 갱신
- 파일·참조·이름 변경 검증
- 최신 `main` 커밋 SHA 확인

미완료를 완료로 보고하지 않는다.

## 변경·충돌 처리

- 상위 정본과 충돌하면 하위 산출물을 중지한다.
- 승인 필요 변경은 자동 확정하지 않는다.
- 변경은 Amendments·Decision Log·관련 설정·장부·상태 문서에 함께 반영한다.
- 파일명과 내부 구조 충돌은 내용 손실 없이 교정하고 참조를 전부 수정한다.
- 출처 불명·다른 프로젝트 오염은 `Q`/`X`로 격리한다.

## GitHub main 반영 규칙

- 운영 브랜치는 `main`이다.
- 완료 전 파일 생성·수정·삭제·이름 변경 결과를 검증한다.
- 기존 원고와 감사는 명시적 승인 없이 삭제하지 않는다.
- 마지막 단계에서 `main`이 생성 커밋을 가리키는지 확인한다.

## 세부 문서 링크

### 집필·문체
- `writing/00-system/writing-style-orchestration-v1.0.md`
- `writing/00-system/craft-coverage-map-v0.1.md`
- `writing/10-style/voice-and-prose-guide-v1.0.md`
- `writing/20-dialogue/character-voice-matrix-v1.0.md`
- `writing/30-workflow/chapter-drafting-and-revision-workflow-v1.0.md`
- `writing/50-craft/`
- `writing/60-recitation/read-aloud-line-criteria-v0.1.md`
- `writing/00-system/legacy-claude-rules-preservation-v1.0.md`

### 구조·정본·상태
- `story/00-series/OFFICIAL_HIERARCHY_MAPPING.md`
- `templates/STORY_HIERARCHY_TEMPLATE.md`
- `templates/CONTEXT_PACK_TEMPLATE.md`
- `ledgers/`
- `reviews/design/canon-orchestration-migration-audit-v1.0.md`
- `reviews/design/world-setting-completion-gap-audit-v1.0.md`
