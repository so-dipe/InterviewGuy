from fastapi import APIRouter, HTTPException
from backend.assistant import gemini
import pickle
from ..logs.logging import get_logger
from ..prompts.prompts import PROMPTS
import base64
from pydantic import BaseModel

LOG = get_logger(__name__)

class Conversation(BaseModel):
    chat_session: bytes
    message: str

class MessagesModel(BaseModel):
    messages: str

router = APIRouter()

@router.post("/conversation")
async def conversation(conversation: Conversation):
    message = conversation.message
    sys_prompt = PROMPTS.get("ASSISTANT")
    message = sys_prompt + message
    try:
        chat_session = base64.b64decode(conversation.chat_session)
        chat = pickle.loads(chat_session)
        chat = gemini.init_chat()
        response = gemini.generate_chat_response(chat, message)
    except Exception as e:
        LOG.error(f"Error generating chat response: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    return response

@router.post("/review")
async def review(messages: MessagesModel):
    messages = messages.messages
    sys_prompt = PROMPTS.get("REVIEWER")
    messages = sys_prompt + messages
    try:
        response = gemini.generate_response(messages)
    except Exception as e:
        LOG.error(f"Error generating response: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    return response

@router.post("/analysis")
async def analysis(messages: MessagesModel):
    messages = messages.messages
    sys_prompt = PROMPTS.get("ANALYST")
    messages = sys_prompt + messages
    try:
        response = gemini.generate_response(messages)
    except Exception as e:
        LOG.error(f"Error generating response: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    return response

@router.post("/autocomplete")
async def autocomplete(conversation: Conversation):
    message = conversation.message
    sys_prompt = PROMPTS.get("AUTOCOMPLETE")
    message = sys_prompt + message
    try:
        chat_session = base64.b64decode(conversation.chat_session)
        chat = pickle.loads(chat_session)
        response = gemini.generate_chat_response(chat, message)
    except Exception as e:
        LOG.error(f"Error generating response: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    return response