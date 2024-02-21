import pytest
from backend.speech_to_text.google_speech import google

@pytest.mark.asyncio
async def test_transcribe():
    with open("WhatsApp Ptt 2024-02-20 at 9.35.29 PM.wav", "rb") as f:
        audio = f.read()
    response = await google.transcribe(audio)
    assert isinstance(response, str)
    