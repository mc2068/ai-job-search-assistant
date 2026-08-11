from src.job_provider import load_mock_jobs

jobs = load_mock_jobs()

print(f"Successfully loaded {len(jobs)} validated jobs!")
for job in jobs:
    print(f"- {job.title} at {job.company} (Remote: {job.remote_type})")