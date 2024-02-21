from google.cloud import speech_v1

async def transcribe(audio, ):
    speech_client = speech_v1.SpeechAsyncClient()
    speech_config = speech_v1.RecognitionConfig(
        encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
    )
    
    audio = speech_v1.RecognitionAudio(content=audio)
    request = speech_v1.RecognizeRequest(config=speech_config, audio=audio)

    try:
        response = await speech_client.recognize(request)
        response = response.results[0].alternatives[0].transcript
    except Exception as e:
        print(e)
        return "Error: " + str(e)

    return response

    