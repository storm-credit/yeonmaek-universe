---
status: active-clean-inventory
scope: world-bible-and-blueprint-only
branch: canon/world-bible-blueprint-clean
supersedes: docs/decisions/world-bible-status-inventory-v0.1.md
canon: false
---
# 세계 설정집 상태 인벤토리 v0.2

## 1. 적용 범위

이 문서는 설정집·설계도 정리 브랜치의 현재 source-of-truth 상태를 기록한다.

포함:
- 세계 원리·힘·비용·실패·복구
- 생태·권리·기관·학교·지역
- 인물·메인 사가·부제작 구조 후보
- 장·장면 카드·화별 기능 후보
- 복선·연표·권한 구조

제외:
- 실제 소설 본문
- 원고 승인 기록
- 초고 완료·편집·독자 테스트 패키지
- 원고를 근거로 한 역감사

제외 자료는 `archive/full-saga-draft-unapproved`에 보존한다.

## 2. 상태 우선순위

1. 사용자가 현재 대화에서 명시한 의도
2. `docs/decisions/clean-branch-candidate-baseline-v0.1.md`
3. `docs/00-project/world-bible-clean-branch-status-v0.1.md`
4. 본 인벤토리
5. 세계관·사가·부제작별 candidate 문서
6. 테스트·레드팀·연구 자료
7. 원고 전환 이전의 오래된 결정
8. 원고 전환 이후 파생 문서

낮은 순위 문서가 높은 순위 문서와 충돌하면 낮은 순위 문서를 `superseded`, `archive-only`, `reframing-required` 중 하나로 처리한다.

## 3. 작품 정체성

| 항목 | 상태 | 기준 | 규칙 |
|---|---|---|---|
| 저장소 코드명 `연맥` | code-name | `CLAUDE.md` | 최종 제목 아님 |
| `겹길` 등 작업명 | candidate | 제목·첫 부제작 후보 문서 | 상표·독자 검토 전 확정 금지 |
| 핵심 독자 10~15세 | candidate-baseline | `CLAUDE.md` | 실제 독자 테스트 전 미검증 |
| 장기 성장형 | author-intent | `memory/project-context.md` | 동일 주인공 장기 성장 기능 유지 |
| 한국 홈베이스 | author-intent | `CLAUDE.md` | 학교·가족·도시 생활 지속 |
| 해리포터 참고 | functional-reference | `memory/project-context.md` | 학교·현실 연결·대표 경기 기능만 분석, 직접 복제 금지 |

## 4. 세계 법칙

| 항목 | 상태 | 기준 문서 | 남은 검토 |
|---|---|---|---|
| 다층 생태 위상 | candidate | `world/00-core/minimum-worldbuilding-baseline-v0.1.md` | 경계·실패 사례 |
| 장소·상태·관계 조건 | candidate | 동일 | 조합별 작동 예시 |
| 물질·결과 보존 | candidate | 동일 | 극단 사례 |
| 결합 조율 | candidate | `world/20-systems/power-system-architecture-v0.1.md` | 수련·도구·환경 세부 |
| 부담 보존 | candidate | `world/00-core/world-rules-failure-recovery-ledger-v0.1.md` | 이동·복구 사례 통합 |
| 성장 척도 | candidate | 학교·힘 체계 문서 | 학년·평가 구조 |

## 5. 생태·권리

| 항목 | 상태 | 기준 문서 | 남은 검토 |
|---|---|---|---|
| 지성 판정 | candidate | `world/20-systems/sentience-ecology-rights-options-v0.1.md` | 종별 사례 |
| 비소유·이동·동의·기록 통제 | candidate | 동일 | 국제 이동·검역 |
| 위험과 권리 분리 | candidate | 동일 | 격리·대표·분쟁 절차 |
| 여울띠 등 개별 종 | working-candidate | 부제작 1·생태 문서 | 최종 종명·생활사·외형 |

## 6. 현실 제도·학교

| 항목 | 상태 | 기준 문서 | 남은 검토 |
|---|---|---|---|
| 분산 이중관할 | candidate | `world/20-systems/secret-society-public-institutions-options-v0.1.md` | 사건별 공동지휘 |
| 기록·비밀 | candidate | `world/20-systems/hidden-world-interface-v0.1.md` | 법원·언론·보험 |
| 학교 법적 외형 | candidate+human-review | `world/30-korea/surface-school-legal-form-options-v0.1.md` | 교육행정·법률 |
| 학생 역할 | candidate | 학교 운영 설정집 | 학년별 자격·금지선 |
| 보호자 동의 | candidate | 학교 운영 설정집 | 재동의·철회·보상 |
| 통학·기숙 | candidate | 학교 생활 문서 | 시간표·비용·비율 |
| 대표 경기 | candidate | 경기 안전·관전 문서 | 재미·재현성·안전 검증 |

