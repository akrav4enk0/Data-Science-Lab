import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ.get("OPENAI_BASE_URL", "https://api.swissai.cscs.ch/v1"),
)
model = os.environ.get("OPENAI_MODEL", "swiss-ai/Apertus-8B-Instruct-2509")
resp = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Write a Python function fib(n) that returns the first n Fibonacci numbers and print(fib(10))."}],
)
print(resp.choices[0].message.content)
