---
status: resolved
related_issue: 50
related_pr: 1
---
# 준비도 파일·PR 갱신 오류 편차 로그 v0.1

## 원래 계획

1. `story/00-series/main-saga-readiness-matrix-v0.1.md`에 후속 부제작을 현재 장면 수준까지 고정하지 않는 이유를 추가한다.
2. 쓰기 실패와 복구 절차를 편차 로그로 남긴다.
3. PR #1의 제목과 설명을 현재 7부제·첫 부제작 준비도에 맞게 갱신한다.

## 실제 편차

### 편차 A — 파일 SHA 종류 혼동

첫 갱신 호출에서 파일 콘텐츠 SHA가 아니라 파일을 만든 커밋 SHA를 사용해 GitHub가 409 충돌로 쓰기를 거부했다.

### 편차 B — 새 로그에 갱신 도구 사용

새 편차 로그 경로에 `create_file` 대신 `update_file`을 호출해 필수 `sha`가 없다는 스키마 검증 오류가 발생했다.

### 편차 C — 같은 저장소 PR에 fork 옵션 사용

PR 설명 갱신 호출에서 `maintainer_can_modify=true`를 함께 보내 GitHub가 `Fork collab can only be enabled on cross-repo pull requests` 422 오류로 거부했다.

세 호출 모두 저장소·PR 내용을 변경하지 않은 안전한 실패였다.

## 발견 위치

통합 감사 종료 후 준비도 매트릭스 보강, 편차 기록, PR 설명 갱신 단계.

## 원인

- GitHub Contents API의 `sha` 필드는 현재 파일 blob/content SHA를 요구하지만 생성 결과의 `commit_sha`를 전달했다.
- 새 파일과 기존 파일의 쓰기 도구를 혼동했다.
- 같은 저장소 PR에는 fork 협업 옵션을 적용할 수 없는데 불필요한 옵션을 전달했다.

## 영향받는 항목

- 문서: `story/00-series/main-saga-readiness-matrix-v0.1.md`
- PR: #1 설명 갱신 1회 지연
- 정본·복선·인물·지역: 영향 없음
- 브랜치 내용 손실: 없음
- 강제 덮어쓰기: 없음

## 복구

1. 최신 파일을 다시 읽어 콘텐츠 SHA를 확인했다.
2. 확인한 파일 SHA로 동일 변경을 정상 적용했다.
3. 편차 로그는 `create_file`로 생성했다.
4. PR 갱신에서 `maintainer_can_modify` 옵션을 제거해 제목과 본문을 정상 적용했다.

## 재발 방지

- 새 파일 생성 결과의 `commit_sha`를 후속 `update_file`의 파일 SHA로 사용하지 않는다.
- 기존 파일 변경 전 `fetch_file`에서 반환된 `sha`를 사용한다.
- 새 경로는 `create_file`, 기존 경로는 `update_file`로 구분한다.
- 같은 저장소 PR 갱신에는 fork 전용 옵션을 넣지 않는다.
- 쓰기 충돌·검증 실패 시 강제 덮어쓰지 않고 최신 상태와 스키마를 다시 읽는다.

## 종료 상태

resolved
