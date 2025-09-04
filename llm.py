import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

resp = client.chat.completions.create(
    model="meta-llama/llama-3.1-70b-instruct", 
    messages=[{"role": "user", "content": "YOLO MATE"}],
)

print(resp.choices[0].message.content)
