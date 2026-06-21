class AIService:
    def __init__(self, client=None):
        self.client = client

    async def summarize(self, text: str):
        if not text:
            raise ValueError("Text cannot be empty")

        words = text.split()

        return {
            "summary": text[:50] + "...",
            "word_count": len(words),
            "model": "mock-ai-v1"
        }