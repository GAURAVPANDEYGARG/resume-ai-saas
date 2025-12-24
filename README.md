# 🤖 Resume AI SaaS

An **AI-powered Resume Analyzer** that compares a resume against a job description and provides:
- Match score
- Strengths & weaknesses
- Improvement suggestions
- ATS optimization tips

Built as a **production-ready SaaS** using **FastAPI + Streamlit + Groq/OpenAI**, deployed on cloud with **scalable, secure architecture**.

---

## 🚀 Live Demo

- **Frontend (UI)**: Streamlit Cloud  
- **Backend (API)**: Render (FastAPI)

> ℹ️ The source code is intentionally kept **private**.  
> The application is publicly accessible via the deployed URLs.

---

## 🧩 Features

- 📄 **PDF Resume Upload**
- 🧾 **Job Description Analysis**
- 📊 **Resume–Job Match Score**
- 💪 Strengths & ⚠️ Weaknesses detection
- 🛠 Actionable improvement suggestions
- 📈 ATS optimization insights
- 🔐 Secure API access with App API Key
- ⚡ Supports multiple LLM providers:
  - **Groq** (recommended)
  - **OpenAI**
- 🌍 Deployed with HTTPS & auto-scaling
- 💰 Zero infrastructure cost (BYO LLM key)

---

## 🏗 Architecture

User Browser
│
├──▶ Streamlit Cloud (Frontend UI)
│
└──▶ FastAPI (Render)
│
└──▶ Groq / OpenAI APIs

yaml
Copy code

- Stateless backend
- No database required
- Scales horizontally
- Secure & cost-efficient

---

## 🛠 Tech Stack

### Backend
- **FastAPI**
- **Uvicorn**
- **SlowAPI** (rate limiting)
- **Groq SDK / OpenAI SDK**
- **Pydantic**

### Frontend
- **Streamlit**
- **PDFPlumber**
- **Requests**

### Cloud
- **Render** – Backend deployment
- **Streamlit Cloud** – Frontend deployment
- **GitHub (Private Repo)** – Source control

---

## 🔐 Security Model

- App-level API key (`X-API-Key`) for access control
- Rate limiting enabled
- No user data stored
- No resumes or API keys persisted
- HTTPS enforced by cloud platforms

---

## 🔑 LLM API Keys (User-Provided)

Users must bring their own LLM API key.

Create keys here:
- **Groq (Free & Fast)**: https://console.groq.com/keys
- **OpenAI**: https://platform.openai.com/api-keys

> Your API key is used **only for the request** and is **never stored**.

---

## 🧪 Local Development (Optional)

### Backend
```bash
cd api
pip install -r requirements.txt
uvicorn main:app --reload
```
### Frontend
```bash
Copy code
cd ui
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

📦 Deployment
Backend (FastAPI)

Deployed on Render

Auto-redeploy on Git push

Stateless & horizontally scalable

Frontend (Streamlit)

Deployed on Streamlit Cloud

Auto-redeploy on Git push

---

📈 Scaling Strategy

UI auto-scales via Streamlit Cloud

API auto-scales via Render

LLM compute handled by Groq/OpenAI

No database bottlenecks

---

💰 Cost Model
Component	Cost
Backend	Free (Render)
Frontend	Free (Streamlit Cloud)
LLM usage	Paid by user
Infra cost	$0

---

🎯 Use Cases

Job seekers optimizing resumes

Career coaches

Recruiters & HR screening

AI portfolio project

SaaS MVP foundation

---

🧠 Future Enhancements

📄 Download analysis as PDF

📊 Skill match visual charts

💳 Stripe-based monetization

👤 User login & history

🌐 Custom domain support

---

👨‍💻 Author

Gaurav Pandey
Software Engineer | Backend & AI Enthusiast

Java • Spring Boot • FastAPI

Databricks • Cloud • Generative AI
Databricks • Cloud • Generative AI
