import os

# Clean up ghost environment variables that crash Gradio on Windows/Anaconda
os.environ.pop('SSL_CERT_FILE', None)
os.environ.pop('REQUESTS_CA_BUNDLE', None)


import gradio as gr
from .explainer import explain_job_match
from typing import List, Dict

# Import our custom logic
from .job_provider import load_mock_jobs
from .matcher import calculate_skill_match_score

def search_jobs(user_skills_text: str) -> List[List]:
    """
    Takes a comma-separated string of user skills, 
    scores all mock jobs, and returns them sorted by score.
    """
    
    # 1. Split the comma-separated string into a list of skills
    # Hint: use the .split(',') method
    user_skills = user_skills_text.split(',')
    # 2. Load the mock jobs using our job_provider
    jobs = load_mock_jobs()
    # 3. Create an empty list to hold our results
    results = []
    
    # 4. Loop through each job
    # Hint: For each job, calculate the score using calculate_skill_match_score(user_skills, job)
    # Then, create a dictionary containing the job's Title, Company, Remote Type, and Score.
    # Append that dictionary to the `results` list.
    for job in jobs:
        score = calculate_skill_match_score(user_skills, job)
        
        # TODO 1: Call explain_job_match to get the MatchExplanation object
        ai_explanation = explain_job_match(user_skills, job)
        
        # TODO 2: Extract the verdict and reason from the explanation object
        ai_verdict = ai_explanation.verdict
        ai_reason = ai_explanation.reason
        
        # TODO 3: Build your row list (must match the new headers order exactly)
        row = [job.title, job.company, job.remote_type, score, ai_verdict, ai_reason]
        
        results.append(row)
    return results

# ... (keep your imports and search_jobs function above this) ...

with gr.Blocks() as demo:
    # 1. Add a Markdown title
    # Hint: gr.Markdown("# 🤖 AI Engineer Job Scout")
    gr.Markdown("# 🤖 AI Engineer Job Scout")
    # 2. Create the skills textbox and save it in a variable
    # Hint: skills_input = gr.Textbox(label="...", placeholder="Python, LLMs, RAG")
    skills_input = gr.Textbox(label="Enter your skills (comma-separated)", placeholder="Python, LLMs, RAG")
    # 3. Create the search button and save it in a variable
    # Hint: search_button = gr.Button("Search Jobs", variant="primary")
    search_button = gr.Button("Search Jobs", variant="primary")
    # 4. Create the Dataframe to display the results table
    # Hint: results_table = gr.Dataframe(headers=["Title", "Company", "Remote type", "Score"], label="Ranked Results")
    results_table = gr.Dataframe(headers=["Title", "Company", "Remote type", "Score", "AI Verdict", "AI Reason"], label="Ranked Results")
    # 5. Wire the button to the function!
    # Hint: search_button.click(fn=search_jobs, inputs=[skills_input], outputs=[results_table])
    search_button.click(fn=search_jobs, inputs=[skills_input], outputs=[results_table])
# Launch the app
demo.launch()