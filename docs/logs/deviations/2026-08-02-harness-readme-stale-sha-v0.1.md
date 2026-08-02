---
status: resolved
area: manuscript-harness
impact: no-content-loss
---
# 하네스 편차 README 잘못된 SHA 호출 v0.1

## 발생

완성본 하네스 작업 뒤 편차 색인을 갱신하려다 `docs/logs/deviations/README.md`에 임시 SHA `FIXME`를 전달했다.

## 결과

- GitHub가 409 SHA 불일치로 요청을 차단함
- 기존 README 변경 없음
- 강제 덮어쓰기 없음
- 콘텐츠 손실 없음

## 후속 실수

별도 편차 파일을 만들려는 과정에서 새 경로에 `update_file`과 임시 값 `no-op`을 전달했고, 커넥터가 이를 새 파일 생성처럼 처리했다.

## 복구

- 생성된 `no-op` 파일의 실제 blob SHA를 다시 읽음
- 현재 문서로 즉시 정상 교체
- 불필요한 빈 파일이나 미완료 상태 없음

## 재발 방지

1. 기존 파일 갱신은 반드시 `fetch_file`의 실제 blob SHA 사용
2. 새 파일은 `create_file` 사용
3. 임시 SHA·임시 본문으로 쓰기 호출 금지
4. 커넥터 결과가 예상과 다르면 바로 파일을 읽어 실제 상태 확인
