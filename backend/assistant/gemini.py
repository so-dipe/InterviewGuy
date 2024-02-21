from vertexai.preview.generative_models import GenerativeModel

model = GenerativeModel('gemini-pro')

def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text

def init():
    return model.start_chat()

def chat(chat_session, message):
    response = chat_session.send_message(message)
    return response.text