## 7. 역사·국제 질서

| 항목 | 상태 | 기준 문서 | 남은 검토 |
|---|---|---|---|
| 다중 협정망 | candidate | 역사·국제 질서 문서 | 대표 협정·연표 |
| 후발 국제 조정체 | candidate | 동일 | 가입·실패·권한 상한 |
| 한국 기관·재단 | working-candidate | 학교·기관 문서 | 창립사·예산·감사 |
| 공개 수준 누적 | candidate | 장기 사가 지도 | 주체별 지식 원장 |

## 8. 메인 사가

| 항목 | 상태 | 규칙 |
|---|---|---|
| 7부제 2/3/2 | candidate | 최종 승인값이 아니며 5권·7권·5+2안과 재비교 가능 |
| 주인공 만 12→18세 약 6년 | candidate | 학사·생일·방학 연표 검증 필요 |
| 서하진 | working-candidate | 이름·성별·가족·성격 모두 최종 canon 아님 |
| 부제작 1 | detailed-blueprint-candidate | 통학 회랑·학교 입문·생태 권리 설계 |
| 부제작 2 | detailed-blueprint-candidate | 학교 스포츠·보호와 소유 설계 |
| 부제작 3 | detailed-blueprint-candidate | 국내 수계·지역 판본 설계 |
| 부제작 4 | detailed-blueprint-candidate | 해외 수계·번역·검역 설계 |
| 부제작 5 | detailed-blueprint-candidate | 기록·공개·생활 피해 설계 |
| 부제작 6 | detailed-blueprint-candidate | 중앙 조율 성공·독점 위험 설계 |
| 부제작 7 | detailed-blueprint-candidate | 권한 분산·졸업·공동관리 설계 |

## 9. 분량·생산 구조

| 항목 | 상태 | 규칙 |
|---|---|---|
| 117장 | candidate-design-count | 상세 설계의 현재 합계일 뿐 고정 분량 아님 |
| 234장면 카드 | candidate-design-count | 장면 기능 카드이며 실제 원고 장면 수 아님 |
| 200화 | candidate-production-map | 플랫폼·실제 분량·작가 승인 전 고정 금지 |
| 물리적 분권 | publishing-candidate | 설계 단계에서 확정 금지 |

## 10. 수집 생태계

| 항목 | 상태 | 기준 |
|---|---|---|
| 생물·동행 | schema+catalog-candidate | 소유·거래·희귀도 중심 금지 |
| 도감 | schema-ready | 정정·판본·비공개·폐기 이력 중심 |
| 회랑 지도 | schema+catalog-candidate | 보호 폐쇄도 보상으로 인정 |
| 유물·도구 | catalog-candidate | 이력·부담·권리·보관 포함 |
| 영웅 기록 | catalog-candidate | 공식·지역·당사자 평가 병기 |
| 경기·배지·장비 | candidate | 전투력 점수화보다 판단·협력·복구 중심 |

## 11. 금지·격리 상태

| 대상 | 상태 | 처리 |
|---|---|---|
| `manuscript/**` | archive-only | 정리 브랜치 제외 |
| 원고 단계 승인 문서 | invalidated/archive-only | 사용자 명시 승인 근거 없음 |
| 원고 완료·제작 로드맵 | archive-only | 설정집 정본 근거로 사용 금지 |
| 원고 기반 독자 테스트 | archive-only | 실제 원고 승인 뒤 새로 설계 |
| 원고↔설정집 역감사 | archive-only | 설정집 자체 감사로 대체 |
| 단일 마법부·세계정부 | prohibited | 분산 관할 유지 |
| 생물 포획·희귀도·진화 트리 | prohibited | 관계·정정·반환 중심 |
| 기억 삭제·허위 기록 기본 은폐 | prohibited | 제한 기록·현실 결과 유지 |

## 12. 현재 남은 작업

1. 오래된 문서의 `author-approved`, `draft-complete`, `human-review-ready` 표기 전수 감사
2. 삭제된 원고 경로를 가리키는 링크 정리
3. 세계관 source-of-truth 문서 간 중복·모순 점검
4. 7부제·117장·200화가 사용자 목표에 적합한지 재평가
5. 주인공·학교·경기·수집 요소의 매력과 독창성 재검토
6. 연표·권한·지역·기관 통합 감사
7. 작가 검토용 최종 설정집 패키지 작성

현재 판정: `world-bible-assets-preserved / manuscript-contamination-removal-in-progress / no-reset`.
