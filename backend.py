from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import ollama  

app = FastAPI()

# Database setup
conn = sqlite3.connect("leads.db", check_same_thread=False)
cursor = conn.cursor()

class Lead(BaseModel):
    name: str
    email: str
    budget: int

def score_lead(lead):
    prompt = f"""
    You are an AI assistant for real estate lead scoring.
    Based on the following details, classify the lead as "Hot", "Warm", or "Cold".

    Lead Details:
    - Name: {lead.name}
    - Budget: {lead.budget}

    Output only one word: "Hot", "Warm", or "Cold".
    """

    try:
        response = ollama.chat(
            model="mistral",
            messages=[
                {"role": "system", "content": "You are an AI scoring real estate leads."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

@app.get("/score_lead/{email}")
def get_lead_score(email: str):
    cursor.execute("SELECT * FROM leads WHERE email=?", (email,))
    lead = cursor.fetchone()

    if not lead:
        return {"message": "Lead not found"}

    name, email, budget = lead[1], lead[2], lead[3]
    score = score_lead(Lead(name=name, email=email, budget=budget))
    return {"lead_score": score}
