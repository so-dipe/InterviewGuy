from fastapi import APIRouter, HTTPException, WebSocket
from backend.speech_to_text.google_speech import google
from backend.logs.logging import get_logger

router = APIRouter()

LOG = get_logger(__name__)

@router.post("/transcribe")
def transcribe_audio(audio : bytes):
    try:
        text = google.transcribe(audio)
        return {"transcription": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.websocket("/transcribe_ws")
async def transcribe_ws(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_bytes()
            text = await google.transcribe(data)
            await websocket.send_text(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


