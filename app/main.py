from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import ask_rag

app = FastAPI()

class Question(BaseModel): 
    question: str

@app.post("/question")
def ask_question(data: Question):
    anwser = ask_rag(data.question)
    return {"answer": anwser}
