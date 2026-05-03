import pytest
from unittest.mock import MagicMock
from app.ai_service import AIService


@pytest.fixture
def mock_client():
    client = MagicMock()
    client.complete.return_value = {
        "content": "This is a concise summary.",
        "model": "mock-model-v1",
    }
    return client


@pytest.fixture
def ai_service(mock_client):
    return AIService(client=mock_client)


# --- Happy path ---

def test_summarize_returns_expected_fields(ai_service):
    result = ai_service.summarize("The quick brown fox jumps over the lazy dog.")
    assert "summary" in result
    assert "word_count" in result
    assert "model" in result


def test_summarize_word_count_is_accurate(ai_service):
    text = "one two three four five"
    result = ai_service.summarize(text)
    assert result["word_count"] == 5


def test_summarize_returns_model_name(ai_service):
    result = ai_service.summarize("Some text here.")
    assert result["model"] == "mock-model-v1"


def test_summarize_calls_client_once(ai_service, mock_client):
    ai_service.summarize("Some text here.")
    mock_client.complete.assert_called_once()


# --- Edge cases ---

def test_summarize_raises_on_empty_string(ai_service):
    with pytest.raises(ValueError, match="empty"):
        ai_service.summarize("")


def test_summarize_raises_on_whitespace_only(ai_service):
    with pytest.raises(ValueError, match="empty"):
        ai_service.summarize("   ")


def test_summarize_raises_on_text_too_long(ai_service):
    long_text = "word " * 3000  # ~15000 chars
    with pytest.raises(ValueError, match="maximum length"):
        ai_service.summarize(long_text)


# --- Parametrize: testing multiple inputs at once ---

@pytest.mark.parametrize("text,expected_words", [
    ("hello world", 2),
    ("one two three", 3),
    ("a b c d e f", 6),
])
def test_word_count_parametrized(ai_service, text, expected_words):
    result = ai_service.summarize(text)
    assert result["word_count"] == expected_words


def test_summarize_raises_runtime_error_on_client_failure(ai_service, mock_client):
    mock_client.complete.side_effect = Exception("network error")
    with pytest.raises(RuntimeError, match="unavailable"):
        ai_service.summarize("some text")
