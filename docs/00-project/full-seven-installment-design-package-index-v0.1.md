---
status: clean-world-bible-design-index
accountable: A00
human_gates: [author, reader, education-safety-legal, regional-cultural, ecology-rights, infrastructure-safety, publishing-visual-trademark]
canon: false
branch: canon/world-bible-blueprint-clean
---
# 세계관·설정집·7부제 설계 패키지 색인 v0.3

## 1. 범위

이 색인은 실제 소설 본문이 아니라 다음 설계 자산만 연결한다.

- 세계관 설정집
- 인물·기관·학교·생태·지역·능력 체계
- 메인 사가와 부제작 구조 후보
- 장·장면 카드·화별 기능 설계
- 복선·연표·권한 구조
- 조사·검증·레드팀 문서

실제 원고, 원고 승인 기록, 초고 완료 패키지, 원고 기반 독자 테스트는 이 브랜치의 정본 범위가 아니다. 해당 자료는 `archive/full-saga-draft-unapproved`에만 보존한다.

## 2. 운영 기준

- 최상위 운영 계약: `CLAUDE.md`
- 정리 브랜치 상태: `docs/00-project/world-bible-clean-branch-status-v0.1.md`
- 복구 감사: `docs/00-project/clean-branch-recovery-audit-v0.1.md`
- 교정된 후보 기준선: `docs/decisions/clean-branch-candidate-baseline-v0.1.md`
- 최신 상태 인벤토리: `docs/decisions/world-bible-status-inventory-v0.2.md`
- 프로젝트 의도: `docs/12-author-intent-v0.1.md`
- 원고 직전 준비도 기준: `docs/decisions/pre-manuscript-integration-readiness-v0.1.md`

`진행`, `계속`, `이어서진행`, `자동으로 끝까지`는 설정집·설계도 자동 진행만 뜻한다. 실제 원고 작성 승인이 아니다.

## 3. 세계관·내부 설정집 C0

- C0 색인: `world/00-core/c0-world-bible-index-v0.1.md`
- C0 핵심편: `world/00-core/c0-world-bible-core-compendium-v0.1.md`
- 세계 규칙·실패·복구: `world/00-core/world-rules-failure-recovery-ledger-v0.1.md`
- 현실 접점: `world/20-systems/hidden-world-interface-v0.1.md`
- 힘 체계: `world/20-systems/power-system-architecture-v0.1.md`
- 학교 운영: `world/40-institutions/korea-school-life-operations-bible-v0.1.md`
- 학교 매력: `world/40-institutions/school-wonder-life-options-v0.1.md`
- 생물 관계 카탈로그: `world/20-ecology/creature-relationship-catalog-v0.1.md`
- 유물·도구·보물: `world/50-artifacts/artifact-tool-treasure-catalog-v0.1.md`
- 영웅·탐사자·실패 기록: `world/30-history/hero-explorer-failure-record-catalog-v0.1.md`
- 회랑·숨은 장소: `world/10-routes/corridor-hidden-place-catalog-v0.1.md`
- 배지·기술·장비: `world/40-institutions/school-badges-skills-equipment-catalog-v0.1.md`
- 독자용 설정집 구조: `world/60-companion/companion-record-schema-and-canon-tiers-v0.1.md`
- 시각 언어 후보: `docs/decisions/visual-collection-language-candidate-v0.1.md`

판정: `candidate-complete`. 인간 전문 검토와 작가 승격 전에는 final canon이 아니다.

## 4. 메인 사가 후보

- 장기 성장 사가 후보: `docs/decisions/long-growth-main-saga-candidate-v0.1.md`
- 7부제 기능 지도: `docs/decisions/seven-installment-saga-map-candidate-v0.1.md`
- 장르·보상 지도: `docs/decisions/seven-installment-genre-reward-candidate-v0.1.md`
- 인물 성장 지도: `docs/decisions/seven-installment-character-arc-candidate-v0.1.md`
- 반복 루프: `docs/decisions/seven-installment-loop-candidate-v0.1.md`
- 3~7부 규모·차별화: `story/00-series/installments-03-07-differentiation-and-scale-matrix-v0.1.md`
- 전체 설계 회귀 감사: `reviews/series/seven-installment-full-blueprint-regression-v0.1.md`
- 7부제·117장·200화 적합성 재감사: `reviews/series/seven-117-200-suitability-reaudit-v0.1.md`
- 장기 복선·미스터리 원장: `story/40-ledgers/foreshadowing-mystery-payoff-ledger-v0.2.md`

판정:

- 7부제·2/3/2 대형막: `strong candidate`
- 117장·234장면 카드: `provisional design resolution`
- 200화: `optional production scenario C`

