import os
from openai import OpenAI

proxy_url = 'http://localhost'
proxy_port = '7890'  # Need to change it according to specific conditions
# Set the http_proxy and https_proxy environment variables
os.environ['http_proxy'] = f'{proxy_url}:{proxy_port}'
os.environ['https_proxy'] = f'{proxy_url}:{proxy_port}'

# url = "https://openai.api.com/v1/audio/transcriptions"
API_OFFICIAL_KEY = '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'

# use WHISPER model provided by GPT ,translate speech in any language to text
def speech2text (path, api_key=API_OFFICIAL_KEY):
    client = OpenAI(api_key=api_key)

    with open(path, "rb") as audio_file:
        response = client.audio.translations.create(
            model="whisper-1",
            file=audio_file,
        )

    return response.text


# usage example：
result = speech2text(r"D:\4.wav")
print(result)
