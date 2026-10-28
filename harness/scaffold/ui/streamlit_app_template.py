"""Streamlit UI 템플릿 — 분석 코어의 결과만 표시한다 (UI 에서 계산 금지).

복사: cp harness/scaffold/ui/streamlit_app_template.py ui/app.py
실행: streamlit run ui/app.py --server.address 0.0.0.0 --server.port 8501 --server.headless true
미리보기: Browser 도구에서 PORT=8501, URL=/

화면 구성(SECTIONS)만 과제에 맞게 고친다. 표·그림 파일은 src/analyze.py 가 만든 것을 그대로 쓴다.
"""
import os

import pandas as pd
import streamlit as st

TABLE_DIR = os.path.join("outputs", "tables")
FIG_DIR = os.path.join("outputs", "figures")

TITLE = "분석 결과"
SUMMARY_FILE = "REPORT.md"   # 결론 요약으로 보여줄 문서 (없으면 생략)

# (섹션 제목, 표 이름 또는 None, 그림 이름 또는 None, 설명)
SECTIONS = [
    ("1. 추이", "trend_daily", "fig_trend", "일별 평균과 이벤트 시점"),
    ("2. 요인별 비교", "strat_main", None, "요인 교차 셀별 평균과 단위 수"),
    ("3. 교란 확인", "dispatch_crosstab", None, "요인 간 배정 쏠림"),
    ("4. 공간 패턴", "radial_by_group", "fig_radial", "중심~가장자리 통과율"),
    ("5. 기여 분해", "waterfall", "fig_waterfall", "하락분의 요인별 기여"),
]

st.set_page_config(page_title=TITLE, layout="wide")
st.title(TITLE)

if os.path.exists(SUMMARY_FILE):
    with st.expander("요약 보고서", expanded=True):
        st.markdown(open(SUMMARY_FILE, encoding="utf-8").read())

for title, table, fig, desc in SECTIONS:
    st.header(title)
    st.caption(desc)
    if fig:
        path = os.path.join(FIG_DIR, f"{fig}.png")
        if os.path.exists(path):
            st.image(path)
        else:
            st.info(f"그림 없음: {path}")
    if table:
        path = os.path.join(TABLE_DIR, f"{table}.csv")
        if os.path.exists(path):
            df = pd.read_csv(path)
            st.dataframe(df, use_container_width=True)
            st.caption(f"출처: {path}")
        else:
            st.info(f"표 없음: {path}")
