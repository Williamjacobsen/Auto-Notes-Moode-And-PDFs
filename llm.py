import os
from openai import OpenAI

class llm:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.environ["OPENROUTER_API_KEY"],
        )

    def prompt(self, prompt):
        resp = self.client.chat.completions.create(
            model="meta-llama/llama-3.1-70b-instruct", 
            messages=[{"role": "user", "content": prompt}],
        )
        print(resp.choices[0].message.content)
