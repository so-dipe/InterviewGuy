from vertexai.preview.generative_models import GenerativeModel
from ..logs.logging import get_logger

LOG = get_logger(__name__)

model = GenerativeModel('gemini-pro')

def init_chat():
    try:
        chat = model.start_chat()
    except Exception as e:
        LOG.error(f"Error initializing chat: {e}")
        chat = None
    return chat

def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        response = response.text
    except Exception as e:
        LOG.error(f"Error generating response: {e}")
        response = str(e)
    return response

def generate_chat_response(chat_session, message):
    try:
        response = chat_session.send_message(message)
        response = response.text
    except Exception as e:
        LOG.error(f"Error generating chat response: {e}")
        response = str(e)
    return response

