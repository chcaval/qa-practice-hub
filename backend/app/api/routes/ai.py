from fastapi import APIRouter, Depends, HTTPException

from ...schemas.ai import SummarizeRequest, SummarizeResponse
from ...services.ai_service import AIService

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


def get_ai_service():
    return AIService()


@router.post(
    "/summarize",
    response_model=SummarizeResponse
)
async def summarize(
    payload: SummarizeRequest,
    ai_service: AIService = Depends(get_ai_service)
):
    try:
        summary = ai_service.summarize(payload.text)

        return SummarizeResponse(summary=summary)

    except ValueError as e:
        raise HTTPException(
            status_code=422,
            detail=str(e)
        )