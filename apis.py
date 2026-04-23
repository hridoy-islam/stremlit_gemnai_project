from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS

import io

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

#initializing a client

client = genai.Client(api_key=my_api_key)


#note generator

def note_generator(images):
    propmt = """ Summerize the picture in note format in bangla language at max 100 words , make sure you add necessary markdown differentiate different section """
    response = client.models.generate_content(
        model = 'gemini-3-flash-preview',
        contents = [images, ]                           
    )
    return response.text

#audio
def audio_transcription(text):
    speech = gTTS(text, lang='en', slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generator(image, difficulty):
    prompt = f"Generte 3 Quiz Based on the {difficulty}. Make Sure to add markdown with correct answer"

    response = client.models.generate_content(
        model = 'gemini-3-flash-preview',
        contents = [image, prompt]                           
    )
    return response.text