from pydantic import BaseModel

class PromptRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str