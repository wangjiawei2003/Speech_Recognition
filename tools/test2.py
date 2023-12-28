import requests
import json
import os

proxy_url = 'http://localhost'
proxy_port = '7890'
# Set the http_proxy and https_proxy environment variables
os.environ['http_proxy'] = f'{proxy_url}:{proxy_port}'
os.environ['https_proxy'] = f'{proxy_url}:{proxy_port}'

OPENAI_API_KEY = 'sk-5xH3t0BNBnGAEBJ9190a84A1DaA045C7B53aF04143E99049'

api_url="https://oneapi.xty.app/v1/images/generations"
headers={
    'Content-Type':'application/json',
    'Authorization':f'Bearer {OPENAI_API_KEY}'
}

data = {
    "model": "dall-e-3",
    "prompt": "a white siamese cat",
    "n": 1,
    "size": "1024x1024"
}

# Make the API request
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 200:
    result = response.json()
    print("Generated image URL:", result['data'][0]['url'])
else:
    print("Error:", response.status_code, response.text)

