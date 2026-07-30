---
status: active
source_decision: D-058
migration_mode: semantic-first-path-later
---
# `권·book·시리즈 길이` 용어 마이그레이션 목록 v0.1

## 목적

기존 저장소의 `권`, `book`, `5권` 표현을 다음 계약에 맞게 정리한다.

- 메인 사가: 동일 주인공의 본편 전체
- 대형막: 여러 부제작을 묶는 성장 단계
- 부제작: 고유 부제를 가진 독립 장편
- 분권: 한 부제작을 나눈 물리적 책

파일 경로를 즉시 대량 변경하면 상호 링크와 이슈 추적이 끊길 수 있으므로 **의미를 먼저 바꾸고 경로는 나중에 일괄 마이그레이션**한다.

## 상태 분류

### A. 결정 상태 수정 완료

| 파일 | 기존 의미 | 현재 처리 |
|---|---|---|
| `docs/decisions/five-book-series-candidate-v0.1.md` | 본편 전체 5권 완결 | `reframing-required`, D-058로 대체 |
| `docs/decisions/long-growth-main-saga-candidate-v0.1.md` | 없음 | 7부제 2/3/2 구조 `candidate` |
| `CLAUDE.md` | 권·시즌·액트 혼용 가능 | 메인 사가·대형막·부제작·분권 계약 추가 |

### B. 역사 비교 문서로 보존

다음 문서는 삭제하지 않고 D-051 당시 비교와 검증 기록으로 보존한다.

- `story/00-series/series-length-architecture-options-v0.1.md`
- `story/00-series/series-length-options-v0.1.md`
- `tests/five-book-series-architecture-scenarios-v0.1.md`
- `reviews/five-book-series-architecture-red-team-v0.1.md`

처리 원칙:

- 문서 상단에 후속 작업에서 `historical / superseded by D-058` 표시
- 새 설계의 근거로 직접 인용할 때는 현재 후보가 아님을 명시
- 유효한 압축 리스크·회수 테스트는 새 7부제 테스트에 재사용

### C. `첫 부제작 후보`로 의미 전환

다음 파일의 `book1`, `book-1`, `1권`은 물리적 첫 책이 아니라 **첫 고유 부제작 후보**를 뜻하도록 바꾼다.

- `story/30-books/book-1-core-incident-options-v0.1.md`
- `story/30-books/book1-core-event-options-v0.1.md`
- `story/20-characters/book1-minimum-character-function-options-v0.1.md`
- `docs/decisions/book1-core-event-candidate-v0.1.md`
- `docs/decisions/book1-character-function-candidate-v0.1.md`
- `tests/book1-core-event-scenarios-v0.1.md`
- `tests/book1-character-function-scenarios-v0.1.md`
- `reviews/book1-core-event-red-team-v0.1.md`
- `reviews/book1-character-function-red-team-v0.1.md`

처리 원칙:

- 본문 용어를 `첫 부제작`으로 통일
- 파일 경로는 일괄 링크 갱신 전까지 유지
- 첫 부제작의 실제 분권 수를 암시하지 않음
- D-058의 대형막 I과 연결

### D. `권별`을 `부제작별`로 전환

다음 유형의 활성 문서에서 의미상 `권별` 표현을 검색·교체한다.

- 시리즈 아키텍처
- 복선·질문·회수 원장
- 캐릭터 관계 변화
- 수집축 공개 예산
- 학교 반복 루프
- 해외 지역 배치

단, 출판·서점·한국판 분권을 실제로 말하는 문맥은 `분권`으로 전환한다.

### E. 경로 이름의 `books` 처리

`story/30-books/`는 당장 이름을 바꾸지 않는다.

이유:

- 현재 PR의 상호 링크가 다수 연결됨
- GitHub contents API에서 경로 변경은 생성+삭제로 기록돼 추적 노이즈가 큼
- 첫 부제작 전체 지도가 완성되기 전 새 디렉터리 구조를 고정하면 다시 변경될 가능성이 있음

후속 후보:

- `story/30-installments/`
- `story/30-titled-works/`
- 한국어 문서 표기는 `부제작`

경로 후보는 저장소 구조 4안 비교 후 선택한다.

## 마이그레이션 순서

1. D-058과 CLAUDE 용어 계약 고정 — 완료
2. 모호한 파일 목록 작성 — 완료
3. 역사 문서 상단에 superseded 상태 추가
4. 첫 부제작 관련 본문 용어 변경
5. 새 7부제 전체 지도가 완성된 뒤 경로 구조 4안 비교
6. 새 경로 파일 생성과 링크 일괄 갱신
7. 기존 경로는 deprecated 안내 파일로 일정 기간 보존
8. P09/N16 교차 검증

## 완료 판정

현재 Gate B의 의미 마이그레이션 계획은 완료다. 실제 경로 이동은 Gate E의 일곱 부제작 전체 지도 뒤에 수행한다.

이는 미완료가 아니라 **의도된 지연**이다. 서사 계층이 정해지기 전에 경로를 먼저 고정하지 않는다.
