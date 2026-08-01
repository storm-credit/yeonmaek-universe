---
status: active
supersedes: docs/14-agent-orchestra-v0.2.md
accountable: A00
issue: 95
---
# 에이전트 오케스트라 v0.3

## 1. 총괄

A00은 소설 프로젝트 PM이며 단일 Accountable이다.

- 세계관 리드: A01
- 서사 리드: N00
- 설정집·정본 리드: P09
- 준비도 통제: A14
- 독립 레드팀: A13
- 인간 검토 라우팅: P12

## 2. 조직

### 세계 평의회

A01~A05, 권역·국가 데스크, A12.

세계 원리·현실 접점·힘·생태·기관·학교·지역 문화를 담당한다.

### 서사 평의회

N00~N18.

결말·사가·부제작·인과·복선·인물·정보·리듬·독창성·원고 인터페이스를 담당한다.

### 제작 관리팀

P01~P13.

정본·용어·연표·지도·도감·출처·독자 이해·동반출판·매체·인간 검토·시각 언어를 담당한다.

### 검증 평의회

A12,A13,A14,N15,N16,P06,P07,P09,P12.

문화·허점·준비도·독창성·연속성·출처·독자·정본·인간 게이트를 담당한다.

## 3. 실행 방식

이 저장소의 에이전트 문서는 역할 계약이다. 별도 실행 로그가 없으면 여러 독립 AI가 병렬 실행됐다고 주장하지 않는다.

기본 파이프라인:

`작가 의도 → A00 분해/RACI → 분야별 R → 상호 C → A13 공격 → A14 게이트 → P09/N16 영향 → 작가/인간 게이트 → 상태 갱신`

## 4. 핵심 산출물 최소 패널

- 세계 규칙: A01+A02+A03+A04 → A13+A14+N16
- 학교: A05+A02 → N13+P03+A14+A13+인간 안전 검토
- 생물: A04+P05 → A12+P06+P13+A13+인간 생태/현지 검토
- 사가: N00+N02+N17 → N01+N03+N09+N10+N15+N16+A13
- C0 설정집: P09+P01 → A01+N00+P02~P06+N16+A13
- 독자용 설정집: P10+P13 → P05+P07+A12+P09+A13
- 원고 패치: N18+N16+P09 → N00+N03+N09+N11+N12+A13

## 5. 문서 머리말

```yaml
accountable: A00
responsible: [IDs]
consulted: [IDs]
challenged_by: [A13]
human_gates: [author, readers, experts]
source_of_truth: true|false
status: candidate|provisional|canon|deprecated|human-review
```

기존 문서는 `docs/00-project/artifact-agent-provenance-matrix-v0.1.md`에서 소급 관리한다.

## 6. 원고 모드

설계 단계에서는 완성 장면·대사를 쓰지 않는다.

작가가 명시적으로 원고 단계를 승인하면 별도 원고 계약과 N18 검토 아래 작성할 수 있다. 원고는 설정을 자동 canon으로 만들지 않으며, 새 사실은 P09/N16 역검증을 거친다.

## 7. 완료 표현

- `candidate-ready`: 내부 설계에 사용 가능
- `conditional-ready`: 작가·독자·전문가 게이트가 남음
- `canon`: 작가 승인과 필요한 검토 통과
- `publication-ready`: 출판·상표·시각·접근성까지 통과

내부 PASS는 독립 AI 실행·인간 전문가·실제 독자 검토 완료가 아니다.

## 8. 현재 판정

- 세계관·C0 설정집: conditional-ready
- 7부제 설계도: conditional-ready
- 독자용 설정집: text-prototype-ready
- 첫 부제작: review-draft/name-migration-pending
- 부제작 2 원고: blocked

상세 감사:

- `reviews/orchestra/novel-pm-agent-division-world-bible-audit-v0.1.md`
- `reviews/orchestra/world-bible-agent-panel-recheck-v0.1.md`
