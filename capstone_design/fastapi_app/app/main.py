# -*- coding: utf-8 -*-
from typing import Dict, Union
import httpx, os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import UJSONResponse
from pydantic import BaseModel

from .open_ai import get_chat_response
from .db_query import get_job_categories
from .job_info_detail import get_data_from_api, get_detail

react_address = os.getenv('react_address')

app = FastAPI(default_response_class=UJSONResponse)

origins = [
    react_address,
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
    msg = message.messages['content']

    return_mes = get_chat_response(msg)
    return {"response": return_mes}

@app.post("/api/predict")
async def predict(request: Request):
    data = await request.json()
    messages = data.get('messages', [])
    contents = " ".join([message['content'] for message in messages])
    data = {"content" : contents}

    # 분류형 AI에 분석 요청
    response = httpx.post("http://home.sung4854.com:8000/api/predict", json=data)
    response.raise_for_status()
    result = response.json()

    return {"response": result}

@app.post("/api/get_job_info")
async def get_job_info(request: Request):
    data = await request.json()
    result = data.get('result', None)
    words = data.get('words', None)

    if result is None or words is None:
        return {"message": "Invalid request data."}

    job_info = await get_job_categories(result)
    job_list = get_data_from_api(job_info['searchAptdCodes'], words)
    if len(job_list) == 0:
        return {"response": "조금 더 자세한 질문을 해주시겠어요?"}

    contents = f"상담 결과 {job_info['job']}이 적합한 직업군 이라고 생각합니다. 해당 관련직에 관련된 직업에 대해 말씀드리겠습니다."
    job_index = []

    for index, (job_name, job_info) in enumerate(job_list.items()):
        related_job_name = job_info[1]
        contents += f"\n\n {index + 1}. {job_name}({related_job_name})"
        job_index.append(job_info[0])
    contents += "\n\n위의 직업군 중에서 조금 더 자세하게 알고 싶은 직업이 있으신가요?? 번호를 입력해주세요!"

    return {"response": contents, "job_index": job_index}

# main.py
@app.get("/api/get_job_detail/{job_code}")
async def get_job_detail(job_code: int):
    job_detail = get_detail(job_code)
    work_data_str = ' '.join(job_detail['work_data'])
    rel_job_data_str = ', '.join(job_detail['rel_job_data'])
    depart_data_str = ', '.join(job_detail['depart_data'])
    certi_data_str = ', '.join(job_detail['certi_data'])
    forcast_data_str = ' '.join(job_detail['forcast_data'])

    job_info_contents = f"요청하신 {job_detail['job_nm']} 직업에 대한 자세한 정보입니다.\n\n "
    job_info_contents += f"- 직업 정보 : {work_data_str}\n\n"
    job_info_contents += f"- 관련 직업 : {rel_job_data_str}\n\n" if rel_job_data_str != '' else ""
    job_info_contents += f"- 관련 학과 : {depart_data_str}\n\n" if depart_data_str != '' else ""
    job_info_contents += f"- 자격증 : {certi_data_str}\n\n" if certi_data_str != '' else ""
    job_info_contents += f"- 전망 : {forcast_data_str}\n\n" if forcast_data_str != '' else ""
    job_info_contents += f"- 직업 정보 URL : {job_detail['url_info']}"
    job_info_contents += "\n\n더 궁금한 사항이 있으시면 말씀해주세요!"

    return {"response": job_info_contents}