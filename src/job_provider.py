import json
from pathlib import Path
from typing import List

# Import our Pydantic schema from the same folder
from .schemas import Job

def load_mock_jobs() -> List[Job]:
    """
    Loads mock job data from the JSON file, validates it against the Job schema,
    and returns a list of Job objects.
    """
    
    # 1. Define the path to the JSON file (Already done for you!)
    file_path = Path(__file__).parent.parent / "data" / "mock_jobs.json"
    
    jobs_list = []
    
    # TODO 2: Open the file and load the JSON data into a variable called `raw_jobs`
    # Hint: use `with open(file_path, 'r') as file:` and `json.load(file)`
    with open(file_path, 'r') as f:
        raw_jobs = json.load(f)
    
    for job in raw_jobs:
        try:
            # TODO 1: Validate the single dictionary using Job.model_validate()
            # and assign it to a variable called validated_job
            validated_job = Job.model_validate(job)
            # TODO 2: Append validated_job to jobs_list
            jobs_list.append(validated_job)
        except Exception as e:
            # This catches the error, prints a warning, and moves to the next job
            print(f"Skipping invalid job data: {e}")
            continue
         
    # TODO 4: Return the `jobs_list`
    return jobs_list