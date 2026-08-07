# 공식 이야기 계층 매핑

상태: P0 운영 매핑
기준일: 2026-08-08

## 1. 목적

기존 5부·15 Act·45 Subact·90장 설계를 삭제하거나 재작성하지 않고 공식 7계층에 연결한다.

## 2. 계층 대응

| 공식 계층 | 기존 자산 | 수량 | 주 참조 |
|---|---:|---:|---|
| Series | 《겹길의 아이들》 전체 | 1 | `story/00-series/`, `story/10-blueprint/` |
| Grand Act | 기존 5부 | 5 | `story/20-structure/five-part-act-sequence-blueprint-v0.1.md` |
| Volume Act | 각 부의 3 Act | 15 | 같은 파일, `story/25-subacts/` |
| Arc | Volume Act별 기능성 Arc 래퍼 | 15 | 이 문서가 최초 매핑 원장 |
| Subact | 기존 45 Subact | 45 | `story/25-subacts/part*-nine-subacts-v1.0.md` |
| Episode | 기존 90장 | 90 | `story/30-chapter-functions/`, `story/60-scene-beats/` |
| Scene | 장별 씬 비트와 실제 장면 | 가변 | `story/50-scene-plans/`, `story/60-scene-beats/`, 원고 |

## 3. Arc 래퍼 규칙

초기 Arc는 Volume Act와 1:1 대응하지만 역할이 다르다.

- Volume Act: 막의 약속, 상승, 중간 성공/저점, 재설계, 막 종료를 관리한다.
- Arc: 그 막 안의 세 Subact를 관통하는 국소 변화, 관계 이동, 정보 흐름, Anti-Repeat를 관리한다.
- Arc는 새 사건을 자동 생성하지 않는다.
- Arc 분할·병합은 기존 45 Subact·90장 대응을 바꾸지 않는 범위에서만 가능하며 Decision Log가 필요하다.

식별자 예:
- `SER-01`
- `GA-01`~`GA-05`
- `VA-01-01`~`VA-05-03`
- `ARC-01-01`~`ARC-05-03`
- `SA-01-01-01`~`SA-05-03-03`
- `EP-001`~`EP-090`
- `SC-EP001-01` 형식

## 4. 계층 공통 필드

모든 계층은 다음을 기록한다.

1. Promise
2. Goal
3. Opposition
4. Choice
5. Cost
6. Revelation
7. Reward
8. Loss
9. State Change
10. Next Cause
11. Anti-Repeat

기존 문서의 `시작 상태`, `중심 갈등`, `핵심 사건`, `중간 반전`, `선택`, `비용`, `관계 변화`, `종료 전환`은 위 필드로 옮길 수 있으나, 근거가 없는 Reward·Loss·Anti-Repeat를 새로 발명하지 않는다.

## 5. 기존 구조의 보존 판정

- 5부: 보존
- 15 Act: 보존
- 45 Subact: 보존
- 90장: 보존
- 장별 씬 비트: 보존
- `story/25-subacts/` 파일명: 내부 구조와 일치하므로 변경 없음
- 기존 Sequence: 역사적 설계 근거로 보존하되 공식 실행 계층은 Arc/Subact를 사용

## 6. 현재 공백

기존 Subact 문서는 대체로 갈등·사건·비용·전환을 가지지만, 모든 단위에 Promise·Choice·Reward·Loss·Next Cause·Anti-Repeat가 명시되어 있지는 않다. 이 공백은 `WORLD_GAP_LEDGER`의 구조 항목으로 추적하며, 신규 원고 잠금 해제 전 보강한다.
