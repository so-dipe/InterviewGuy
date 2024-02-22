import pytest
import websockets
from httpx import AsyncClient
from backend import app

@pytest.mark.asyncio
async def test_index():
    async with AsyncClient(app=app.app, base_url="http://test") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to Interview Guide API!"}

@pytest.mark.asyncio
async def test_websocket_endpoint():
    async with websockets.connect("ws://localhost:8000/ws") as ws:
        response = await ws.recv()
        assert response == "Welcome to Interview Guide API!"


    