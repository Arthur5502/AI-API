from fastapi import APIRouter, HTTPException, status
from . import services, schemas

router = APIRouter()

@router.post("/chat", response_model=schemas.ChatResponse)
async def handle_chat(request: schemas.PromptRequest):
    try:
        ai_reply = await services.get_ai_response(request.message)
        
        return schemas.ChatResponse(reply=ai_reply)

    except ConnectionError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(e)
        )
    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )