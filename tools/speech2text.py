# tools/speech2text_module.py
from openai import OpenAI

def speech2text(path, api_key):
    client = OpenAI(api_key=api_key)

    with open(path, "rb") as audio_file:
        response = client.audio.translations.create(
            model="whisper-1",
            file=audio_file,
        )

    return response.text
