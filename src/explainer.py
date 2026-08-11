import os

# Clean up ghost environment variables that crash httpx/OpenAI on Windows/Anaconda
os.environ.pop('SSL_CERT_FILE', None)
os.environ.pop('REQUESTS_CA_BUNDLE', None)

from pydantic import BaseModel, Field
from typing import List, Literal
from .schemas import Job

class MatchExplanation(BaseModel):
    verdict:Literal["strong", "medium", "weak"] = Field(...,description="how the job fits the user")
    reason: str = Field(...,description="the reason of the judgement reason")
    missing_skills: List[str] = Field(...,description="the missing skills to fit the job")




SYSTEM_PROMPT = """
You are a senior technical career advisor specializing in AI and machine learning roles.

Your task: judge how well ONE specific job fits a candidate's skills.
You will receive the candidate's skills and the job's title, company, skills, and description.

GROUNDING RULES (strict):
- Use ONLY the job data provided in the user message.
- NEVER invent jobs, companies, requirements, or facts that are not present.
- If information is missing, mention the uncertainty in the reason instead of guessing.

EVALUATION GUIDE:
- "strong": the day-to-day work closely matches the candidate's skills.
- "medium": partial overlap; the candidate could do the job but with notable gaps.
- "weak": the actual work differs significantly from the candidate's skills.
- Focus on HOW the skills are used in the description, not just keyword overlap.
- - Be highly critical. If the day-to-day description does not explicitly require AI/ML engineering work, rate it as "medium" or "weak" even if the keywords overlap.

OUTPUT RULES (strict):
- Respond with ONLY valid JSON, no extra text.
- The JSON must contain exactly these keys: "verdict", "reason", "missing_skills".
- "verdict" must be one of: "strong", "medium", "weak".
- "missing_skills" must be a list of strings (an empty list if none).
"""

def _build_user_message(user_skills: List[str], job: Job) -> str:
    """
    Builds the user message containing the user's skills and the job data.
    """
    return f"""
Candidate skills: { user_skills }

Job title: { job.title }
Company: { job.company }
Required skills: { job.skills }
Description: { job.description }
"""


import json
from openai import OpenAI

# TODO 1: Create the client pointed at your local Ollama
# Hint: OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def explain_job_match(user_skills: List[str], job: Job) -> MatchExplanation:
    """
    (keep your docstring)
    """
    # TODO 2: Call the chat API
    
    response = client.chat.completions.create(
    model="llama3",
    messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": _build_user_message(user_skills, job)},
             ],
    temperature = 0.1
    )

    # TODO 3: Extract the raw text the model replied with
    raw_text = response.choices[0].message.content
    # TEMPORARY DEBUG: print the raw text so we can SEE what the model returns
    # before we trust it. Senior engineers inspect before trusting!
    # print(raw_text)
    # TODO 4: Parse the JSON string into a dict, then validate it
    data = json.loads(raw_text)
    return MatchExplanation.model_validate(data)