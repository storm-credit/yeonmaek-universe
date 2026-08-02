---
status: resolved-by-source-verification-pending-runtime
area: manuscript-harness
impact: no-repository-content-loss
---
# 로컬 하네스 실행 환경 제한 편차 v0.1

## 발생

완성본 하네스 구축 뒤 v0.3 빌더와 문체 감사기를 현재 작업 컨테이너에서 실행하려 했다.

## 실패 1

- 명령: `gh auth status`와 `gh repo clone`
- 결과: `gh` CLI가 설치돼 있지 않아 실행 불가
- 저장소 변경: 없음

## 실패 2

- 대체: 일반 `git clone` HTTPS
- 결과: 컨테이너의 외부 DNS 접근 차단으로 `github.com` 해석 실패
- 저장소 변경: 없음

## 대체 검증

- GitHub 커넥터로 v0.3 패치 대상 최신 장을 직접 읽음
- P01~P12 원문이 각 대상 파일에 존재함을 확인
- 패치 매니페스트는 각 원문이 정확히 한 번 일치하지 않으면 안전 실패하도록 설계
- 빌드·감사 실제 실행은 저장소 접근 가능한 개발/CI 환경에서 수행하도록 명령 기록

## 영향

- 하네스 설계와 소스 파일 작성에는 영향 없음
- 실제 런타임 실행 성공을 주장하지 않음
- 첫 부제작의 인간 검토 전 `build_installment1_v03.py`와 `audit_manuscript_style.py` 실행 필요

## 재발 방지

- 도구 존재와 네트워크 접근을 실행 전에 확인
- 실행 불가 시 저장소 변경 성공과 로컬 실행 성공을 분리 보고
- 검색 결과 0건 또는 코드 작성만으로 런타임 통과를 선언하지 않음
