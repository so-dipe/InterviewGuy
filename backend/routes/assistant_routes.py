from fastapi import APIRouter, HTTPException
from backend.assistant import gemini

router = APIRouter()

@router.post("/start")
def start_chat():
    try:
        chat = gemini.init()
        return {"chat": chat}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate")
def generate(prompt: str):
    try:
        response = gemini.generate_response(prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))