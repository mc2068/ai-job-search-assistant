# AI Job Search Assistant

## Overview
This project helps AI engineers find relevant job opportunities and ranks them based on skill match.
## Problem
- Job searching is time-consuming
- Many job listings are not personalized
- Users may not know which roles fit their skills
- LLMs may hallucinate if not grounded in real data
## Solution
- Uses structured job data
- Matches jobs to user skills
- Gives a skill match score
- Explains why a job is a good match
- Uses real job listings, not invented ones
## Key Features
- Skill Match Score: scores jobs based on how well they match the user's skills.
- AI-powered job ranking/explanation: every job ranking has an explanation
- Source URL verification to reduce hallucination risk: the src url make the user sure that the job is real
## Planned Architecture
User Input
Job Provider
Job Normalizer/Validator
AI Ranking Agent
Response Formatter
Gradio UI
## Roadmap
1. Define job data schema
2. Create mock job data
3. Build skill matching logic
4. Add LLM ranking and explanation
5. Build Gradio interface
6. Connect real job source
7. Improve README and demo
