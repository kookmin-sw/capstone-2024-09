import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import requests, os

#laod env
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/Yeongchae/my_consulting_ai_model"    # 파인튜닝한 polyglot이 저장된 경로 기입
API_TOKEN = mySecret = os.environ.get('Huggingface_API_TOEKN')                   # 코드 작성자의 hugging face api 토큰 (write 권한 있음) 기입
headers = {"Authorization": f"Bearer {API_TOKEN}"}                   # ai 모델에 요청을 보낼 때, 함께 보낼 헤더 데이터 기입

st.header("🤖 학생 진로 상담 ai 챗봇")        # 웹사이트의 상단에 표시될 타이틀 작성
st.text("polyglot-ko 1.3B 기반 (학생 진로 상담 데이터로 파인튜닝)")                      # 웹사이트의 상단에 표시될 하위 타이틀 작성
st.text("상담 모델이 로딩되는데 시간이 걸리니 접속 후 약 5초 뒤에 채팅을 입력해주세요 :)")         # 웹사이트의 상단에 표시될 하위 타이틀 작성
st.text('상담을 끝내고 직업 추천을 받고 싶다면 "이제 직업을 추천해주세요"라고 채팅을 입력하세요!')         # 웹사이트의 상단에 표시될 하위 타이틀 작성

if 'generated' not in st.session_state:                         # 각 사용자 세션이 재실행 되는 경우에도 세션 간 공유될 변수를 설정
    st.session_state['generated'] = []

if 'past' not in st.session_state:                              # 각 사용자 세션이 재실행 되는 경우에도 세션 간 공유될 변수를 설정
    st.session_state['past'] = []


def query(payload):                                            # hugging face에 업로드돼 있는 대화형 ai 모델에 답변을 요청하는 함수
    response = requests.post(API_URL, headers=headers, json=payload)
    print("HTTP 상태 코드:", response.status_code)
    print("응답 내용:", response.json())
    return response.json()

def finalize(dialog):                       # 분류형 ai 모델에 그간 대화한 내용을 넘겨주어 추천 직업 카테고리를 반환받는 함수(추가)
    print(dialog)
    pass

with st.form('form', clear_on_submit=True):                     # 사용자가 채팅을 하면 그 텍스트들을 저장하는 코드
    user_input = st.text_input('You: ', '', key='input')
    submitted = st.form_submit_button('Send')

if submitted and user_input:                                    # 사용자가 채팅을 전송했고, 입력 내용이 있다면 이를 저장 후, ai 모델에 그에 대한 답변 요청
    try:
        if user_input.find("이제 직업을 추천해주세요")!=-1:         # 분류형 ai 모델에 그간 대화한 내용을 넘겨주기 위한 코드 (추가)
            # 분류형 ai 모델로 그간 대화 내용 넘겨주기
            output = finalize(user_input)
            temp = []
            for i in range(len(st.session_state.generated)):
                temp.append(st.session_state.past[i])
                temp.append(st.session_state.generated[i])
            st.session_state.dialog = temp
            print(temp)
        else:
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
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')    # 나의 채팅 내용 출력
        message(st.session_state["generated"][i], key=str(i))                       # 챗봇의 채팅 내용 출력


# 하단에는 학생이 상담 종료를 요청하면 ROBERTa에 session_state 데이터들을 넘겨줘서 ROBERTa가 추천 직업 카테고리 번호를 반환하게 코딩하면 될 듯