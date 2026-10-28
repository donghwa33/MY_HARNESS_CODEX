# 07. Handoff

스킬: harness/skills/handoff/SKILL.md

| 시점 | 트리거 | 새 세션 첫 과제 |
|---|---|---|
| #1 (약 65분) | S2 완료 | S3 분석 |
| #2 (약 115분) | S3 완료 | S4 수정 반영 (+ 레드팀은 별도 새 세션) |
| #3 (약 165분) | 마감 | 없음 (인계 문서로 제출) |
| 예외 | 결정 재질문, D-번호와 다른 처리, 일반론 응답, 같은 파일 반복 읽기 | 이어서 진행 |

## 기존 세션
```
$handoff
```
(스킬 미인식 시) `harness/skills/handoff/SKILL.md 를 읽고 따라 work/HANDOFF.md 를 작성하고 커밋하라.`

## 새 세션 부팅 (T1 에서 `/new` 로 새 대화 시작. 안 되면 codex 종료 후 재실행)
```
AGENTS.md 를 따른다. work/HANDOFF.md, work/STATE.md, work/AGREEMENT.md, work/DECISIONS.md 를 이 순서로 읽어라.
그다음 세 줄만 답하라. 다른 작업은 하지 마라.
1) 현재 단계와 다음 행동
2) 지켜야 할 결정 중 결과에 가장 영향이 큰 2개 (D-번호)
3) 아직 열려 있는 질문
```
세 줄이 HANDOFF 와 일치하면 시작. 틀리면 지적하고 다시 읽게 한다.

## 주의
- 서버가 떠 있는 터미널(T3)은 세션 교대 때 닫지 않는다.
