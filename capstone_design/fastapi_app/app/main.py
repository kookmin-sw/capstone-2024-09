from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, Request
from pydantic import BaseModel
from .open_ai import get_chat_response

router = APIRouter()
app = FastAPI()

origins = [
    "http://react_app:3000",  # React 앱의 도메인
    # 추가적인 도메인들...
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    messages: list

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/chat")
async def chat():
    messages = chat_request.messages
    messages = "나는 축구와 농구를 좋아해"
    response = get_chat_response(messages)
    return {"response": response}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

    app.include_router(router)