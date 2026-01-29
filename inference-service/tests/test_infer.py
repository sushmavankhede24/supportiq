from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_infer():
    payload = {
        "session_id": "test123",
        "intent": "billing",
        "messages": [{"role": "user", "content": "My payment failed"}],
    }

    response = client.post("/infer", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "reply" in data
    assert "confidence" in data
    assert "model_version" in data
