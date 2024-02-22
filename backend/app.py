from fastapi import FastAPI
from fastapi.websockets import WebSocket
from backend.logs.logging import get_logger
from backend.routes import assistant_routes, transcribe_routes

app = FastAPI()
LOG = get_logger(__name__)

app.include_router(assistant_routes.router, prefix="/api/v1/assistant", tags=["assistant"])
app.include_router(transcribe_routes.router, prefix="/api/v1/transcribe", tags=["transcribe"])

LOG.debug("Routes have been included.")

@app.get("/")
async def index():
    LOG.info("Welcome to Interview Guide API!")
    return {"message": "Welcome to Interview Guide API!"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Welcome to Interview Guide API!")
    await websocket.close()