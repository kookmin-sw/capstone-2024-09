# -*- coding: utf-8 -*-
from typing import Dict, Union
from collections import Counter
import httpx

from fastapi import FastAPI, Request
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


job_list = [] # 추 후 DB에 저장하도록 변경

@app.post("/api/get_result")
async def get_result(request: Request):
    data = await request.json()
    messages = data.get('messages', [])
    contents = []
    for message in messages:
        try:
            contents.append(message['content'])
        except KeyError:
            return {"message": "상담을 진행해주세요."}
    contents = " ".join([message['content'] for message in messages])
    data = {"content" : contents}

    word_counts = Counter(contents.split())
    most_common_words = word_counts.most_common(3)
    print(most_common_words)

    response = httpx.post("http://home.sung4854.com:8000/api/predict", json=data)
    response.raise_for_status()
    result = response.json()
    job_info = await get_job_categories(result['result'])
    print(job_info)
    job_list = get_data_from_api(job_info['searchAptdCodes'], result['freq'][0][1])

    contents = f"상담 결과 {job_info['job']}이 적합한 직업군 이라고 생각합니다. 해당 관련직에 관련된 직업에 대해 말씀드리겠습니다."

    for index, (job_name, job_info) in enumerate(job_list.items()):
        related_job_name = job_info[1]
        contents += f"\n\n {index}. {job_name}, [{related_job_name}]"

    contents += "\n\n위의 직업군 중에서 조금 더 자세하게 알고 싶은 직업이 있으신가요??"

    print(contents)

    return {"response": contents}