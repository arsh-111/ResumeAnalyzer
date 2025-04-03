import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# Check if API key is loaded correctly
if not DEEPSEEK_API_KEY:
    raise ValueError("API key is missing. Please set the DEEPSEEK_API_KEY in your .env file.")

def analyze_resume_with_deepseek(resume_text):
    """Uses DeepSeek API to extract key skills from a resume."""
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}", "Content-Type": "application/json"}

    # Prepare the prompt for the API request
    prompt = f"Extract key skills, job roles, and relevant experience from the following resume:\n\n{resume_text}"

    # Payload for the API request
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "Extract the candidate's key skills and most relevant job roles."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        # Send the request to the DeepSeek API
        response = requests.post(url, headers=headers, json=payload)

        # Check if the response is successful
        if response.status_code == 200:
            # Parse the response JSON to extract the skills and roles
            response_data = response.json()
            if "choices" in response_data and len(response_data["choices"]) > 0:
                extracted_skills = response_data["choices"][0]["message"]["content"]
                return extracted_skills
            else:
                return "Error: No skills extracted from the resume."
        else:
            # Log the response status code and message for debugging
            return f"Error analyzing resume. Status Code: {response.status_code}. Response: {response.text}"

    except Exception as e:
        # Catch any exceptions that occur during the request and log the error
        return f"An error occurred while analyzing the resume: {str(e)}"
