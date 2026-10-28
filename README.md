# 🚀 GitHub Code Explainer — AI-Powered Repository Analysis

An AI-powered web application that analyzes GitHub repositories and explains their code in simple, beginner-friendly language using a locally running Large Language Model (LLM).

🔗 **Live Demo:** https://app-code-explainer-u6e6jf2onjavepek8u5g4l.streamlit.app/  
💻 **GitHub Repository:** https://github.com/PragnaChelsiya/github-code-explainer

## 📌 Project Overview

Understanding an unfamiliar codebase can be challenging, especially for students and beginner developers. GitHub Code Explainer simplifies this process by allowing users to submit a public GitHub repository URL and receive an AI-generated explanation of the project's structure, technologies, features, and workflow.

The application uses a Streamlit frontend, a FastAPI backend, GitPython for repository cloning, and Ollama to run the Qwen 2.5 3B language model locally.

## ✨ Features

- **Repository Analysis:** Accepts a public GitHub repository URL.
- **Project Overview:** Explains the purpose and functionality of the repository.
- **Technology Detection:** Identifies programming languages, frameworks, libraries, and tools from supported repository files.
- **Important File Analysis:** Highlights key files and their responsibilities.
- **Workflow Explanation:** Describes how the project's components interact.
- **Interactive Follow-up Questions:** Allows users to ask additional questions about the analyzed code.
- **Adjustable AI Generation:** Supports temperature, Top-k, and Top-p parameters to experiment with model responses.
- **Local LLM Integration:** Uses Ollama with Qwen 2.5 3B for code explanations.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| FastAPI | Backend REST API |
| GitPython | Cloning GitHub repositories |
| Ollama | Local LLM runtime |
| Qwen 2.5 3B | Code explanation and question answering |
| Requests | HTTP communication |
| Pydantic | API request validation |

## 🏗️ Project Architecture

```text
GitHub Code Explainer
│
├── frontend/
│   └── app.py                 # Streamlit user interface
│
├── backend/
│   ├── main.py                # FastAPI endpoints
│   ├── github_processor.py    # Repository cloning and code extraction
│   ├── llm.py                 # Ollama model integration
│   └── requirements.txt       # Backend dependencies
│
├── requirements.txt           # Streamlit Cloud dependencies
└── README.md
```

## 🔄 How It Works

1. The user enters a public GitHub repository URL.
2. The backend clones the repository using GitPython.
3. Supported source files are collected while common generated and dependency directories are ignored.
4. The extracted repository code is passed to the Qwen 2.5 3B model through Ollama.
5. The model generates a structured explanation of the project's purpose, technologies, important files, architecture, and workflow.
6. The user can ask follow-up questions about the repository.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- Ollama installed on your computer
- The Qwen 2.5 3B model downloaded through Ollama

### 1. Clone the repository

```bash
git clone https://github.com/PragnaChelsiya/github-code-explainer.git
cd github-code-explainer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
pip install -r backend/requirements.txt
```

### 3. Download the model

```bash
ollama pull qwen2.5:3b
```

### 4. Start the FastAPI backend

Open a terminal and run:

```bash
cd backend
python -m uvicorn main:app --port 8001
```

The backend will be available at:

`http://127.0.0.1:8001`

FastAPI interactive API documentation:

`http://127.0.0.1:8001/docs`

### 5. Start the Streamlit frontend

Open a second terminal from the project root:

```bash
streamlit run frontend/app.py
```

The frontend will usually open at:

`http://localhost:8501`

**Note:** The frontend's configured backend URL must point to the running FastAPI server. For local use, the backend and Ollama must both be running on your computer.

## 🎛️ AI Generation Parameters

The application provides controls to experiment with how the model generates responses.

- **Temperature:** Controls response variability.
- **Top-k:** Limits token selection to a set of high-ranked candidates.
- **Top-p:** Selects tokens from a cumulative probability distribution.

These settings control text generation. They do not fine-tune or retrain the underlying Qwen model.

## 🌐 Deployment

The Streamlit interface is deployed using Streamlit Community Cloud.

The AI backend uses FastAPI and a locally running Ollama model. The live interface requires a reachable backend to perform repository analysis and answer follow-up questions. A local backend or temporary tunnel is not guaranteed to remain available continuously.

## 🎯 Learning Outcomes

Through this project, I explored:

- Building a full-stack Python application.
- Developing REST APIs using FastAPI.
- Integrating a locally hosted LLM using Ollama.
- Cloning and processing GitHub repositories programmatically.
- Connecting a Streamlit frontend to a backend API.
- Experimenting with LLM generation parameters.
- Deploying a Streamlit application and understanding backend connectivity.

## 🔮 Future Enhancements

- Support for larger repositories using file selection and chunking.
- Improved code understanding through retrieval-augmented generation (RAG).
- Persistent conversation history.
- More detailed dependency and architecture analysis.
- Deployment of the backend and model through a reliable hosting solution.

## 👩‍💻 Author

**D Pragna Chelsiya**  
BCA Student | Alliance University, Bengaluru

- GitHub: https://github.com/PragnaChelsiya
- Portfolio: https://pragna-chelsiya-portfolio.vercel.app/

---

⭐ If you find this project useful, feel free to explore the repository and share feedback.
