import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load API keys from .env file

# Get API keys from environment variables
LINKEDIN_API_KEY = os.getenv("LINKEDIN_API_KEY")
JOOBLE_API_KEY = os.getenv("JOOBLE_API_KEY")

def fetch_jobs_from_linkedin(skill):
    """
    Fetch jobs using LinkedIn Jobs API.
    """
    headers = {
        "Authorization": f"Bearer {LINKEDIN_API_KEY}",
        "Content-Type": "application/json"
    }
    url = f"https://api.linkedin.com/v2/jobSearch?q=keywords&keywords={skill}"
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        jobs = []
        for job in data.get("elements", [])[:5]:  # Fetch top 5 jobs
            job_title = job.get("title", "Unknown Job")
            job_link = job.get("jobPostingUrl", "#")
            jobs.append(f"{job_title} - [Apply Here]({job_link})")
        return jobs
    else:
        return ["Error fetching jobs from LinkedIn."]

def fetch_jobs_from_jooble(skill):
    """
    Fetch jobs using Jooble API.
    """
    url = f"https://jooble.org/api/{JOOBLE_API_KEY}"
    payload = {"keywords": skill, "location": "Remote", "radius": "50", "page": "1"}

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        jobs = []
        for job in data.get("jobs", [])[:5]:  # Fetch top 5 jobs
            job_title = job.get("title", "Unknown Job")
            job_link = job.get("link", "#")
            jobs.append(f"{job_title} - [Apply Here]({job_link})")
        return jobs
    else:
        return ["Error fetching jobs from Jooble."]

def fetch_jobs(skill):
    """
    Fetch job listings using LinkedIn Jobs API first, then Jooble API as backup.
    """
    jobs = fetch_jobs_from_linkedin(skill)
    
    if "Error" in jobs[0]:  # If LinkedIn fails, use Jooble API
        jobs = fetch_jobs_from_jooble(skill)

    return jobs
