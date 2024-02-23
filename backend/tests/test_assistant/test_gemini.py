from backend.assistant import gemini
from vertexai.preview.generative_models import ChatSession

def test_init_chat():
    chat = gemini.init_chat()
    assert chat is not None

def test_generate_response():
    response = gemini.generate_response("Hello, how are you?")
    assert isinstance(response, str)

def test_generate_chat_response():
    chat = gemini.init_chat()
    response = gemini.generate_chat_response(chat, "Hello, how are you?")
    assert isinstance(response, str)