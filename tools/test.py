# -*- coding = utf-8 -*-
# @Time : 2023/12/28 23:57
# @Author : 王加炜
# @File : test.py
# @Software : PyCharm

# -*- coding: utf-8 -*-
from openai import OpenAI
import os

proxy_url = 'http://localhost'
proxy_port = '7890'

# Set the http_proxy and https_proxy environment variables
os.environ['http_proxy'] = f'{proxy_url}:{proxy_port}'
os.environ['https_proxy'] = f'{proxy_url}:{proxy_port}'

def assistant(client, init_prompt, user_input):
    # Initialize the conversation
    messages = [
        {"role": "system", "content": init_prompt},
        {"role": "user", "content": user_input}
    ]

    # Get assistant response
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
    )

    # Return assistant message
    return completion.choices[0].message.content

# 使用：
client = OpenAI(api_key="sk-5xH3t0BNBnGAEBJ9190a84A1DaA045C7B53aF04143E99049",
                base_url="https://oneapi.xty.app/v1")

# 设置一些默认提示
default_prompts = [
    "You are a helpful assistant who can write song lyrics.",
    "You are a knowledgeable assistant who can answer questions about science.",
    "You are a witty assistant who can engage in amusing conversations."
]

# 从默认提示列表中选择一个提示
init_prompt = default_prompts[0]  # 或者可以随机选择一个提示

while True:
    user_input = input("You: ")
    if user_input.lower() == 'q':
        break
    response = assistant(client, init_prompt, user_input)
    print("Assistant: ", response)