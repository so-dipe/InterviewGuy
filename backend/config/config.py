import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    #SPEECH API CREDENTIALS
    GOOGLE_CLIENT_ID = os.get_env("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.get_env("GOOGLE_CLIENT_SECRET")