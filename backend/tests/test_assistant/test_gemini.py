from backend.assistant.gemini import generate_response, init
from vertexai.preview import generative_models

def test_generate_response():
    response = generate_response("Hello")
    assert isinstance(response, str)

def test_init():
    chat = init()
    assert isinstance(chat, generative_models.ChatSession)