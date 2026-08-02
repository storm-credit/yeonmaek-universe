---
status: c0-candidate-complete
issue: 62
scope: internal-c0-world-bible
canon_level: candidate-baseline
manuscript_lock: installment-01-v0.2-frozen-patch-queue-ready
reader_samples: complete-text-prototypes
---
# C0 내부 세계 설정집 통합 색인 v0.2

## 목적

작가·설계 에이전트가 세계 규칙, 역사, 기관, 학교, 생활, 생태, 유물, 영웅, 회랑, 7부제, 원고 영향과 인간 검토 상태를 한곳에서 추적하는 내부 설정집의 단일 진입점이다.

`C0`는 판매용 설정집이 아니다. candidate·provisional·deprecated·protected-private·human-review를 모두 포함한다.

## 현재 판정

| 영역 | 상태 |
|---|---|
| 핵심 세계 규칙 | candidate-complete |
| 학교·가족·도시 생활 | candidate-complete |
| 역사·협정·기관·지식 경계 | candidate-complete |
| 생물·유물·영웅·회랑 최소 카탈로그 | candidate-complete |
| 부제작 2~7 상세 설정 | detailed-setting-candidate |
| 첫 부제작 원고 역검증 | compatible-with-12-line-patch-queue |
| 독자용 도감·지도 텍스트 샘플 | complete-prototype |
| 인간·전문가 검토 | matrix-complete / reviews-pending |
| canon 승격 | author-and-expert-gates-pending |
| 부제작 2 원고 | blocked-until-author-gate-after-issue-62 |

# 1. 가장 먼저 읽을 문서

1. 핵심편: `world/00-core/c0-world-bible-core-compendium-v0.1.md`
2. 상태 인벤토리: `docs/decisions/world-bible-status-inventory-v0.1.md`
3. 열린 질문: `memory/open-questions-v0.2.md`
4. 완료 게이트: `docs/00-project/world-bible-completion-gate-v0.1.md`
5. 인간 검토: `reviews/world-bible/human-expert-review-matrix-v0.1.md`

# 2. 상태 체계

| 상태 | 의미 | 사용 |
|---|---|---|
| canon | 작가 승인과 필요한 검토 통과 | 정본·출판 후보 |
| candidate | 현재 1순위 작업 기준선 | 설계·초고·테스트 가능 |
| provisional | 지역·사례·감수 부족 | 구조 참고, 구체 묘사 제한 |
| open | 다음 결정을 실제로 막음 | 임의 확정 금지 |
| deprecated | 사용 중지, 이력 보존 | 신규 사용 금지 |
| superseded | 최신 문서가 대체 | 영향 추적만 |
| protected-private | 권리·안전 때문에 의도적 비공개 | 일반 공개 금지 |
| human-review | 법률·문화·안전·상표·출판 검토 필요 | 검토 전 canon 금지 |

# 3. 세계 법칙

## 기준 문서

- `world/00-core/minimum-worldbuilding-baseline-v0.1.md`
- `world/00-core/world-rules-failure-recovery-ledger-v0.1.md`
- `docs/decisions/installment1-world-bible-clarifications-v0.1.md`
- 테스트: `tests/world-bible/world-rules-case-scenarios-v0.1.md`

## 핵심

- 하나의 현실·복수 생태 위상
- 장소·상태·관계 조건 중 둘 이상 필요
- 물질·시간·부상·결과 보존
- 기록·감각·센서 불일치 가능, 물리적 시간여행 아님
- 공통 마나 생성이 아닌 결합 조율
- 신체·장소·생태·도구·관계·시간·법적 책임의 부담 보존
- 출력보다 관측·중지·인계·복구·정정 중심 성장
- 위험과 권리 분리, 거부·철회·비공개 가능
- 학생·학교·현실기관·당사자·감사의 권한 분산

# 4. 학교·가족·생활

## 기준 문서

