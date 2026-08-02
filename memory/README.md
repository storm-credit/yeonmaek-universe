# Memory Protocol

`memory/`는 AI가 새 세션에서 복구해야 할 장기 맥락만 보관한다.

- `project-context.md`: 이미 확인된 의도와 제약
- `open-questions.md`: 아직 결정되지 않은 질문

세션 종료 전 새 결정, 거절된 방향, 다음 행동을 갱신한다. 임시 아이디어나 민감한 개인 정보는 저장하지 않는다.
