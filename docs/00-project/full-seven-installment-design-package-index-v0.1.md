---
status: complete-internal-design-package
issue: 105
accountable: A00
responsible: [A01, N00, P09]
consulted: [A13, A14, N03, N09, N16, N17, N18, P03, P07, P10, P12, P13]
human_gates: [author, reader, education-safety-legal, regional-cultural, ecology-rights, infrastructure-safety, publishing-visual-trademark]
canon: partial-author-baseline
---
# 세계관·설정집·7부제·200화 전체 설계 패키지 색인 v0.1

## 1. PM·운영 계약

- 소설 프로젝트 PM: `agents/00-orchestrator.md`
- RACI·검토 서명: `docs/00-project/novel-pm-raci-signoff-v0.1.md`
- 설계 오케스트라: `docs/14-agent-orchestra-v0.3.md`
- 원고 완성 오케스트라: `docs/14-agent-orchestra-v0.4.md`
- 작가 승인 기준선: `docs/decisions/author-approved-core-baseline-v0.1.md`
- CLAUDE 운영 계약: `CLAUDE.md`
- 완성본 집필 하네스: `docs/00-project/manuscript-completion-harness-index-v0.1.md`

## 2. 세계관·내부 설정집 C0

- C0 색인: `world/00-core/c0-world-bible-index-v0.1.md`
- C0 핵심편: `world/00-core/c0-world-bible-core-compendium-v0.1.md`
- 세계 규칙·실패·복구: `world/00-core/world-rules-failure-recovery-ledger-v0.1.md`
- 현실 접점: `world/20-systems/hidden-world-interface-v0.1.md`
- 학교 운영: `world/40-institutions/korea-school-life-operations-bible-v0.1.md`
- 학교 매력: `world/40-institutions/school-wonder-life-options-v0.1.md`
- 생물 12종: `world/20-ecology/creature-relationship-catalog-v0.1.md`
- 유물·도구·보물 8개: `world/50-artifacts/artifact-tool-treasure-catalog-v0.1.md`
- 영웅·탐사자·실패자 8명: `world/30-history/hero-explorer-failure-record-catalog-v0.1.md`
- 회랑·숨은 장소 10곳: `world/10-routes/corridor-hidden-place-catalog-v0.1.md`
- 배지·기술·장비: `world/40-institutions/school-badges-skills-equipment-catalog-v0.1.md`
- 독자용 설정집 구조: `world/60-companion/companion-record-schema-and-canon-tiers-v0.1.md`
- 시각 언어: `docs/decisions/visual-collection-language-candidate-v0.1.md`

상태: `candidate-complete / 인간 전문 검토·최종 정본 승격 대기`.

## 3. 전체 사가

- 7부제 기능 지도: `docs/decisions/seven-installment-saga-map-candidate-v0.1.md`
- 장르·보상 지도: `docs/decisions/seven-installment-genre-reward-candidate-v0.1.md`
- 인물 성장: `docs/decisions/seven-installment-character-arc-candidate-v0.1.md`
- 반복 루프: `docs/decisions/seven-installment-loop-candidate-v0.1.md`
- 3~7 규모·차별화: `story/00-series/installments-03-07-differentiation-and-scale-matrix-v0.1.md`
- 전체 회귀 감사: `reviews/series/seven-installment-full-blueprint-regression-v0.1.md`
- 7부제 맥거핀·복선·결말 회수: `story/40-ledgers/foreshadowing-mystery-payoff-ledger-v0.2.md`

상태: `author-approved structural baseline`.

## 4. 부제작별 원고 직전 상태

| 부제작 | 장르 | 장면 | 장 | 통합 패키지 | 상태 |
|---:|---|---:|---:|---|---|
| 1 | 도시 통학 미스터리 | 30 | 15 | `docs/00-project/installment1-chapter-outline-package-v0.1.md` | v0.3 review-copy / 독자 테스트 대기 |
| 2 | 학교 스포츠·친구·소속 | 32 | 16 | `docs/00-project/installment2-pre-manuscript-package-v0.1.md` | pre-manuscript-ready |
| 3 | 국내 수계 여행·탐사 | 30 | 15 | `docs/00-project/installment3-pre-manuscript-package-v0.1.md` | pre-manuscript-ready / 지역 감수 대기 |
| 4 | 해외 재난·번역 스릴러 | 32 | 16 | `docs/00-project/installment4-pre-manuscript-package-v0.1.md` | pre-manuscript-ready / 언어·현지 감수 대기 |
| 5 | 도시 추적·사회 미스터리 | 34 | 17 | `docs/00-project/installment5-pre-manuscript-package-v0.1.md` | pre-manuscript-ready / 법률·언론·교통 검토 대기 |
| 6 | 시스템 구조·권력 선택 | 36 | 18 | `docs/00-project/installment6-pre-manuscript-package-v0.1.md` | pre-manuscript-ready / 기반시설·정책 검토 대기 |
| 7 | 분산 최종 임무·졸업 | 40 | 20 | `docs/00-project/installment7-pre-manuscript-package-v0.1.md` | pre-manuscript-ready / 최종 인간 검토 대기 |

