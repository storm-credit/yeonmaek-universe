---
status: clean-world-bible-design-index
accountable: A00
canon: false
branch: canon/world-bible-blueprint-clean
---
# 세계관·설정집·사가 설계 패키지 색인 v0.4

## 범위

이 브랜치는 실제 소설 본문이 아니라 다음 설계 자산만 관리한다.

- 세계관 설정집
- 인물·기관·학교·생태·지역·능력 체계
- 메인 사가와 부제작 구조 후보
- 막·시퀀스·장·장면 카드 수준의 이야기 설계
- 복선·연표·권한 구조
- 조사·검증·레드팀 문서

실제 원고, 원고 승인 기록, 초고 완료 패키지, 원고 기반 독자 테스트는 제외한다.

## 운영 기준

- 최상위 운영 계약: `CLAUDE.md`
- 정리 브랜치 상태: `docs/00-project/world-bible-clean-branch-status-v0.1.md`
- 복구 감사: `docs/00-project/clean-branch-recovery-audit-v0.1.md`
- 교정된 후보 기준선: `docs/decisions/clean-branch-candidate-baseline-v0.1.md`
- 최신 상태 인벤토리: `docs/decisions/world-bible-status-inventory-v0.2.md`
- 프로젝트 의도: `docs/12-author-intent-v0.1.md`

`진행`, `계속`, `이어서진행`, `자동으로 끝까지`는 설정집·설계도 자동 진행만 뜻하며 실제 원고 작성 승인이 아니다.

## 세계관·설정집

- C0 색인: `world/00-core/c0-world-bible-index-v0.1.md`
- C0 핵심편: `world/00-core/c0-world-bible-core-compendium-v0.1.md`
- 세계 규칙·실패·복구: `world/00-core/world-rules-failure-recovery-ledger-v0.1.md`
- 현실 접점: `world/20-systems/hidden-world-interface-v0.1.md`
- 힘 체계: `world/20-systems/power-system-architecture-v0.1.md`
- 학교 운영: `world/40-institutions/korea-school-life-operations-bible-v0.1.md`
- 학교 매력: `world/40-institutions/school-wonder-life-options-v0.1.md`
- 생물 관계: `world/20-ecology/creature-relationship-catalog-v0.1.md`
- 유물·도구·보물: `world/50-artifacts/artifact-tool-treasure-catalog-v0.1.md`
- 역사 인물 기록: `world/30-history/hero-explorer-failure-record-catalog-v0.1.md`
- 회랑·숨은 장소: `world/10-routes/corridor-hidden-place-catalog-v0.1.md`
- 배지·기술·장비: `world/40-institutions/school-badges-skills-equipment-catalog-v0.1.md`
- 동반 설정집 구조: `world/60-companion/companion-record-schema-and-canon-tiers-v0.1.md`

판정: `candidate-complete`. 작가 승인과 인간 전문 검토 전에는 final canon이 아니다.

## 메인 사가 후보

- 장기 성장 사가 후보: `docs/decisions/long-growth-main-saga-candidate-v0.1.md`
- 7부제 기능 지도: `docs/decisions/seven-installment-saga-map-candidate-v0.1.md`
- 장르·보상 지도: `docs/decisions/seven-installment-genre-reward-candidate-v0.1.md`
- 인물 성장 지도: `docs/decisions/seven-installment-character-arc-candidate-v0.1.md`
- 반복 루프: `docs/decisions/seven-installment-loop-candidate-v0.1.md`
- 장기 복선·미스터리 원장: `story/40-ledgers/foreshadowing-mystery-payoff-ledger-v0.2.md`

7부제와 장·장면 카드 수는 모두 후보 설계다. 실제 작품 길이, 장 수, 회차 수는 확정하지 않는다.

## 교정 사항

`200화`는 이 프로젝트 요구에서 나온 값이 아니라 다른 소설 프로젝트에서 잘못 유입된 교차 프로젝트 오염값으로 판정했다.

따라서 다음을 정리 브랜치에서 제거했다.

- `story/00-series/two-hundred-episode-serialization-map-v0.1.md`
- `scripts/build_200_episode_map.py`

앞으로 이 프로젝트의 회차 수는 `미정`으로 관리한다. 세계관·설정집·설계도 완성도와 연재 화수는 별개다.

## 현재 완료 판정

- 세계관·내부 설정집: 내부 설계 후보 완료
- 사가·부제작 구조: 상세 후보 설계 존재
- 장·장면 카드: 구조 검증용 후보
- 회차 수·연재 분량: 미정
- 실제 소설 본문: 잠금
- final canon·출판 준비: 미완료
