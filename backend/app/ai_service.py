class AIService:
    def __init__(self, client=None):
        # client is injected — use a real LLM client or a mock in tests
        self.client = client

    def summarize(self, text: str) -> dict:
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")

        if len(text) > 10_000:
            raise ValueError("Text exceeds maximum length of 10,000 characters")

        response = self.client.complete(prompt=f"Summarize this text:\n\n{text}")

        return {
            "summary": response["content"],
            "word_count": len(text.split()),
            "model": response["model"],
        }
