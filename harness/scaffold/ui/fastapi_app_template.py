"""FastAPI + 정적 HTML UI 템플릿 — 과제가 API·특정 화면 동작을 요구할 때 사용.

복사: cp harness/scaffold/ui/fastapi_app_template.py ui/server.py
      cp -r harness/scaffold/ui/static ui/static
실행: python -m uvicorn ui.server:app --host 0.0.0.0 --port 8000
미리보기: Browser 도구에서 PORT=8000, URL=/
원칙: 계산은 src/analyze.py 가 한다. 이 서버는 outputs/ 의 결과를 전달만 한다.
"""
import os

import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

TABLE_DIR = os.path.join("outputs", "tables")
FIG_DIR = os.path.join("outputs", "figures")
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

app = FastAPI(title="analysis-ui")


def _safe(name: str) -> str:
    if not name.replace("_", "").replace("-", "").isalnum():
        raise HTTPException(400, "잘못된 이름")
    return name


@app.get("/api/health")
def health():
    return {"ok": True}


@app.get("/api/tables")
def list_tables():
    if not os.path.isdir(TABLE_DIR):
        return []
    return sorted(f[:-4] for f in os.listdir(TABLE_DIR) if f.endswith(".csv"))


@app.get("/api/tables/{name}")
def get_table(name: str):
    path = os.path.join(TABLE_DIR, f"{_safe(name)}.csv")
    if not os.path.exists(path):
        raise HTTPException(404, f"표 없음: {name}")
    df = pd.read_csv(path)
    return {"name": name, "source": path, "columns": list(df.columns),
            "rows": df.astype(object).where(df.notna(), None).values.tolist()}


@app.get("/api/figures/{name}")
def get_figure(name: str):
    path = os.path.join(FIG_DIR, f"{_safe(name)}.png")
    if not os.path.exists(path):
        raise HTTPException(404, f"그림 없음: {name}")
    return FileResponse(path, media_type="image/png")


app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")