- `world/40-institutions/korea-school-life-operations-bible-v0.1.md`
- `docs/decisions/surface-school-legal-form-candidate-v0.1.md`
- `world/40-institutions/school-badges-skills-equipment-catalog-v0.1.md`
- 테스트: `tests/world-bible/school-life-operation-scenarios-v0.1.md`

## 핵심

- 인가 중·고등학교+별도 현장교육센터 candidate
- 일반 교과·학적·상담·진급·졸업 유지
- 통학 기본+선택 기숙+계절 학단
- 관측·자기 안정·안전·생태 권리·부담 복구·제도 책임 교육
- 학생은 관찰·기록·신고·중지·제한 보조 가능
- 시설·교통·구조·의료·수사 최종권한은 성인 현실 전문기관
- 보호자·학생 단계별 동의·철회
- 건강·장애·경제·가정 조건에 대체 역할과 지원
- 사건 없는 급식·수업·동아리·친구·가족·일반 진로 유지

# 5. 역사·기관·국제 질서

## 기준 문서

- `world/30-history/history-agreements-institutions-knowledge-boundary-v0.1.md`
- 테스트: `tests/world-bible/history-institutions-knowledge-scenarios-v0.1.md`

## 핵심

- 단일 고대 비밀제국·세계정부 없음
- 지역 관계 관행→시설 충돌→분절 대응→전문화→디지털 불일치→후발 국제 조정
- 현실 전쟁·식민지배·재난·신앙을 심층 세계의 원인으로 대체하지 않음
- 국제망은 경보·검역 최소 기준·구조·기록 호환·통역·중재만 담당
- 공개 수준과 기관 권한 변화는 다음 작품에서 초기화되지 않음
- K0~K5 지식 경계는 접근 범위이지 신분 서열이 아님

# 6. 실제 수집 카탈로그

## 통합 색인

`world/60-companion/world-bible-collection-catalog-index-v0.1.md`

## 생물·동행 관계 12

`world/20-ecology/creature-relationship-catalog-v0.1.md`

여울띠, 모서리잠, 온기고리, 길눈, 물갈피, 뒤집잎, 빗마디, 문답결, 소리주머니, 마른물결, 숨돌, 빛바느질.

## 유물·도구·보물 8

`world/50-artifacts/artifact-tool-treasure-catalog-v0.1.md`

되짚등, 겹눈틀, 비움매듭, 반납열쇠, 멈춤종, 숨은추, 잔기록판, 돌림패.

## 영웅·탐사자·실패자 8

`world/30-history/hero-explorer-failure-record-catalog-v0.1.md`

윤서후, 한재목, 장리원, 민서림, 임해솔, 백도원, 세 차례 철회한 대표, 판본 사이의 통역자.

## 회랑·숨은 장소 10

`world/10-routes/corridor-hidden-place-catalog-v0.1.md`

서안 통학 회랑, 삼면계단, 유리온실 배수정원, 갈림물목, 서해 바람턱, 수문겹길, 환승그늘선, 마른물길 제8구간, 숨돌층 완충로, P-17 보호폐쇄구역.

## 보조 항목

- 행동 배지 8
- 공통 기술 10
- 장비 8

테스트: `tests/world-bible/collection-catalog-scenarios-v0.1.md`

# 7. 메인 사가·부제작

## 상위 기준

- `docs/decisions/seven-installment-saga-map-candidate-v0.1.md`
- `story/30-books/installments-02-07-setting-bible-index-v0.1.md`
- 4안 비교: `story/30-books/installments-02-07-setting-incident-options-v0.1.md`

| 부제작 | 중심 사건 | 상세 문서 | 상태 |
|---:|---|---|---|
| 1 | 잘못 분류된 통학 회랑 | 첫 부제작 패키지·v0.2 원고 | review-ready/frozen |
| 2 | 학교 경기·시설·철회 가능한 동행 | `installment2-protection-ownership-setting-bible-v0.1.md` | candidate |
| 3 | 하구 계절판·고정 복구·공동보관 | `installment3-different-koreas-setting-bible-v0.1.md` | provisional-region |
| 4 | 국제 검역·수문 운영·번역 권력 | `installment4-translation-border-setting-bible-v0.1.md` | provisional-region |
| 5 | 한국 환승생활권·영상·삭제 기록 | `installment5-records-disclosure-setting-bible-v0.1.md` | candidate |
| 6 | 중앙 조율망의 실제 성공 | `installment6-choice-monopoly-setting-bible-v0.1.md` | candidate |
| 7 | 복수 지역 행동·권한 만료·졸업 | `installment7-decision-co-governance-setting-bible-v0.1.md` | candidate |

