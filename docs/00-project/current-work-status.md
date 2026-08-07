# 현재 작업 상태

기준일: 2026-08-08
저장소: `storm-credit/yeonmaek-universe`
운영 브랜치: `main`

## 현재 단계

**정본 우선 계층형 스토리 오케스트라 마이그레이션 완료. 신규 원고 잠금 유지. 세계·설정·계층 S1 공백 보강 대기.**

## 실제 자산 확인

- 세계관·설정집: `world/`에 핵심 규칙, 5권역·25거점, 생물·현상 36종, 유물·도구 30종, 학교·기관 9개, 역사 15사건 등의 문서가 존재
- 인물: `characters/`에 주인공 후보 정본, 핵심 배역, 관계 매트릭스, 5부 독립 아크가 존재
- 이야기: 5부·15 Act·45 Subact·90장 기능표와 5개 부 씬 비트가 존재
- 원고: 제1부 1~11장 존재
- 검수: 장별 1~11장 검수, Act 1·2 통합 감사 존재
- `story/25-subacts/`: 다섯 파일의 파일명과 내부 부 번호·9 Subact 구조 일치, 이름 변경 없음

## 정본 운영

- Constitution: `canon/CANON_CONSTITUTION.md`
- Amendments: `canon/CANON_AMENDMENTS.md`
- Decision Log: `canon/DECISION_LOG.md`
- 공식 계층: `story/00-series/OFFICIAL_HIERARCHY_MAPPING.md`
- 오케스트레이션: `orchestration/`
- 상태 장부: `ledgers/`

## 공식 구조

`Series → Grand Act → Volume Act → Arc → Subact → Episode → Scene`

기존 대응:
- 5부 → Grand Act
- 15 Act → Volume Act
- Volume Act별 기능성 Arc 15개
- 45 Subact → Subact
- 90장 → Episode
- 장별 씬 비트 → Scene

## 원고 진행

- 전체: **11/90장 존재**
- 제1부: **11/18장 존재**
- Act 1: 1~6장, 통합 감사 통과·잠금
- Act 2: 7~11장, 통합 감사 통과·잠금
- Act 3: 설계 존재, 원고 없음
- 기존 원고 삭제·신규 원고 생성: 없음

## 현재 원고 잠금

**LOCKED**

사용자가 다시 명시적으로 허가하기 전까지 신규 원고, 대사, 장면 본문을 작성하지 않는다. 잠금 해제에는 대상 CP와 S0=0, S1=0이 추가로 필요하다.

## 새 완료 게이트 감사

- S0: **0**
- S1: **7**
- 운영 구조 마이그레이션: 통과
- 세계·설정·계층의 신규 집필 준비: 차단
- 상세: `reviews/design/world-setting-completion-gap-audit-v1.0.md`
- 장부: `ledgers/WORLD_GAP_LEDGER.md`

주요 차단:
1. P1 후보 문서와 “완료” 상태 표기의 정본 지위 충돌
2. 문화·종교 생활 기능 부재
3. 경제·법·예산·절차 비용 부족
4. 25거점 필수 장소 필드 불완전
5. 핵심 인물 통합 카드·정보상한·오프스크린 행동 부족
6. 아이템·생물 실제 인스턴스 상태 추적 부족
7. 공식 계층 11필드 불균일

## 분량 정책

- 최소 기준만 둔다.
- 상한 없음.
- 현재 신규 Episode 최소: 공백 제외 2,500자.
- 기존 1~11장은 소급 증보하지 않는다.
- 현재는 신규 집필 자체가 잠겨 있다.

## 다음 자동 작업

1. WG-S1-001: `world/`·`characters/` 원문별 정본 지위 재분류
2. 제1부 후반에 필요한 장소·기관·아이템·인물 카드부터 템플릿 이관
3. 문화·종교, 경제·법 절차 보강
4. Series→Episode 11필드 역산 보강
5. 아이템·복선·오프스크린·POV 장부 연결
6. S0/S1 재감사
7. 사용자의 명시적 허가가 있을 때만 원고 잠금 해제 검토
