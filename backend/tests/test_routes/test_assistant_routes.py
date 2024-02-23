from fastapi.testclient import TestClient
from backend.routes.assistant_routes import router
from backend.assistant import gemini
import pickle
import base64

client = TestClient(app=router)

def test_conversation():
    chat = gemini.init_chat()
    chat_session = pickle.dumps(chat.history)
    chat_session = base64.b64encode(chat_session).decode("utf-8")
    response = client.post("/conversation", json={"chat_session": chat_session, "message": "Hello, how are you?"})
    assert response.status_code == 200
    assert isinstance(response.text, str)

def test_review():
    messages = "User1: Hello, how are you? User2: I'm doing well, how about you?"
    response = client.post("/review", json={"messages": messages})
    assert response.status_code == 200
    assert isinstance(response.text, str)

def test_analysis():
    messages = "User1: Hello, how are you? User2: I'm doing well, how about you?"
    response = client.post("/analysis", json={"messages": messages})
    assert response.status_code == 200
    assert isinstance(response.text, str)

def test_autocomplete():
    chat = gemini.init_chat()
    chat_session = pickle.dumps(chat.history)
    chat_session = base64.b64encode(chat_session).decode("utf-8")
    response = client.post("/autocomplete", json={"chat_session": chat_session, "message": "Hello, how are you?"})
    assert response.status_code == 200
    assert isinstance(response.text, str)
