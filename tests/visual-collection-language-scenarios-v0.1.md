---
status: internal-test
issue: 98
accountable: A00
responsible: [P13, P07]
consulted: [P05, P10, P11, A04, A12, N15]
challenged_by: [A13]
human_gates: [art-director, illustrator, child-readers, publishing, accessibility]
---
# 시각 수집 언어 테스트 v0.1

| ID | 검사 | 결과 |
|---|---|---|
| VC01 | 대표 생물 6종이 실루엣만으로 구분되는가 | PASS DESIGN SPEC / HUMAN ART TEST PENDING |
| VC02 | 얼굴 표정 없이 상태를 표현할 수 있는가 | PASS |
| VC03 | 생물 12종이 색상만으로 구별되지 않는가 | PASS POLICY |
| VC04 | 유물 8종이 기능 문법과 형태가 연결되는가 | PASS |
| VC05 | 유물이 전투 아이템·희귀도 카드처럼 보이지 않는가 | PASS |
| VC06 | 회랑 개방·조건부·보호폐쇄·비공개가 별도 기호인가 | PASS |
| VC07 | 위치 비공개가 빈 지도 오류처럼 보이지 않는가 | PASS — 보호 상태 카드 병기 |
| VC08 | 도감 정정이 틀린 카드 폐기가 아니라 판본 수집이 되는가 | PASS |
| VC09 | 흑백 인쇄에서 상태 구분 가능한가 | PASS SPEC / PRINT TEST PENDING |
| VC10 | 색각·저시력 접근성 대체가 있는가 | PASS SPEC / HUMAN TEST PENDING |
| VC11 | 실제 문화·종교 문양을 직접 사용하지 않는가 | PASS POLICY |
| VC12 | 어린 독자가 좋아하는 항목을 이유와 함께 고르는가 | HUMAN TEST PENDING |
| VC13 | 성인 독자에게 유아 캐릭터 상품처럼 보이지 않는가 | HUMAN TEST PENDING |
| VC14 | 모바일 카드에서 핵심 정보가 과밀하지 않는가 | PROTOTYPE PENDING |

## 마스코트화 공격 테스트

- 모든 생물에 큰 눈 추가: REJECT
- 생물을 학교 팀 엠블럼으로 영구 사용: REJECT 또는 당사자·공개권 별도 검토
- 희귀도 색 테두리: REJECT
- 포획 완료 도장: REJECT
- `관찰 범위 변경`, `철회`, `보호 폐쇄` 상태 수집: ACCEPT

## 재개 조건

실제 시안에서 다음 중 하나면 #98 재개:
- 여울띠·물갈피·문답결이 모두 투명 리본처럼 보임
- 유물 절반 이상이 원형 금속 장신구로 겹침
- 지도 기호가 색을 제거하면 구분되지 않음
- 아이들이 생물보다 희귀도·전투력부터 질문함
- 도감이 본편 정답을 먼저 공개함
