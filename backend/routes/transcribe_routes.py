from fastapi import APIRouter, HTTPException
from backend.speech_to_text.google_speech import google

router = APIRouter()

@router.post("/transcribe")
def transcribe_audio(audio : bytes):
    try:
        text = google.transcribe(audio)
        return {"transcription": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))