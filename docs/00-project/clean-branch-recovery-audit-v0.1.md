---
status: recovery-audit-complete
branch: canon/world-bible-blueprint-clean
archive_branch: archive/full-saga-draft-unapproved
reset: false
manuscript_generation: prohibited
---
# 설정집·설계도 정리 브랜치 복구 감사 v0.1

## 1. 결론

이 작업은 프로젝트 초기화가 아니다.

- 기존 전체 작업은 `archive/full-saga-draft-unapproved`에 그대로 보존돼 있다.
- 정리 브랜치는 아카이브 브랜치의 최신 상태에서 출발했다.
- 세계관·설정집·인물·기관·학교·생태·지역·사가·장면 설계 파일은 유지했다.
- 실제 소설 원고와 원고 완료를 전제로 한 파생 문서만 정리 브랜치에서 제거했다.
- `main`과 기존 PR #1은 변경하거나 병합하지 않았다.

## 2. 보존된 핵심 자산

### 세계관

- `world/00-core/**`
- `world/10-regions/**`
- `world/10-routes/**`
- `world/20-ecology/**`
- `world/20-systems/**`
- `world/30-history/**`
- `world/30-korea/**`
- `world/40-ecology/**`
- `world/40-institutions/**`
- `world/50-artifacts/**`
- `world/60-companion/**`

### 작품 설계

- `story/00-series/**`
- `story/10-secrets/**`
- `story/20-characters/**`
- `story/30-books/**`
- 원고 전용 회수표를 제외한 `story/40-ledgers/**`

### 조사·검증

- `research/**`
- 원고 감사 영역을 제외한 `reviews/**`
- 원고·초고 독자 테스트를 제외한 `tests/**`
- `agents/**`
- `templates/**`

## 3. 격리한 영역

- `manuscript/**`
- `reviews/manuscript/**`
- `tests/manuscript/**`
- 초고를 읽는 전제의 `tests/readers/**` 일부
- 원고↔설정집 역감사
- 원고 단계 승인 문서
- 부제작별 초고 완료 패키지
- 전체 사가 초고 완료 패키지
- 원고 완성 하네스·원고 운영 계약
- 원고 기반 제작 로드맵
- 원고용 심기·진전·회수표

위 자료는 삭제된 것이 아니라 아카이브 브랜치에 남아 있다.

## 4. 교정한 상태

| 항목 | 과거 잘못된 상태 | 정리 브랜치 상태 |
|---|---|---|
| `이어서진행` | 원고 단계 승인으로 해석 | 설정집·설계도 자동 진행만 허용 |
| 7부제 | 작가 확정 기준선 | candidate structural baseline |
| 117장 | 완성 분량 | candidate design count |
| 234장면 | 원고 장면 확정 | candidate scene-function count |
| 200화 | 제작 완료 구조 | candidate production map |
| 서하진·유나 등 | 사실상 고정 | working candidate |
| 태국·수문·검역 | 완성 원고 사건 | 지역·사건 설계 후보 |
| 전체 초고 | human-review-ready | 정리 브랜치 범위 밖 |

## 5. 활성 source-of-truth

1. `README.md`
2. `docs/00-project/world-bible-clean-branch-status-v0.1.md`
3. `docs/decisions/clean-branch-candidate-baseline-v0.1.md`
4. `docs/decisions/world-bible-status-inventory-v0.2.md`
5. `docs/00-project/full-seven-installment-design-package-index-v0.1.md`
6. `memory/project-context.md`
7. `CLAUDE.md`

`CLAUDE.md`의 자동 완주 규칙은 위 교정 기준선과 함께 읽으며, 원고 작성으로 확장할 수 없다.

## 6. 현재 남은 위험

- 일부 오래된 문서가 `author-approved`, `draft`, `human-review-ready`를 계속 사용할 수 있음
- 삭제된 `manuscript/**` 경로를 가리키는 링크가 남아 있을 수 있음
- 원고 작성 뒤 보강된 설정이 원래 설계와 뒤섞였을 수 있음
- 7부제·117장·200화가 사용자의 실제 목표에 최적인지는 아직 재평가되지 않음
- 주인공·학교·경기·수집 구조의 재미와 독창성은 별도 감사가 필요함

## 7. 다음 자동 작업

1. 활성 핵심 문서의 끊어진 원고 링크 제거
2. 오래된 완료·승인 상태 표기 교정
3. 7부제·117장·200화 적합성 재평가
4. 해리포터 참고 기능과 독자적 변형 거리 감사
5. 세계관·인물·학교·생태·지역·능력 설정의 누락·중복·모순 보수
6. 최종 작가 검토용 설정집 패키지 작성

## 8. 안전 규칙

- 실제 소설 문장을 쓰지 않는다.
- 원고 승인 문서를 자동 생성하지 않는다.
- `main`에 병합하지 않는다.
- 기존 PR #1을 Ready로 바꾸거나 병합하지 않는다.
- 아카이브 브랜치를 삭제하거나 강제 이동하지 않는다.
- 후보를 final canon으로 승격하지 않는다.
