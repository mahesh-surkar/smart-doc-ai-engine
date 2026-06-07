# 🚀 Smart Doc AI Engine

A hybrid AI system combining **Rule-Based Intelligence + LLM (AI)**

---

## 🔥 Idea

This project aims to build a next-generation AI engine that:

- Uses **rules for fast + explainable responses**
- Uses **LLM (AI) for complex reasoning**
- Combines both for better accuracy and efficiency

---

## 🧠 Architecture

User Input  
↓  
Rule Engine (fast, deterministic)  
↓ (fallback if no match)  
LLM Engine (AI reasoning)  
↓  
Final Response  

---

## ⚙️ Tech Stack

- Backend: FastAPI (Python)
- Frontend: HTML (basic UI)
- AI: OpenAI / LLM
- Rule Engine: Custom logic (core innovation)

---

## 🚀 How to Run

### Backend

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
