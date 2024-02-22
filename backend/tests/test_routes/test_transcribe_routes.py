import pytest
import websockets

@pytest.mark.asyncio
async def test_transcribe_ws():
    websocket_url = "ws://localhost:8000/api/v1/transcribe/transcribe_ws"
    async with websockets.connect(websocket_url) as ws:
        with open("backend/tests/assets/WhatsApp Ptt 2024-02-20 at 9.35.29 PM.wav", "rb") as f:
            audio = f.read()
            await ws.send(audio)
            response = await ws.recv()
            assert isinstance(response, str)
