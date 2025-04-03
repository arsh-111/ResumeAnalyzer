import requests
import os

DEEPSEEK_API_KEY = "your_api_key_here"

resume_text = "Skills: Python, AI, Machine Learning, AWS, Docker, Kubernetes"

url = "https://api.deepseek.com/v1/analyze"
headers = {
    "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    "Content-Type": "application/json"
}
payload = {
    "model": "deepseek-vision",
    "input": resume_text,
    "task": "extract_skills"
}

response = requests.post(url, headers=headers, json=payload)

print("Response Code:", response.status_code)
print("Response Body:", response.json())
