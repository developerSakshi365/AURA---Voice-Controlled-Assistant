import requests
import os

API_TOKEN = os.getenv("API_TOKEN")


MODEL = "google/flan-t5-base"

url = f"https://router.huggingface.co/models/{MODEL}"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "inputs": "Who developed Python?",
    "parameters": {
        "max_new_tokens": 100,
        "temperature": 0.7
    }
}

response = requests.post(url, headers=headers, json=payload, timeout=20)

print("STATUS:", response.status_code)
print("RAW:", response.text)

if response.status_code == 200:
    print("JSON:", response.json())
