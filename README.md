# SupportIQ

SupportIQ is a **production-grade, microservices-based AI customer support system** built to demonstrate real-world backend engineering, AI integration, and cloud-ready deployment practices.

The project emphasizes **clean service boundaries, cost-aware AI usage, automated testing, containerization, and CI/CD-friendly design**.

---

## 🧠 High-Level Architecture

SupportIQ is designed as a set of independent, loosely coupled microservices:

- **Inference Service**  
  Generates AI responses using a pluggable LLM interface (mock, Hugging Face, local).

- **Gateway Service** *(in progress)*  
  Acts as the public-facing API and orchestrates requests across services.

- **Intent Service** *(planned)*  
  Classifies user intent (billing, support, escalation, etc.).

- **Memory Service** *(planned)*  
  Manages conversation history and session context.

Each service is:
- Independently deployable  
- Containerized with Docker  
- Tested and linted  
- Designed for CI/CD and cloud deployment  

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI  
- **AI / LLM:** Mock LLM, Hugging Face Inference API (pluggable design)  
- **Testing:** Pytest, FastAPI TestClient  
- **Linting & Formatting:** Black, isort, flake8, mypy  
- **Containerization:** Docker  
- **Cloud (planned):** Azure Container Apps  
- **CI/CD (planned):** GitHub Actions  

---

## 🚀 Running a Service Locally

Example: **Inference Service**

```bash
cd inference-service
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
## 📘 Swagger UI:
```bash
http://localhost:8000/docs
```

## 📦 Running with Docker

```bash
cd inference-service
docker build -t supportiq-inference .
docker run -p 8000:8000 supportiq-inference
```

## 🧪 Testing

Automated tests are written using pytest and FastAPI’s TestClient.

Run tests locally:
```bash
pytest
```

Tests are:

- Deterministic
- Cost-free (AI calls are mocked)
- CI/CD safe

## 📌 Project Status

- ✅ Inference Service complete (Dockerized, tested, linted)
- 🔄 Gateway Service in progress
- 🔜 Intent & Memory services planned
- 🔜 CI/CD and Azure deployment planned

## 📄 License

This project is licensed under the MIT License and is intended for learning, demonstration, and portfolio use.