7부제 유지가 200화 확정을 의미하지 않는다.

## 5. 부제작별 설계 상태

| 부제작 | 장르 후보 | 장면 카드 | 장 후보 | 설계 패키지 | 상태 |
|---:|---|---:|---:|---|---|
| 1 | 도시 통학 미스터리 | 30 | 15 | `docs/00-project/installment1-chapter-outline-package-v0.1.md` | 설계 후보 |
| 2 | 학교 스포츠·친구·소속 | 32 | 16 | `docs/00-project/installment2-pre-manuscript-package-v0.1.md` | 원고 직전 설계 후보 |
| 3 | 국내 수계 여행·탐사 | 30 | 15 | `docs/00-project/installment3-pre-manuscript-package-v0.1.md` | 지역 감수 대기 |
| 4 | 해외 재난·번역 | 32 | 16 | `docs/00-project/installment4-pre-manuscript-package-v0.1.md` | 언어·현지 감수 대기 |
| 5 | 도시 추적·기록 공개 | 34 | 17 | `docs/00-project/installment5-pre-manuscript-package-v0.1.md` | 법률·개인정보 검토 대기 |
| 6 | 시스템 구조·권력 선택 | 36 | 18 | `docs/00-project/installment6-pre-manuscript-package-v0.1.md` | 기반시설·정책 검토 대기 |
| 7 | 분산 최종 임무·졸업 | 40 | 20 | `docs/00-project/installment7-pre-manuscript-package-v0.1.md` | 최종 구조 검토 대기 |

117장·234장면 카드는 확정 분량이 아니라 비교·검증 가능한 설계 해상도다. 구조 감사에서 통합·분할할 수 있다.

## 6. 연재 변환 시나리오

- 200화 후보 지도: `story/00-series/two-hundred-episode-serialization-map-v0.1.md`
- 번호표 생성기: `scripts/build_200_episode_map.py`

200화는 네 가지 변환안 중 하나인 카드 혼합형 시나리오다. 실제 원고 분량, 플랫폼 정책, 출판 단위 검토 전에는 목표 화수로 고정하지 않는다.

향후 비교 대상:

- 117화 장 단위안
- 180~220화 가변안
- 200화 카드 혼합안
- 234화 장면 카드 단위안

## 7. 설정집 검증 자산

- 세계관 상세 갭 감사: `reviews/world-bible/full-detail-world-bible-gap-audit-v0.1.md`
- 설정집 독창성·맹점 감사: `reviews/world-bible/world-bible-originality-blindspot-collection-red-team-v0.1.md`
- 정본 중복·자리표시자 감사: `reviews/world-bible/source-of-truth-duplicate-placeholder-audit-v0.1.md`
- 인간 전문가 검토표: `reviews/world-bible/human-expert-review-matrix-v0.1.md`
- 설정집 최종 조건 테스트: `tests/world-bible/world-bible-final-completion-scenarios-v0.1.md`
- 7부제 통합 회귀: `tests/seven-installment-integrated-regression-v0.1.md`

원고를 읽거나 초고 완료를 전제로 한 역감사·독자 테스트는 정리 브랜치에서 제외한다.

## 8. 완료된 복구 작업

- 실제 원고와 원고 승인 문서 격리
- 원고 완료·집필 하네스·원고 감사 패키지 격리
- 원고 기반 독자 테스트와 역검증 격리
- 잘못된 `author-approved` 기준선 제거
- README·상태표·설계 색인 교정
- 7부제·117장·200화 적합성 재감사

## 9. 다음 자동 작업

1. 부제작 1~7 설계 패키지의 원고 파생 표현 감사
2. 3~7부 장르·행동·보상 중복 감사
3. 해리포터에서 가져올 기능과 독자적 변형 거리 재점검
4. 주인공·학교·대표 경기·수집 요소의 매력도 재검토
5. 연표·나이·학사·이동거리·권한 구조 통합 감사
6. 작가가 한눈에 검토할 최종 설정집 패키지 작성

## 10. 현재 완료 판정

- 세계관·내부 설정집: 내부 설계 후보가 충분히 축적됨.
- 7부제: 강한 사가 후보.
- 117장·234장면: 상세 구조 검사에 쓰는 임시 설계 해상도.
- 200화: 선택 가능한 플랫폼 시나리오.
- 실제 소설 본문: 정리 브랜치에 존재하지 않으며 새로 작성하지 않음.
- 최종 canon·출판 준비: 미완료.

원고 단계는 사용자가 작품과 범위를 특정하여 명시적으로 승인하기 전까지 잠금 상태다.