합계: **117장·234장면 카드**.

## 5. 200화 연재

- 연재 지도: `story/00-series/two-hundred-episode-serialization-map-v0.1.md`
- 상세 번호표 생성기: `scripts/build_200_episode_map.py`
- 첫 부제작 28화 브리프: `manuscript/installment-01/episode-briefs/episode-ledger-v0.1.md`

후보 배정:

- 1부제: 1~28화
- 2부제: 29~56화
- 3부제: 57~82화
- 4부제: 83~110화
- 5부제: 111~139화
- 6부제: 140~169화
- 7부제: 170~200화

상태: `candidate-production-map / 실제 원고 분량·플랫폼·출판 검토 대기`.

## 6. 원고 완성 하네스

- 하네스 H0~H12: `docs/00-project/manuscript-completion-harness-v0.1.md`
- 원고 모드 v0.2: `docs/00-project/manuscript-mode-operating-contract-v0.2.md`
- 문체·액션·풍경·연재·카피 담당: N19·N20·N21·N22·P14
- 한국 웹소설 기능 연구: `research/references/korean-webnovel-prose-serialization-patterns-v0.1.md`
- 회차·장면 브리프: `templates/episode-scene-writing-brief.md`
- 논리 시나리오: `tests/manuscript/manuscript-completion-harness-scenarios-v0.1.md`
- v0.3 결정적 빌드: `scripts/build_installment1_v03.py`
- 문장·문단 정량 감사: `scripts/audit_manuscript_style.py`
- 첫 부제작 적용 감사: `reviews/manuscript/installment1-completion-harness-audit-v0.2.md`

상태 구분:

1. design-complete
2. draft-complete
3. internal-review-ready
4. human-review-ready
5. edited-manuscript
6. publication-ready

첫 부제작은 `human-review-ready`이며 `edited-manuscript` 또는 `publication-ready`가 아니다.

## 7. 내부적으로 완료된 것

- 세계 존재 원리·힘·비용·실패·복구
- 현대 기술·기관·기록·노출 경계
- 학교 학적·생활·수업·통학·기숙·경기·안전
- 생물·유물·영웅·회랑·수집 구조
- 서하진 12→18세 성장
- 7부제 2/3/2 대형막
- 각 작품 구조 4안·3막·8시퀀스
- 234장면 기능 카드
- 공정 단서·합리적 오해·회수 구조
- 활성 인물·등장 휴지 예산
- 117장 장별 개요
- 장기 미스터리 회계와 P-17 결말
- 200화 연재 변환
- 문체·액션·풍경·연재·복선·카피 하네스
- PM·RACI·레드팀·편차 기록

## 8. 아직 완료되지 않은 것

- 실제 10~15세·성인·보호자 독자 테스트 결과
- 한국 교육행정·학교안전·의료·보험·개인정보 법률 검토
- 금강하구 지역 복수 당사자·생태·시설 검토
- 태국어·방콕 수계·현지 생활·기관·문화 검토
- 기반시설·재난 대응·긴급 권한·감사 제도 검토
- 실제 생물·유물·지도 삽화와 접근성 테스트
- 제목·상표·출판·판형·분권·가격·플랫폼 분량 검토
- 부제작 2~7 원고
- 첫 부제작 발달·분야·라인·카피·교정쇄
- 최종 canon·출판본

## 9. 정확한 완료 판정

- **세계관·내부 설정집:** 내부 설계용으로 완료.
- **7부제 전체 설계도:** 원고 직전 수준으로 완료.
- **200화 구조:** 기존 장면을 늘리지 않는 생산 후보로 완료.
- **집필 하네스:** 구축 및 첫 부제작 시험 적용 완료.
- **첫 부제작:** 인간 검토 가능한 리뷰본.
- **부제작 2~7:** 원고 승인 전 단계까지 완료.
- **편집·출판 완성본:** 인간 검토와 편집이 남아 미완료.

## 10. 다음 차단선

한 작품의 원고를 시작하려면 해당 작품의 명시적 원고 승인이 필요하다. 인간 검토 대기 항목은 승인 뒤에도 `working/provisional/human-review` 상태로 유지한다.
