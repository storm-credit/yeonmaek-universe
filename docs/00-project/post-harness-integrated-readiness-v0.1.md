---
status: integrated-readiness-after-manuscript-harness
accountable: A00
human_gates: [reader, developmental-edit, domain-review, line-edit, copyedit, proofread, publishing]
canon: partial-author-baseline
---
# 집필 하네스 이후 통합 준비도 v0.1

## 종합 상태

| 영역 | 판정 | 다음 차단선 |
|---|---|---|
| 세계관·C0 설정집 | design-complete candidate | 분야 인간 검토·정본 승격 |
| 7부제·117장·234장면 | design-complete | 작품별 원고 승인 |
| 200화 지도 | candidate-production-map | 실제 원고 분량·플랫폼 검토 |
| 집필 하네스 | complete-harness-package | 작품별 적용 |
| 첫 부제작 초고 | draft-complete | 인간 독자·편집 |
| 첫 부제작 28화 브리프 | candidate-complete | 실제 화 분량·낭독 |
| 첫 부제작 리뷰본 | human-review-ready | 발달·분야·라인·카피·교정쇄 |
| 부제작 2~7 원고 | blocked | 작품별 명시적 승인 |
| 편집 원고 | blocked | 인간 편집 결과 반영 |
| 출판 완성본 | blocked | 교정쇄·플랫폼·계약·작가 승인 |

## 작문 기준

- `단문 금지`가 아니라 `단문 남발 금지`
- 중단문·짧은 복문 중심의 가변 리듬
- 액션은 공간·궤적·저항·결과·비용·새 위치를 갱신
- 풍경은 방향·구별 디테일·변화의 3층
- 웹소설 화는 약속·진전·보상·추진 중 최소 3개
- 특정 작가 문체 모사 금지

## 계층

`공유세계관 → 메인 사가 → 대형막 → 부제작 → 내부막 → 시퀀스/서브액트 → 장 → 연재 화 → 장면 → 비트`

대형막은 여러 부제작의 비용을 합산해 비가역 전환을 만든다. 부제작은 현재 사건과 감정 질문을 독립적으로 닫는다.

## 맥거핀·회수

활성 원장:
`story/40-ledgers/foreshadowing-mystery-payoff-ledger-v0.2.md`

- M-01: 잘못 분류된 도감·분산 부담 기록
- M-02: 돌림패·우선 연결권
- M-03: P-17 보호 기록
- Q0~Q7 질문 사다리
- F-001~F-015 회수 부채
- P-17은 검증 가능한 비공개로 현재 사가 안에서 완결

## 첫 부제작 적용

- 15장·30장면·28화
- v0.3 패치 매니페스트와 결정적 빌더
- 문장·문단 기계적 패턴 감사기
- 새 영문 이름 잔재 수정
- 장면 카드 매핑 편차 수정
- 최신 판정: `human-review-ready / edited-manuscript 아님`

## 로컬 실행 제한

현재 세션 컨테이너에는 gh CLI가 없고 외부 DNS가 차단돼 빌더·문체 감사기를 실제 저장소에서 실행하지 못했다. 패치 원문 존재는 GitHub 커넥터로 확인했으며, 실행 가능한 개발/CI 환경에서 실제 명령을 수행해야 한다.

## 다음 실제 작업

1. v0.3 빌드·문체 감사 실행
2. 첫 부제작 작가 완독
3. 10~15세·성인 베타 테스트
4. 발달편집
5. 분야 검토
6. 라인·카피 편집
7. 교정쇄·플랫폼·출판 검토
8. 부제작 2 원고 승인 시 동일 하네스 적용
