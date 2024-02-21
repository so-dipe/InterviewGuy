from fastapi import FastAPI
from backend.routes import assistant_routes, transcribe_routes

app = FastAPI()

app.include_router(assistant_routes.router, prefix="/api/v1/assistant", tags=["assistant"])
app.include_router(transcribe_routes.router, prefix="/api/v1/transcribe", tags=["transcribe"])

@app.get("/")
def index():
    return {"message": "Welcome to Interview Guide API!"}
