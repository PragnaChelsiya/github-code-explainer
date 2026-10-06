from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from github_processor import process_repository
from llm import explain_repository, ask_followup


app = FastAPI(
    title="GitHub Code Explainer",
    description="Local GenAI application for explaining GitHub repositories"
)


class RepositoryRequest(BaseModel):
    github_url: str
    temperature: float = 0.7
    top_k: int = 40
    top_p: float = 0.9


class FollowUpRequest(BaseModel):
    repository_code: str
    files: list[str]
    question: str
    temperature: float = 0.7
    top_k: int = 40
    top_p: float = 0.9


@app.get("/")
def home():
    return {
        "message": "GitHub Code Explainer API is running"
    }


@app.post("/explain")
def explain(request: RepositoryRequest):

    try:
        repository = process_repository(request.github_url)

        explanation = explain_repository(
            repository["code"],
            repository["files"],
            temperature=request.temperature,
            top_k=request.top_k,
            top_p=request.top_p
        )

        return {
            "success": True,
            "files_analyzed": repository["files"],
            "repository_code": repository["code"],
            "explanation": explanation
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/followup")
def followup(request: FollowUpRequest):

    try:

        answer = ask_followup(
            request.repository_code,
            request.files,
            request.question,
            temperature=request.temperature,
            top_k=request.top_k,
            top_p=request.top_p
        )

        return {
            "success": True,
            "answer": answer
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )