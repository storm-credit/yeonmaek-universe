---
status: package-index
issue: 50
readiness: conditional-ready
---
# 원고 직전 설계 패키지 색인 v0.1

## 사용법

이 문서는 원고 작성자가 저장소 전체를 처음부터 읽지 않고도 필요한 설계·근거·테스트·차단선을 순서대로 찾게 하는 진입점이다.

현재 단계는 **세계관·7부제 사가 candidate 기준선 완료 / 첫 부제작 작가 승인 대기**다. 원고·장면·대사·회차는 아직 작성하지 않는다.

# 1. 운영 계약

1. `CLAUDE.md`
   - 자동 완주, 질문·중지 조건, 4안, 함정 체크, 메타 프롬프트, 검증, 기억·편차 규칙.
2. `docs/00-project/meta-prompt-compiler-template-v0.1.md`
   - Goal/Audience/Inputs/Outputs/Constraints/Success/Verification/Stop/Next 형식.
3. `tests/autonomous-design-operating-contract-scenarios-v0.1.md`
   - 운영 계약 회귀 테스트.
4. `research/references/agent-workflow-patterns-v0.1.md`
   - Karpathy Guidelines, Superpowers, Understand-Anything, agentmemory, claude-video의 추상 기능 적용.
5. `docs/logs/assumptions/README.md`
6. `docs/logs/deviations/README.md`
7. `docs/logs/deviations/2026-07-31-title-and-saga-reframing-deviation-v0.1.md`

# 2. 세계관 최소 기준선

## 핵심

- `world/00-core/minimum-worldbuilding-baseline-v0.1.md`
- `world/00-core/worldbuilding-readiness-matrix-v0.1.md`
- `reviews/worldbuilding-gates-cross-consistency-v0.1.md`

## 8개 게이트

1. 존재론: `world/00-core/ontology-boundary-options-v0.1.md`
2. 힘·비용: `world/20-systems/power-training-cost-options-v0.1.md`
3. 생태·권리: `world/20-systems/sentience-ecology-rights-options-v0.1.md`
4. 현실 제도: `world/20-systems/secret-society-public-institutions-options-v0.1.md`
5. 학교·생활: `world/30-korea/school-education-life-options-v0.1.md`
6. 역사·국제 질서: `world/10-regions/history-international-order-options-v0.1.md`
7. 한국 생활권: `world/30-korea/korea-first-stage-life-route-options-v0.1.md`
8. 갈등 엔진: `world/20-systems/structural-conflict-engine-options-v0.1.md`

핵심 문장:

> 현대 현실과 같은 세계 안에 서로 다른 생태 위상이 겹치며, 모든 개입의 부담은 어딘가에 남고 기존 질서는 그 부담을 보이지 않는 장소·생물·주민·기록으로 전가해 왔다.

# 3. 메인 사가

## 결정·구조

- `docs/decisions/long-form-growth-saga-intent-v0.1.md`
- `docs/decisions/five-book-series-candidate-v0.1.md` — `reframing-required`
- `docs/decisions/protagonist-age-time-candidate-v0.1.md`
- `docs/decisions/seven-installment-saga-map-candidate-v0.1.md`
- `docs/26-pre-manuscript-dependency-graph-v0.1.md`

## 7부제 candidate

- 동일 주인공
- 만 12세 전후→만 18세 전후, 약 6년
- 대형막 I 1~2: 발견과 소속
- 대형막 II 3~5: 기준 확장과 신뢰 붕괴
- 대형막 III 6~7: 선택과 재구성
- 한 학년=한 부제작 공식 금지
- 한국 학교·가족·현실 친구·도시 생활 지속

## 통합 검증

- `tests/seven-installment-integrated-regression-v0.1.md`
- `reviews/pre-manuscript-integrated-red-team-v0.1.md`

# 4. 결말·비밀·복선

- `docs/decisions/ending-state-candidate-v0.1.md` 또는 #16 관련 결정 문서
- `story/00-series/core-secret-macguffin-options-v0.1.md`
- `story/00-series/foreshadowing-ledger-v0.1.md`
- `docs/decisions/protagonist-final-personal-cost-candidate-v0.1.md`

결말 방향:

- 독점적 우선 접근·결정권 해체
- 단계적 공개
- 회랑 공동관리와 부담 원장
- 학교의 교육·보호와 수사·연구·분쟁 심판 권한 분리
- 모든 지역을 동일 제도로 통일하지 않음

장기 미확인 기본 상한:

- 첫 부제작에서 삭제 항목 ID 1개
- 각 부제작 현장 사건은 장기 비밀의 정답 없이 독립 완결

# 5. 인물·관계 성장

## 사가 전체

- `docs/decisions/seven-installment-character-arc-candidate-v0.1.md`
- `story/20-characters/seven-installment-character-arc-options-v0.1.md`

후보:

- 홈베이스 관계 고정+현장 핵심팀 2~4명 회전
- 고정 삼인조 금지
- 주인공 없이 작동하는 관계·협력 설계
- 능력 상승은 공격력이 아니라 불확실성·동의·책임 처리 능력 상승

## 첫 부제작

- `story/20-characters/installment1-active-character-profile-options-v0.1.md`
- `tests/installment1-active-character-profile-scenarios-v0.1.md`
- `reviews/installment1-active-character-profile-red-team-v0.1.md`
- `docs/decisions/installment1-active-character-profile-candidate-v0.1.md`

활성 작업 후보:

- 서하진 / 문하람 / 차도겸 / 강유나 / 서지현 / 오세린 / 여울띠 가족군

모든 이름·성별·구체 직업은 작가 승인 전 작업 candidate다.

# 6. 수집 생태계

