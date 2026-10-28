"""UI 스모크 테스트 템플릿. tests/test_ui_smoke.py 로 복사해 쓴다.
FastAPI: TestClient 로 엔드포인트 확인. Streamlit: 앱 스크립트가 예외 없이 실행되는지 AppTest 로 확인.
"""
import os

import pytest

USE = "streamlit"   # "streamlit" 또는 "fastapi"


@pytest.mark.skipif(USE != "fastapi", reason="FastAPI 미사용")
def test_fastapi_endpoints():
    from fastapi.testclient import TestClient
    from ui.server import app

    c = TestClient(app)
    assert c.get("/api/health").json() == {"ok": True}
    names = c.get("/api/tables").json()
    if names:
        assert c.get(f"/api/tables/{names[0]}").status_code == 200
    assert c.get("/").status_code == 200


@pytest.mark.skipif(USE != "streamlit" or not os.path.exists("ui/app.py"), reason="Streamlit 미사용")
def test_streamlit_runs():
    from streamlit.testing.v1 import AppTest

    at = AppTest.from_file(os.path.abspath("ui/app.py"), default_timeout=30).run()
    assert not at.exception
