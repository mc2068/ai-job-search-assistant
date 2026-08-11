from src.job_provider import load_mock_jobs
from src.explainer import explain_job_match

user_skills = ["Python", "RAG", "TensorFlow"]

for job in load_mock_jobs():
    result = explain_job_match(user_skills, job)
    print(f"\n{job.title} @ {job.company}")
    print("Verdict:", result.verdict)
    print("Reason:", result.reason)
    print("Missing:", result.missing_skills)