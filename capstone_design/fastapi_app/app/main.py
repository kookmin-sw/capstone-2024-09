from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Union
from .open_ai import get_chat_response

app = FastAPI()

origins = [
    "http://localhost:3000",  # React 앱의 도메인
    "http://fastapi_app:5000",
    "http://develop.sung4854.com:3000",
    "https://develop.sung4854.com",
    # 추가적인 도메인들...
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    messages: Dict[str, Union[str, str]]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/chat")
async def chat(message: Message):
    print(message)
    role = message.messages['role']
    msg = message.messages['content']
    return_mes = get_chat_response(msg)
    print("return_mes : ", return_mes)
    return {"response": return_mes}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}