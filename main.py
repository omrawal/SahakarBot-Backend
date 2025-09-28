from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from query import get_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    question: str
    answer: str

class QueryRequest(BaseModel):
    question: str
    chat_history: Optional[List[ChatMessage]] = None

@app.post("/query")
async def query_endpoint(request: QueryRequest):
    # Convert chat history to the format expected by get_answer
    chat_history = [
        {"question": msg.question, "answer": msg.answer}
        for msg in (request.chat_history or [])
    ]

    try:
        answer = get_answer(request.question, chat_history)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}