통합 테스트: `tests/world-bible/installments-02-07-setting-scenarios-v0.1.md`

# 8. 첫 부제작 원고

## 최신본

`manuscript/installment-01/README.md`

## 역검증

- 감사: `reviews/world-bible/installment1-manuscript-world-bible-reverse-audit-v0.1.md`
- 테스트: `tests/world-bible/installment1-manuscript-reverse-audit-scenarios-v0.1.md`
- 명료화 결정: `docs/decisions/installment1-world-bible-clarifications-v0.1.md`

## 판정

- 사건·인물·결말 재설계 없음
- 12문장 국소 패치 큐
- 시간여행 오해·시설/센터 주체·`이동군` 공식용어만 조정
- #62 종료 전 실제 원고 파일은 동결

# 9. 독자용 설정집 샘플

## 정정되는 생태 도감 6항목

`publishing/samples/correcting-bestiary-six-card-sample-v0.1.md`

- 여울띠
- 모서리잠
- 온기고리
- 물갈피
- 문답결
- 숨돌

## 회랑 지도첩 4구역

`publishing/samples/corridor-atlas-four-zone-sample-v0.1.md`

- 서안 통학 회랑
- 삼면계단
- 갈림물목
- 수문겹길

## 테스트

`tests/world-bible/companion-reader-sample-scenarios-v0.1.md`

독자용 샘플은 본편 필수 해답을 독점하지 않으며 실제 출판·삽화 승인이 아니다.

# 10. 지역·문화·법률·출판 검토

## 기준

- `reviews/world-bible/human-expert-review-matrix-v0.1.md`
- 테스트: `tests/world-bible/human-review-matrix-scenarios-v0.1.md`

## 검토 대기

- 작가: 7부제·주인공 정체성·대표 수집 얼굴·최종 감정·제목
- 독자: 10~15세·성인·보호자 가독성·학교 매력·수집 인상
- 한국: 교육행정·학교안전·의료·보험·개인정보·도시시설
- 지역: 금강하구 복수 당사자 감수
- 해외: 태국어·방콕 수계·주민·기관·문화 감수
- 전문: 생태권리·연구윤리·언론·디지털 기록
- 출판: 제목·상표·분권·판형·삽화·접근성

# 11. 금지·보호

- 생물 포획·거래·희귀도·전투력 순위
- 유물 만능무기·상위호환
- 학교·한국·주인공의 세계 최종권한
- 실제 신앙·재난·피해·보호종의 수집품화
- 기억 삭제·허위 현실 기록 기본 은폐
- 학생의 구조·시설·의료·수사 지휘
- 해외 지역에서 한국팀의 최종 결정
- 민감 위치·자기명칭·미성년·의료·수사 기록 공개
- 후속작에서 하진의 독점 최종열쇠 복구

# 12. 다음 게이트

- #63 상태 인벤토리 최종 정리
- #72 전체 완성도 종료 테스트
- #62 작가 승인 전 candidate 완료 판정

# 13. #62 종료 기준 상태

- 사례로 작동하는 세계 규칙: 충족
- 6년 학교·가족·생활 운영: 충족
- 실제 생물·유물·영웅·회랑 최소 세트: 충족
- 부제작 2~7 고유 사건 직전 설정: 충족
- 인간 검토 상태와 후퇴안: 충족
- 첫 원고 양방향 연속성: 충족, 12문장 패치 대기
- C0 단일 색인·핵심편·독자 샘플: 충족
- 최종 통합 테스트: #72 대기
