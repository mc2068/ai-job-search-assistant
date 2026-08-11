# 🤖 AI-Jon-Search-Assistant

An agentic AI application that helps AI engineers find relevant job opportunities by combining keyword-based skill matching with a local LLM reasoning layer. 

## 🚀 The Problem
Job boards are noisy. Recruiters often spam AI buzzwords (like "RAG" or "LLMs") on unrelated roles like "Data Analyst" or "Backend Developer". A simple keyword search will give you false positives. 

## 💡 The Solution
Instead of just counting keywords, this app uses a local LLM (Llama 3) to read the job description and provide a **grounded, critical verdict** on whether the day-to-day work actually matches an AI Engineer's skills.

## 🏗️ Architecture & Tech Stack
- **UI:** Gradio
- **Data Validation:** Pydantic (enforces strict schemas to prevent pipeline crashes)
- **LLM Engine:** Ollama (running Llama 3 locally for zero-cost, private inference)
- **API Client:** OpenAI SDK (pointed at a local base_url)
- **Language:** Python

## ⚠️ Hallucination Guardrails
To prevent the LLM from inventing fake jobs, the architecture strictly separates **Data Retrieval** from **LLM Reasoning**:
1. The app loads verified mock data.
2. The LLM acts *only* as an analyst. It is strictly forbidden from searching for or inventing companies.

## ⚙️ How to Run Locally
1. Clone the repo and install dependencies: `pip install -r requirements.txt`
2. Ensure you have Ollama running locally with Llama 3: `ollama run llama3`
3. Launch the app: `python -m src.app`

## 🧠 Limitations & Future Work
Local models (like Llama 3 8B) are excellent for privacy and speed, but they struggle with critical reasoning and often act as "yes-men", rating everything highly. Future versions will integrate asynchronous (asyncio) execution for faster loading, and swap the local model for a larger cloud API (like GPT-4o or Claude) for stricter logical evaluation.
