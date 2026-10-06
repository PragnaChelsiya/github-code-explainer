import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b"


def explain_repository(
    repository_code,
    files,
    temperature=0.7,
    top_k=40,
    top_p=0.9
):

    prompt = f"""
You are a software engineer explaining an entire GitHub repository
to a college student who is new to the project.

Analyze the ENTIRE repository, not just one file.

Generate a concise project-level explanation using EXACTLY these sections:

## 1. Project Overview
Explain in 3-5 sentences what the complete project does.

## 2. Main Technologies
List the programming languages, frameworks, libraries, databases,
and tools that can be identified from the repository.

## 3. Main Features
List the important features implemented by the project.

## 4. Important Files
List the most important files and explain what each one does.
Do not explain every file.

## 5. How It Works
Explain the complete flow from user input to final output.

## 6. Overall Architecture
Explain how the frontend, backend, APIs, agents, database,
and other major components interact.

IMPORTANT RULES:
- Analyze the whole repository.
- Do not focus mainly on HTML, CSS, or JavaScript.
- Do not invent technologies or features.
- Use only information supported by the repository.
- Keep the explanation simple and easy to understand.
- Prefer a project-level explanation over a file-level explanation.

FILES IN REPOSITORY:
{files}

REPOSITORY CODE:
{repository_code}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "top_k": top_k,
                "top_p": top_p
            }
        },
        timeout=300
    )

    response.raise_for_status()
    return response.json()["response"]


def ask_followup(
    repository_code,
    files,
    question,
    temperature=0.7,
    top_k=40,
    top_p=0.9
):

    prompt = f"""
You are answering a follow-up question about a GitHub repository.

Use ONLY the repository information provided below.

Repository files:
{files}

Repository code:
{repository_code}

User's follow-up question:
{question}

Instructions:
- Answer the question clearly and simply.
- Base the answer on the repository code.
- Do not invent information.
- If the repository does not contain enough information to answer,
  clearly say that the information is not available in the repository.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "top_k": top_k,
                "top_p": top_p
            }
        },
        timeout=300
    )

    response.raise_for_status()
    return response.json()["response"]