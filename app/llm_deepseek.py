# app/llm_deepseek.py
import requests

def call_deepseek(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "deepseek-chat",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    return response.json()["response"]

if __name__ == "__main__":
    print(call_deepseek("물질의 상태변화에 대해 간단히 설명해줘"))
