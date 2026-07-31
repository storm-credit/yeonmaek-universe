---
status: complete
issues: [63, 81]
scope: source-of-truth+legacy+empty-placeholders+terminology
method: c0-index+decision-inventory+pr-file-stats+targeted-file-check
---
# 세계 설정집 근거·중복·빈 자리표시자 감사 v0.1

## 1. 판정

- 핵심 세계관마다 단일 진입 근거 문서가 지정됐다.
- 과거 5권 구조·옛 제목·구판 질문은 삭제하지 않고 superseded/deprecated로 보존한다.
- 초기 도구 오류로 생성된 0바이트 옵션·레드팀 자리표시자가 존재한다.
- 0바이트 파일은 내용이 없으므로 정본 근거로 사용할 수 없으며 C0 색인에서 제외했다.
- 최신 실질 레드팀·테스트 문서는 `reviews/world-bible/`, `tests/world-bible/`를 우선한다.
- 첫 부제작 원고는 최신본 색인에 지정된 버전만 사용한다.

## 2. 단일 진입 근거

| 영역 | 단일 진입 문서 |
|---|---|
| C0 전체 | `world/00-core/c0-world-bible-index-v0.1.md` |
| C0 핵심 요약 | `world/00-core/c0-world-bible-core-compendium-v0.1.md` |
| 상태·후보·폐기 | `docs/decisions/world-bible-status-inventory-v0.1.md` |
| 열린 질문 | `memory/open-questions-v0.2.md` |
| 세계 규칙 | `world/00-core/world-rules-failure-recovery-ledger-v0.1.md` |
| 학교·생활 | `world/40-institutions/korea-school-life-operations-bible-v0.1.md` |
| 역사·기관·지식 | `world/30-history/history-agreements-institutions-knowledge-boundary-v0.1.md` |
| 공통 데이터 스키마 | `world/00-core/world-bible-record-schema-v0.1.md` |
| 수집 카탈로그 | `world/60-companion/world-bible-collection-catalog-index-v0.1.md` |
| 부제작 2~7 | `story/30-books/installments-02-07-setting-bible-index-v0.1.md` |
| 첫 부제작 원고 | `manuscript/installment-01/README.md` |
| 첫 원고 역검증 | `reviews/world-bible/installment1-manuscript-world-bible-reverse-audit-v0.1.md` |
| 인간 검토 | `reviews/world-bible/human-expert-review-matrix-v0.1.md` |
| 원본성·맹점 | `reviews/world-bible/world-bible-originality-blindspot-collection-red-team-v0.1.md` |
| 독자용 샘플 | `publishing/samples/`의 2개 샘플 파일 |

## 3. 상태 우선순위

동일 개념이 여러 문서에 있을 때:

1. 작가 의도·CLAUDE 운영 계약
2. C0 통합 색인·최신 decision
3. 최신 상세 bible·catalog
4. 최신 테스트·레드팀
5. 연구·후보 4안
6. 과거 후보·구판 질문·빈 자리표시자

낮은 순위 문서가 높은 순위와 충돌하면 최신 문서를 사용한다. 과거 파일은 이력 보존용이다.

## 4. 명칭 정리

| 명칭 | 상태 | 사용 |
|---|---|---|
| 연맥 | 저장소·세계관 코드명 | 내부 경로·과거 문서, 독자 제목 아님 |
| 겹길 | 메인 작업 제목 preliminary-candidate | 원고·샘플 작업명 |
| 틈너머 | superseded working title | 신규 사용 금지 |
| 깊은결학교 | 학교 작업명 | canon·상표 아님 |
| 경계생태협력재단 | 재단 작업명 | canon·법적 명칭 아님 |
| 빈자리 도감 | 도감 작업명 | 제목·상표 검토 전 candidate |
| 길문전 | 경기 작업명 | 상세 규칙·브랜드 검토 전 candidate |
| 여울띠 | 한국 학교 외부명 | 자기명칭 아님 |
| 가족군 | 학생 임시 가설 | 공식 기록에서는 `현재 관측 이동군` |

## 5. 과거 구조 보존

### 전체 5권 핵심 완결형

- 상태: `reframing required / deprecated candidate`
- 금지: 메인 사가 전체를 5권으로 다시 해석
- 재사용: 발견·보호·번역·공개·공동관리 기능을 7부제에 분산

### 나라별 주인공 교체 지역 사이클

- 상태: 메인 사가에서는 rejected
- 재사용: 본편 완결 뒤 공유세계관 외전 슬롯

### 한 학년=한 부제작

- 상태: prohibited
- 사건·방학·계절·성장 기간에 따라 가변

## 6. 구판·대체 문서

| 파일·유형 | 상태 | 최신 대체 |
|---|---|---|
| `memory/open-questions.md` | superseded snapshot | `memory/open-questions-v0.2.md` |
| `series-length-architecture-options-v0.1.md`의 5권안 | reframing required | 7부제 사가 결정·색인 |
| 틈너머 명칭 사용 문서 | superseded terminology | 겹길 preliminary candidate |
| `book1` 용어가 남은 초기 문서 | legacy terminology | `installment1` 문서 우선 |
| 초기 worldbuilding readiness | historical gate | C0 색인·#62 완료 게이트 |
| 초기 companion framework | schema source | 실제 카탈로그·독자 샘플 우선 |

## 7. 빈 자리표시자 파일

