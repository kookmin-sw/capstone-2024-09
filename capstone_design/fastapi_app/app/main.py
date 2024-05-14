# -*- coding: utf-8 -*-
from typing import List, Dict, Union
import httpx

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import UJSONResponse
from pydantic import BaseModel

from .open_ai import get_chat_response
from .db_query import save_chats, get_job_categories
from .job_info_detail import get_data_from_api

app = FastAPI(default_response_class=UJSONResponse)

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
    role = message.messages['role']
    msg = message.messages['content']
    return_mes = get_chat_response(msg)
    await save_chats(role, msg) # 사용자의 질문 저장
    await save_chats(role, return_mes) # AI의 답변에 대한 저장
    return {"response": return_mes}



from fastapi import Request

@app.post("/api/get_result")
async def get_result(request: Request):
    data = await request.json()
    messages = data.get('messages', [])
    contents = " ".join([message['content'] for message in messages])
    data = {"content" : contents}

    response = httpx.post("http://home.sung4854.com:8000/api/predict", json=data)
    response.raise_for_status()
    result = response.json()
    job_info = await get_job_categories(result['result'])
    print(job_info)
    get_data_from_api(job_info['career_id'])

    return job_info