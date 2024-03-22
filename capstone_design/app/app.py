import streamlit as st
from streamlit_chat import message
import requests

API_URL = "https://api-inference.huggingface.co/models/EleutherAI/polyglot-ko-1.3b"    # polyglot이 저장된 경로 기입
API_TOKEN = "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"                  # 코드 작성자의 hugging face api 토큰 (write 권한 있음) 기입
headers = {"Authorization": f"Bearer {API_TOKEN}"}                   # ai 모델에 요청을 보낼 때, 함께 보낼 헤더 데이터 기입

st.header("🤖학생 진로 상담 ai 챗봇 \n(polyglot-ko-1.3B 기반)")          # 웹사이트의 상단에 표시될 타이틀 작성

if 'generated' not in st.session_state:                         # 각 사용자 세션이 재실행 되는 경우에도 세션 간 공유될 변수를 설정
    st.session_state['generated'] = []

if 'past' not in st.session_state:                              # 각 사용자 세션이 재실행 되는 경우에도 세션 간 공유될 변수를 설정
    st.session_state['past'] = []


def query(payload):                                            # hugging face에 업로드돼 있는 ai 모델에 특정 데이터를 요청하는 함수
    response = requests.post(API_URL, headers=headers, json=payload)
    print("HTTP 상태 코드:", response.status_code)
    print("응답 내용:", response.json())
    return response.json()


with st.form('form', clear_on_submit=True):                     # 사용자가 채팅을 하면 그 텍스트들을 저장하는 코드
    user_input = st.text_input('You: ', '', key='input')
    submitted = st.form_submit_button('Send')

if submitted and user_input:                                    # 사용자가 채팅을 전송했고, 입력 내용이 있다면 이를 저장 후, ai 모델에 그에 대한 답변 요청
    try:
        output = query(user_input)
        #{
        #     "inputs": {
        #         "past_user_inputs": st.session_state.past,
        #         "generated_responses": st.session_state.generated,
        #         "text": user_input,
        #     },
        #     "parameters": {"repetition_penalty": 1.33},
        #}
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output[0]["generated_text"])
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if st.session_state['generated']:                               # ai 모델의 응답 내용이 존재한다면 하단에 메시지 형식으로 출력
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))


# 하단에는 session_state['past']의 길이가 몇 이상이면 ROBERTa에 session_state 데이터들을 넘겨줘서 ROBERTa가 추천 직업 카테고리 번호를 반환하게 코딩하면 될 듯