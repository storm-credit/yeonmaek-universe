---
status: candidate-schema
issue: 78
scope: all-world-bible-records
format: markdown-frontmatter-compatible
---
# 세계 설정 항목 공통 ID·데이터 스키마 v0.1

## 1. 목적

생물·유물·영웅·회랑·기관·협정·사건·복선·원고 영향을 같은 추적 규칙으로 관리한다. Markdown에서 사람이 읽을 수 있고 이후 JSON·데이터베이스로 변환 가능해야 한다.

## 2. ID 접두사

| 접두사 | 유형 | 예 |
|---|---|---|
| BIO | 생물·동행 관계·비인간 당사자 | BIO-001 여울띠 |
| ART | 유물·도구·보물 | ART-008 돌림패 |
| HR | 영웅·탐사자·실패자 기록 | HR-006 백도원 |
| RTE | 회랑·숨은 장소·생활권 | RTE-001 서안 통학 회랑 |
| INS | 기관·학교·센터·재단 | INS-KR-001 학교 candidate |
| AGR | 협정·공동관리·기록 규칙 | AGR-005 정정·철회 협정 |
| EVT | 역사·현재 사건 | EVT-I1-001 통학 회랑 사건 |
| CHR | 등장인물·관계 기능 | CHR-IAN-001 서이안 |
| CLU | 공정 단서 | CLU-I1-F01 |
| QST | 미스터리 질문 | QST-I1-Q01 |
| BAD | 행동 배지 | BAD-001 첫 신고 |
| SKL | 기술·절차 | SKL-004 중지 호흡 |
| EQP | 일반 장비 | EQP-002 이중 안전선 |
| DOC | 도감·지도·판본·원장 | DOC-BEST-001 |
| REV | 검토·감사·테스트 | REV-WB-001 |

접두사는 우열이나 소유권을 뜻하지 않는다.

## 3. 공통 필수 필드

```yaml
id: BIO-001
type: creature-relationship
working_name: 여울띠
self_name: unknown-or-protected
status: candidate
canon_level: none
source_of_truth: world/20-ecology/creature-relationship-catalog-v0.1.md
first_installment: 1
last_updated: 2026-08-01
```

### 정체·상태

- `id`
- `type`
- `working_name`
- `self_name`
- `status`: canon/candidate/provisional/open/deprecated/superseded/protected-private/human-review
- `canon_level`
- `source_of_truth`
- `supersedes`
- `superseded_by`

### 근거

- `observation_scope`
- `evidence`
- `inference`
- `unknowns`
- `disagreements`
- `source_cards`
- `last_verified`
- `next_verification_condition`

### 권리·접근

- `rights_holder`
- `decision_holder`
- `access_level`
- `disclosure_level`
- `withdrawal_conditions`
- `protected_fields`
- `location_policy`

### 사건·서사

- `story_function`
- `choice_changed`
- `cost_created`
- `relationship_changed`
- `mystery_contribution`
- `first_installment`
- `reappearances`
- `payoff`
- `deletion_impact`

### 세계 규칙

- `rule_ids`
- `failure_modes`
- `stop_conditions`
- `recovery_conditions`
- `authority_matrix`

### 검토

- `author_review`
- `legal_review`
- `cultural_review`
- `ecology_review`
- `safety_review`
- `reader_review`
- `publishing_review`
- `fallback`

## 4. 유형별 추가 필드

### BIO

- 외형·크기·움직임
- 감각·행동·경고·거부
- 생태 기능
- 지성·대표·자기명칭 상태
- 서식·이동·검역
- 관계 상태
- 포획·거래·소유 금지 여부

### ART

- 제작 목적
- 제작·수리·이전·실패 이력
- 기능·발동 조건·중지 조건
- 부담·사용권·보관권
- 수리·반환·폐기 상태
- 상위호환 방지 한계

### HR

- 공식 공적
- 당시 선택
- 실제 성공
- 남은 비용
- 누락 당사자
- 공식·지역·당사자 판본
- 현재 평가와 재검토

### RTE

- 표면 생활 기능
- 장소·상태·관계 조건
- 사람·시설·생태 당사자
- 개방·폐쇄·복구·지도 폐기 상태
- 판본별 공개 범위
- 실제 위치 안전 정책

### INS

