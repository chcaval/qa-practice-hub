import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient

from app.main import app, get_ai_service
from backend.app.services.ai_service import AIService


def make_mock_ai(summary="Mocked summary.", model="mock-v1"):
    mock_client = MagicMock()
    mock_client.complete.return_value = {"content": summary, "model": model}
    return AIService(client=mock_client)


@pytest.fixture
def ai_client():
    """Client with mocked AI service injected."""
    app.dependency_overrides[get_ai_service] = lambda: make_mock_ai()
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


# --- Happy path ---

def test_summarize_returns_200(ai_client):
    response = ai_client.post("/ai/summarize", json={"text": "Some meaningful text here."})
    assert response.status_code == 200


def test_summarize_response_shape(ai_client):
    response = ai_client.post("/ai/summarize", json={"text": "Some meaningful text here."})
    data = response.json()
    assert "summary" in data
    assert "word_count" in data
    assert "model" in data


def test_summarize_summary_is_string(ai_client):
    response = ai_client.post("/ai/summarize", json={"text": "Some meaningful text here."})
    assert isinstance(response.json()["summary"], str)


def test_summarize_summary_is_not_empty(ai_client):
    response = ai_client.post("/ai/summarize", json={"text": "Some meaningful text here."})
    assert len(response.json()["summary"]) > 0


# --- AI output quality checks (non-determinism handled via mocks) ---

def test_summarize_output_does_not_contain_prompt_text():
    """Summary should not echo back the raw prompt instruction."""
    mock_ai = make_mock_ai(summary="This text talks about AI systems.")
    app.dependency_overrides[get_ai_service] = lambda: mock_ai
    with TestClient(app) as c:
        response = c.post("/ai/summarize", json={"text": "Some meaningful text here."})
    app.dependency_overrides.clear()
    assert "Summarize this text" not in response.json()["summary"]


def test_summarize_word_count_matches_input():
    mock_ai = make_mock_ai()
    app.dependency_overrides[get_ai_service] = lambda: mock_ai
    with TestClient(app) as c:
        response = c.post("/ai/summarize", json={"text": "one two three four"})
    app.dependency_overrides.clear()
    assert response.json()["word_count"] == 4


# --- Edge cases / failure modes ---

def test_summarize_empty_text_returns_422(ai_client):
    response = ai_client.post("/ai/summarize", json={"text": ""})
    assert response.status_code == 422


def test_summarize_whitespace_only_returns_422(ai_client):
    response = ai_client.post("/ai/summarize", json={"text": "     "})
    assert response.status_code == 422


def test_summarize_missing_text_field_returns_422(ai_client):
    response = ai_client.post("/ai/summarize", json={})
    assert response.status_code == 422


def test_summarize_text_too_long_returns_422(ai_client):
    long_text = "word " * 3000
    response = ai_client.post("/ai/summarize", json={"text": long_text})
    assert response.status_code == 422


# --- Model traceability ---

def test_summarize_response_includes_model_name():
    mock_ai = make_mock_ai(model="gpt-mock-4")
    app.dependency_overrides[get_ai_service] = lambda: mock_ai
    with TestClient(app) as c:
        response = c.post("/ai/summarize", json={"text": "Testing model traceability."})
    app.dependency_overrides.clear()
    assert response.json()["model"] == "gpt-mock-4"
