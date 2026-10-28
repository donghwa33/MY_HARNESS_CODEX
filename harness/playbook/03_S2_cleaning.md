# 03. S2 정제 (30–65분)

스킬: harness/skills/decision-log/SKILL.md

## 1. 정제 후보 목록 (30–37)
```
AGENTS.md 와 decision-log 스킬을 따른다. outputs/inventory.md 를 바탕으로 정제가 필요한 항목을 outputs/profile.md 에 표로 정리하라.
각 항목: 파일·열 / 문제 유형(포맷 혼재·표기 혼재·중복·범위 이탈·조인 실패·결측) / 영향 행 수와 예시 3개 / 처리 대안 2개 이상과 결과에 미치는 영향 방향.
처리는 하지 말고, 결정은 내가 한다. 날짜 슬래시 포맷이 있으면 infer_slash_order() 결과도 붙여라.
```

## 2. 자주 나오는 함정과 기본 결정
| 함정 | 기본 결정 | 확인 |
|---|---|---|
| 범주 표기 혼재 | normalize_categories 명시 매핑, 미등록 값은 에러 | 매핑 단위 테스트 |
| 날짜 포맷 혼재 | parse_dates_strict 허용 포맷 목록. 슬래시는 infer_slash_order 근거로 판정 | 파싱 후 기간 범위 검사 |
| 재측정·중복 행 | dedupe_keep (기준은 업무 담당자 진술) + 반대 기준을 민감도로 | 키 유일성 테스트 |
| 범위 이탈 | isolate_out_of_range 로 격리, 개수 보고 | 범위 테스트 |
| 조인 실패 | join_report 로 손실 키 격리, 비율 보고 | 손실 키 격리 테스트 |

## 3. 결정 기록 (37–40)
```
decision-log 스킬을 따른다. 아래 내 결정을 work/DECISIONS.md 에 D-번호로 기록하라. 대안·근거·영향·확인 방법을 채워라.
(결정 목록)
```

## 4. 구현과 테스트 (40–60)
```
work/DECISIONS.md 의 결정을 구현하는 src/clean.py 를 작성하라.
- analysis_utils 의 정제 함수를 쓰고, 결정마다 함수 하나, docstring 첫 줄에 D-번호.
- main(): data/raw → data/clean/<이름>_clean.csv, 단계별 행 수 변화 outputs/tables/cleaning_summary.csv, 격리 파일들.
- tests/test_clean.py 에 결정별 단위 테스트, tests/test_invariants.py 에 harness/scaffold/test_invariants_template.py 를 열 이름에 맞게 수정.
python -m pytest 실행. 실패하면 코드를 고치고, 테스트를 고쳐야 한다면 먼저 이유를 말하라.
```

## 5. 마무리 (60–65)
- 커밋 (가능하면 결정 단위): `[S2] D-002 날짜 월/일 판정`
- EXPLAIN 추가: `DECISIONS 에서 결과 영향이 큰 결정 2개를 EXPLAIN.md 에 E-번호로 (왜 / 어디서 틀릴 수 있나 / 다음 검증)`
- STATE 전환 감사 → HANDOFF #1 (07)