PR 파일 통계와 대상 파일 확인에서 아래 종류의 0바이트 또는 실질 내용이 없는 자리표시자가 발견됐다.

### 레드팀 자리표시자

- `reviews/long-growth-main-saga-red-team-v0.1.md`
- `reviews/seven-installment-saga-map-red-team-v0.1.md`
- `reviews/seven-installment-loop-red-team-v0.1.md`
- `reviews/seven-installment-character-arc-red-team-v0.1.md`
- `reviews/protagonist-age-time-red-team-v0.1.md`
- `reviews/protagonist-final-cost-red-team-v0.1.md`
- `reviews/ontology-boundary-red-team-v0.1.md`
- `reviews/power-cost-failure-red-team-v0.1.md`
- `reviews/sentience-ecology-rights-red-team-v0.1.md`
- `reviews/secret-society-public-institutions-red-team-v0.1.md`
- `reviews/school-education-life-red-team-v0.1.md`
- `reviews/history-international-order-red-team-v0.1.md` 계열의 초기 자리
- `reviews/structural-conflict-engine-red-team-v0.1.md`
- `reviews/representative-sport-red-team-v0.1.md`
- `reviews/naming-gate-red-team-v0.1.md`
- `reviews/pre-manuscript-integrated-red-team-v0.1.md`
- `reviews/worldbuilding-readiness-red-team-v0.1.md`
- `reviews/worldbuilding-gates-cross-consistency-v0.1.md`
- `reviews/red-team-v0.1.md`

### 첫 부제작·지역 자리표시자

- `reviews/installment1-pressure-responsibility-red-team-v0.1.md`
- `reviews/installment1-capital-commute-zone-red-team-v0.1.md`의 초기 빈 자리 가능성은 최신 실질 파일을 확인해 사용
- `reviews/installment4-overseas-region-red-team-v0.1.md`
- `reviews/kr-installment3-domestic-region-red-team-v0.1.md`
- `reviews/korea-first-stage-life-route-red-team-v0.1.md`
- `reviews/miscatalogued-bestiary-ledger-red-team-v0.1.md`
- `reviews/surface-school-legal-form-red-team-v0.1.md`

### 원고 감사 자리표시자

- `reviews/manuscript/installment1-final-preflight-v0.1.md`
- `reviews/manuscript/installment1-first-draft-integrated-audit-v0.1.md`
- `reviews/manuscript/installment1-repetition-dialogue-audit-v0.1.md`

### 초기 옵션·README 자리표시자

`story/00-series/`, `story/10-secrets/`, `story/20-characters/`, `story/30-books/`, `story/40-ledgers/`의 일부 초기 0바이트 README·옵션 파일.

## 8. 자리표시자 처리 정책

1. C0 색인·자동 에이전트 입력에서 제외한다.
2. 파일명만으로 완료됐다고 판정하지 않는다.
3. 동일 기능의 실질 최신 문서가 있으면 `superseded empty placeholder`로 본다.
4. PR 병합 전 별도 정리 커밋에서 삭제하거나 짧은 redirect stub로 교체한다.
5. 과거 커밋 이력은 보존한다.
6. 사용자 승인 없이 실질 정본 파일을 삭제하지 않는다.

## 9. 현재 실질 대체 문서

| 빈 자리 기능 | 실질 대체 |
|---|---|
| 전체 원본성·맹점 레드팀 | `reviews/world-bible/world-bible-originality-blindspot-collection-red-team-v0.1.md` |
| 7부제 통합 | `tests/world-bible/installments-02-07-setting-scenarios-v0.1.md` |
| 세계 규칙 | `tests/world-bible/world-rules-case-scenarios-v0.1.md` |
| 학교·생활 | `tests/world-bible/school-life-operation-scenarios-v0.1.md` |
| 역사·기관 | `tests/world-bible/history-institutions-knowledge-scenarios-v0.1.md` |
| 수집 시스템 | `tests/world-bible/collection-catalog-scenarios-v0.1.md` |
| 첫 원고 감사 | `reviews/world-bible/installment1-manuscript-world-bible-reverse-audit-v0.1.md` |
| 원고 v0.2 회귀 | `tests/manuscript/installment1-v0.2-integrated-regression-v0.1.md` |
| 인간 검토 | `reviews/world-bible/human-expert-review-matrix-v0.1.md` |

## 10. canon 표기 감사

고영향 C0·decision·catalog·setting bible 문서에서 작가 승인 없이 새 항목을 `canon`으로 승격하지 않았다.

- 세계 규칙: candidate
- 학교 법적 형태: candidate+human-review
- 7부제: candidate
- 제목·인물명·종명·지역명: working/preliminary candidate
- 금강·방콕: provisional-region
- 독자용 샘플: reader-sample-candidate
- 첫 원고: review copy, canon 아님

검색 색인만으로 저장소 모든 문자열을 완전 증명할 수 없으므로 PR 병합 전 로컬 정적 검사로 `status: canon`과 0바이트 파일을 다시 확인한다.

## 11. #63 완료 판정

- 고영향 상태·근거·재검토 조건: 완료
- 열린 질문 최신화: 완료
- 과거 구조·명칭 보존: 완료
- 빈 자리표시자 식별·비정본 처리: 완료
- C0 단일 source-of-truth 지정: 완료
- PR 병합 전 물리 파일 삭제/redirect 정리: 별도 저장소 위생 작업

`world-bible-source-status-ready`로 판정한다.