- 법적·표면 형태
- 실제 책임
- 금지 권한
- 예산·감사·기록
- 다른 기관과의 인계
- 학생·보호자·당사자 이의 절차

### AGR

- 당사자
- 적용 범위
- 허용·금지·철회
- 긴급 예외
- 비용·감사·갱신
- 실패 사례

## 5. 판본·정정 이력

각 항목은 다음 이력을 배열로 가진다.

```yaml
revision_history:
  - version: 0.1
    action: created
    reason: installment-1 design
    evidence: [CLU-I1-F01, CLU-I1-F02]
  - version: 0.2
    action: corrected
    previous: fixed-hazard-membrane
    current: conditional-moving-party
    reason: independent movement and refusal patterns
    author: school-record-team
    objections: [local-observer-note]
```

원기록을 삭제하지 않는다.

## 6. 관계 상태

생물·사람·기관 관계는 `소유 여부` 대신 다음으로 기록한다.

- 관찰
- 접근 제한
- 접근 허용
- 제한 협력
- 활동별 동행
- 이동 보조
- 거부
- 거리 두기
- 철회
- 공동관리
- 보호 폐쇄
- 위치 비공개
- 다음 재검증

## 7. 공개 수준

| 수준 | 의미 |
|---|---|
| L0 | 일반 생활·안전 공개 |
| L1 | 학생·보호자·참여자 공개 |
| L2 | 책임기관·시설·의료 공개 |
| L3 | 제한 전문·권리·검역 기록 |
| L4 | 당사자·지역 통제·민감 위치·원문 |
| L5 | 독립 감사·분쟁 판단에만 제한 접근 |

L5가 가장 진실한 서열이라는 뜻은 아니다.

## 8. 대표 10항목 변환 검증

| ID | 유형 | 공통 필드 | 권리·상태 | 사건 연결 | 검토·후퇴 |
|---|---|---|---|---|---|
| BIO-001 여울띠 | BIO | 충족 | 이동·비공개·재검증 | 부제작 1·5·7 | 이름·생태 검토 |
| BIO-003 온기고리 | BIO | 충족 | 활동별 동행·철회 | 부제작 2 | 장기 마스코트 금지 |
| BIO-008 문답결 | BIO | 충족 | 자기명칭·대표·위치 보호 | 부제작 4·7 | 현지 감수 |
| ART-003 비움매듭 | ART | 충족 | 공동보관·수용처 책임 | 부제작 5·6 | 부담 이동 상한 |
| ART-008 돌림패 | ART | 충족 | 위임·만료·분산 | 부제작 6·7 | 비상 최종열쇠 금지 |
| HR-004 민서림 | HR | 충족 | 판본·누락 협력자 | 부제작 2·3 | 공식 공적 유지 |
| HR-006 백도원 | HR | 충족 | 감사·수용처 비용 | 부제작 6 | 성공 무효화 금지 |
| RTE-001 서안 | RTE | 충족 | 공동관리·보호폐쇄 | 부제작 1·7 | 합성 위치 유지 |
| RTE-004 갈림물목 | RTE | 충족 | 지역판·계절 재검증 | 부제작 3 | 지역 감수 |
| INS-KR-001 학교 | INS | 충족 | 학생·보호자 이의 | 전 부제작 | 법률 후퇴안 |

손실 없이 동일 스키마에 대응: PASS

## 9. 파일 적용 규칙

- 원문 서사 문서 전체를 데이터 표로 바꾸지 않는다.
- 각 상세 문서 상단·색인에 핵심 ID를 연결한다.
- 중복 항목은 ID가 같으면 하나의 source-of-truth만 지정한다.
- 작업 이름이 바뀌어도 ID는 유지한다.
- 실제 자기명칭이 공개되면 외부명을 삭제하지 않고 별도 필드로 병기한다.
- 지역 감수 실패 시 ID는 유지하고 내용·이름·등장 작품을 수정할 수 있다.

## 10. 금지

1. ID 번호를 희귀도·세대·강함 순위로 해석
2. 데이터 필드가 없는 빈칸을 임의 추정으로 채움
3. protected-private를 미설계로 간주
4. 테스트 통과를 canon 승인으로 간주
5. 사람·지역·당사자를 데이터 객체로만 축소
6. 실제 개인정보·민감 좌표를 저장소에 기록
