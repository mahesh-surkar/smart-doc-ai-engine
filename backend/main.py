from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    text: str

def rule_engine(text):
    if "interest" in text:
        return {
            "answer": "Interest = Principal × Rate × Time",
            "confidence": 0.9,
            "source": "rule"
        }
    return None

def llm_engine(text):
    return {
        "answer": f"AI response for: {text}",
        "confidence": 0.6,
        "source": "llm"
    }

@app.post("/ask")
def ask(query: Query):
    rule_result = rule_engine(query.text)

    if rule_result and rule_result["confidence"] > 0.8:
        return rule_result

    return llm_engine(query.text)
