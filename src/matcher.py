from typing import List
from .schemas import Job

def calculate_skill_match_score(user_skills: List[str], job: Job) -> float:
    """
    Calculates a skill match score from 0 to 100 based on overlapping skills.
    """
    
    # 1. Normalize the user's skills to lowercase and strip whitespace
    # Hint: use a list comprehension like [skill.strip().lower() for skill in user_skills]
    normalized_user_skills = [skill.strip().lower() for skill in user_skills]
    
    # 2. Normalize the job's skills to lowercase and strip whitespace
    normalized_job_skills = [skill.strip().lower() for skill in job.skills]
    
    # 3. Convert both lists to Sets
    user_set = set(normalized_user_skills)
    job_set = set(normalized_job_skills)
    
    # 4. Find the intersection (overlapping skills)
    matching_skills = user_set.intersection(job_set)
    
    # 5. Calculate the score!
    # Formula: (Number of matching skills / Total number of job skills) * 100
    # Hint: Use len() to count the items in the sets.
    # Make sure to handle the case where job_set is empty to avoid dividing by zero!
    Number_of_matching_skills = len(matching_skills)
    Number_of_job_skills = len(job_set)
    try:
        score = (Number_of_matching_skills / Number_of_job_skills) * 100
        return score
    except Exception as e:
        print(f"Could not calculate score: {e}")
        return 0.0