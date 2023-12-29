# tools/text2image_module.py
import requests
import json

def text2image(prompt, api_key):
    api_url = "https://oneapi.xty.app/v1/images/generations"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        "model": "dall-e-3",
        "prompt": prompt,  # 使用传入的文本作为生成图片的提示
        "n": 1,
        "size": "1024x1024"
    }

    # Make the API request
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        return result['data'][0]['url']
    else:
        return f"Error: {response.status_code}, {response.text}"