- `docs/decisions/collection-ecosystem-candidate-v0.1.md`
- `world/20-systems/collection-ecosystem-options-v0.1.md`
- `tests/collection-ecosystem-scenarios-v0.1.md`
- `reviews/collection-ecosystem-red-team-v0.1.md`

핵심축:

1. 동행종·협력 생물
2. 도감 항목·정정 이력
3. 회랑 지도·숨은 장소
4. 유물·도구·보물
5. 영웅·탐사자·실패자 기록

운영:

- 중심 1축+보조 1축+이전 항목 재맥락화
- 소유·희귀도·100% 완성이 아니라 관찰·정정·관계·반환·보호 폐쇄가 보상
- 작품별 수량은 할당량이 아니라 상한

# 7. 학교·경기·생활 반복

- `docs/decisions/seven-installment-loop-candidate-v0.1.md`
- `world/30-korea/surface-school-legal-form-options-v0.1.md`
- `docs/decisions/surface-school-legal-form-candidate-v0.1.md`
- `world/20-systems/representative-sport-simplified-options-v0.2.md`
- `docs/decisions/representative-sport-candidate-v0.1.md`

학교 candidate:

- 인가 중학교·고등학교
- 별도 현장교육센터
- 외부 독립 의료·구조·수사·권리·분쟁·국제 조정 주체

대표 경기:

- 부제작 2에서만 중심화
- 직접 공격·정신 침입·강제 생물 사용 금지
- 단일 가시적 승리 조건

# 8. 지역

## 첫 부제작

- `research/regions/installment1-capital-commute-zone-options-v0.1.md`
- `tests/installment1-capital-commute-zone-scenarios-v0.1.md`
- `reviews/installment1-capital-commute-zone-red-team-v0.1.md`
- `docs/decisions/installment1-capital-commute-zone-candidate-v0.1.md`

candidate: 합성 `서안 생활권`.

## 부제작 3

- `research/regions/kr-installment3-domestic-region-options-v0.1.md`
- `docs/decisions/kr-installment3-domestic-region-candidate-v0.1.md`

candidate: 서천–군산 금강하구 생활권. 현지 인간 감수 전 생활·생업 세부 canon 금지.

## 부제작 4

- #36 해외 지역 산출물과 방콕–차오프라야 dossier

candidate: 방콕–차오프라야 도시 수계. 태국어 자료·현지 인간 감수 전 문화 세부 canon 금지.

# 9. 첫 부제작 완성 패키지

## 중심 문서

- `docs/decisions/first-titled-installment-blueprint-candidate-v0.1.md`

## 구성 문서

- 생활권 D-054
- 인물 D-055
- 비인간 당사자 D-056
- 압력·책임 D-057
- 학교·수집·사가 D-060~D-065

## 작업 한 문장

완전한 증거를 모을 때까지 이상을 숨기던 만 12세 아이가, 비와 안전 공사로 두 이동로가 차례로 닫히는 통학 구간에서 고정 위험종으로 오분류된 여울띠 가족군을 발견하고, 불완전한 기록을 공유해 판단권을 넘기는 법을 배운다.

## 장면 설계 진입 상태

`candidate-ready-for-author-gate`

작가 승인 전에는 장면·회차·대사·원고를 작성하지 않는다.

# 10. 제목·브랜드

- `research/references/main-title-collision-precheck-v0.1.md`
- `story/00-series/audience-tone-brand-options-v0.1.md`
- `tests/audience-tone-brand-scenarios-v0.1.md`
- `reviews/audience-tone-brand-red-team-v0.1.md`
- `docs/decisions/audience-tone-brand-candidate-v0.1.md`

상태:

- 저장소 코드명: 연맥
- 메인 예비 candidate: 겹길
- 첫 부제 작업 예시: 사라진 통학로
- 학교 작업명: 깊은결학교
- 경기 작업명: 길문전
- 비인간 작업명: 여울띠

어느 이름도 법률·상표·출판 검토를 통과한 canon이 아니다.

# 11. 동반 출판

- `world/60-companion/companion-publication-framework-options-v0.1.md`
- `world/60-companion/companion-record-schema-and-canon-tiers-v0.1.md`
- `tests/companion-publication-scenarios-v0.1.md`
- `reviews/companion-publication-red-team-v0.1.md`
- `docs/decisions/companion-publication-framework-candidate-v0.1.md`

첫 착수 슬롯:

1. 정정되는 생태 도감
2. 겹길 회랑 지도첩

본편 이해에 필수이지 않으며 C0 내부 정본은 판매하지 않는다.

# 12. 인간 승인과 전문 검토

- `docs/00-project/human-approval-and-expert-review-checklist-v0.1.md`

우선 작가 승인:

- 7부제 장기 성장형 묶음
- 첫 부제작 사건·생활권·인물·여울띠·두 시계
- 주인공 기본 정체성
- 작업 제목 유지 여부

전문 검토:

- 교육행정·학교안전·미성년 현장활동
- 합성 생활권·시설·교통·수방
- 10~15세 독자 테스트
- 금강하구·방콕 현지 인간 감수
- 상표·ISBN·출판·지도·개인정보·라이선스

# 13. 현재 판정

| 범위 | 상태 |
|---|---|
| 운영 계약 | ready |
| 세계관 최소 기준선 | candidate-baseline-ready |
| 7부제 메인 사가 | candidate-baseline-ready |
| 첫 부제작 원고 직전 구조 | candidate-ready-for-author-gate |
| 첫 부제작 장면·회차 | author-gate blocked |
| 부제작 2~7 전체 기능 | blueprint-ready |
| 부제작 2~7 구체 장면 | not started / approval 이후 순차 설계 |
| 실재 문화·법률·상표 | human-review blocked |
| 소설 원고 | not started by design |
