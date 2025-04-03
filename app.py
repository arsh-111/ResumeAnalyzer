import streamlit as st
import os
from resume_parser import extract_text_from_pdf
from deepseek_analyzer import analyze_resume_with_deepseek
from job_scraper import fetch_jobs  # Updated import
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer & Job Suggestion Bot")
st.write("Upload your resume to extract key skills and get job recommendations.")

# Upload Resume
uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from resume..."):
        file_path = os.path.join("uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        resume_text = extract_text_from_pdf(file_path)
        st.text_area("Extracted Resume Text", resume_text, height=300)  # Display for debugging

    with st.spinner("Analyzing resume with AI..."):
        extracted_skills = analyze_resume_with_deepseek(resume_text)
    
    st.subheader("🛠️ Extracted Skills & Job Roles")
    st.write(extracted_skills)

    # Get job recommendations
    st.subheader("💼 Job Recommendations")
    first_skill = extracted_skills.split("\n")[0] if extracted_skills else "Software Engineer"  # Fallback skill
    job_recommendations = fetch_jobs(first_skill)  # Fetch jobs using LinkedIn or Jooble API

    if job_recommendations and "Error" not in job_recommendations[0]:
        for job in job_recommendations:
            st.markdown(job, unsafe_allow_html=True)
    else:
        st.error("❌ No jobs found or API error. Please try again.")
