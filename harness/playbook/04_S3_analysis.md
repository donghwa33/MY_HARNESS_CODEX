# 04. S3 분석과 UI (65–115분)

스킬: harness/skills/stratify-analysis/SKILL.md
모든 프롬프트 앞: `AGENTS.md 와 stratify-analysis 스킬을 따른다. 숫자는 src/analyze.py 로 계산해 outputs/ 에 저장하고 문서에는 출처를 단다.`

| # | 분석 | 시간 | 산출 |
|---|---|---|---|
| 1 | 시계열 + 이벤트 | 65–70 | trend_daily.csv, fig_trend.png |
| 2 | 측정 효과 분리 (2가지 방법) | 70–77 | measure_*.csv, D-번호 |
| 3 | 가설 요인 교차 층화 | 77–83 | strat_main.csv |
| 4 | 교란 확인 | 83–86 | dispatch_crosstab.csv |
| 5 | 독립 근거 (공간·시간·타 제품) | 86–92 | radial_by_group.csv, fig_radial.png |
| 6 | 기여 분해 + 구간 | 92–100 | waterfall.csv, fig_waterfall.png |
| 7 | (UI 필요 시) 화면 | 100–112 | ui/app.py 또는 ui/server.py |
| 8 | FINDINGS·EXPLAIN 정리, 커밋 | 112–115 | |

## 1. 시계열
```
trend() 를 추가하라. <대상> 의 단위 평균을 일별로 계산해 trend_daily.csv 로 저장하고,
이벤트 <날짜·라벨 목록> 과 <측정 조건 변경일: 데이터에서 자동 탐지> 를 겹쳐 fig_trend.png 로 그려라.
기준 기간과 이후 기간의 평균·차이·단위 수를 period_compare 로. 하락이 계단형인지, 계단이 몇 개인지만 말하라.
```
## 2. 측정 효과
```
measurement_effect() 를 추가하라. 측정 조건별 세부 불량 항목(Bin 등) 비율을 비교하고, 급증 항목이 모든 그룹에서 증가했는지 확인하라.
보정 두 가지를 모두 계산하라: (a) 해당 항목 제외 (b) 영향 없는 대조군의 전후 차이를 측정 효과로 추정. 선택은 내가 한다.
```
## 3. 층화
```
stratify_main() 을 추가하라. 기간: <이후>, 값: <보정 후 값>, 단위: <Lot>, 요인: <가설 요인 A>, <가설 요인 B>.
셀별 평균·중앙값·단위 수·기준 대비 차이를 strat_main.csv 로. 단위 수 10 미만 표시. 이 표만 보고 각 가설을 지지/반박 한 줄씩 판정하라.
```
## 4. 교란
```
confounding_check() 를 추가하라. 요인 교차 빈도표(dispatch_crosstab.csv)와 naive_vs_stratified 결과를 비교해, 단순 비교가 층화와 다르게 보이는 이유를 설명하라.
```
## 5. 독립 근거
```
spatial_pattern() 을 추가하라. 좌표 데이터가 있으면 radial_profile 로 그룹별 반경 구간 통과율과 주 불량 항목을 계산·그림. 없으면 다른 제품·시간 패턴으로 대체.
```
메커니즘 해석 문장은 사람이 직접 쓴다.
## 6. 기여 분해
```
decompose() 를 추가하라. 전체 변화 = 측정 효과 + 주요인 효과 + 잔차. waterfall 로 표·그림, 주요인 효과에 bootstrap_diff 구간. 가법 가정과 잔차의 의미를 표 아래 주석으로.
```
## 7. UI (README·AGREEMENT 에 화면·도구가 있을 때)
```
harness/scaffold/ui/streamlit_app_template.py 를 ui/app.py 로 복사하고 SECTIONS 를 outputs/ 의 실제 표·그림 이름에 맞춰라.
UI 에서 계산하지 마라. tests/test_ui_smoke.py 를 smoke_test_template.py 로 만들어 실행하라.
```
- API·특정 동작이 필요하면 fastapi_app_template.py + static/ 사용.
- 서버(터미널 T3): `streamlit run ui/app.py --server.address 0.0.0.0 --server.port 8501 --server.headless true`
- Browser 도구: PORT=8501, URL=/ → 기능 직접 확인 → REVIEW.md 미리보기 기록표.
- 안 열리면: 터미널 오류 → 실제 포트 → 0.0.0.0 → 경로 순서로 점검.

## 8. 정리
```
FINDINGS.md 에 F-번호로 정리하고, 핵심 발견마다 EXPLAIN.md 에 3줄을 추가하라. "어디서 틀릴 수 있나" 는 데이터·방법·가정 중 무엇이 약한지 구체적으로.
```
사람이 EXPLAIN 을 읽고 설명 못 하는 문장은 고치거나 지운다. 커밋 → STATE → HANDOFF #2.
