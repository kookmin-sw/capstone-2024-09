# 1. 프로젝트 소개

**팀페이지 주소** -> https://kookmin-sw.github.io/capstone-2024-09

### 학생의 진로 상담해주는 ai 모델 서비스
챗봇을 활용하여 학생들의 진로 상담을 진행하고, 상담을 통해 수집한 데이터를 기반으로 학생에게 적합한 직업을 추천해주며, 해당 직업의 현재 수요, 전망, 준비 과정 등 보다 구체적인 데이터를 제공함으로서 진로 상담을 진행하는 서비스 입니다.

### Abstract
We use chatbots to provide career counseling to students, recommend jobs they prefer based on data collected through counseling, and provide career counseling to obtain data on the current demand, views, and treatment process of the job. This is an ongoing service.

## ⚙ 기술 스택
### 🖥 Front-End
<img alt="React" src ="https://img.shields.io/badge/react-2A2A2A.svg?&style=for-the-badge&logo=react&logoColor=blue"/>

### 🖥 Back-End
<img alt="streamlit" src="https://img.shields.io/badge/fastapi-FFFFFF.svg?&style=for-the-badge&logo=fastapi&logoColor=red"/>  \
<img alt="AWS" src="https://img.shields.io/badge/AWS EC2-FF9900.svg?&style=for-the-badge&logo=amazonec2&logoColor=green"/> <img alt="AWS" src="https://img.shields.io/badge/AWS RDS-527FFF.svg?&style=for-the-badge&logo=amazonrds&logoColor=green"/> <img alt="mysql" src="https://img.shields.io/badge/Mysql-4479a1.svg?&style=for-the-badge&logo=mysql&logoColor=white"/>  \
<img alt="GHCR" src="https://img.shields.io/badge/GHCR-181717.svg?&style=for-the-badge&logo=github&logoColor=white"/> <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED.svg?&style=for-the-badge&logo=Docker&logoColor=white"/> <img alt="github action" src="https://img.shields.io/badge/Github Actions-2088FF.svg?&style=for-the-badge&logo=Github Actions&logoColor=white"/>

### 🖥 AI
<img alt="scikit learn" src="https://img.shields.io/badge/scikit  learn-F7931E.svg?style=for-the-badge&logo=scikitlearn&logoColor=white"> <img src="https://img.shields.io/badge/Open Ai-412991?style=for-the-badge&logo=openai&logoColor=white"> <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">\
<img src="https://img.shields.io/badge/google colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"> <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/json-000000?style=for-the-badge&logo=json&logoColor=white">

### 🖥 협업
<img alt="Html" src ="https://img.shields.io/badge/github-181717.svg?&style=for-the-badge&logo=github&logoColor=white"/> <img alt="Html" src ="https://img.shields.io/badge/Notion-000000.svg?&style=for-the-badge&logo=Notion&logoColor=white"/> <img alt="Html" src ="https://img.shields.io/badge/Slack-4A154B.svg?&style=for-the-badge&logo=Slack&logoColor=white"/>

## 서비스 구조
![image](https://github.com/kookmin-sw/capstone-2024-09/assets/61531215/a150ab0d-0d62-4175-84c3-5f854710ff5c)


# 2. 소개 영상

[![Video Label](http://img.youtube.com/vi/tx8chBLjQVg/0.jpg)](https://youtu.be/tx8chBLjQVg?t=0s)

# 3. 👩‍👩‍👧‍👧 팀 소개

|이름|역할|주소|
|------|---|---|
|서영채(****1630)|AI, 프론트엔드|https://github.com/Seo-yeong-Chae|
|유성환(****2240)|백엔드, 협업 관리|https://github.com/ISCMSHY|


# 4. 사용법
## 서비스 사용
**서비스 접속 도메인** : http://capstone.sung4854.com

**1. 사이트 접속 후 기존 챗봇과 동일하게 진로 상담 내용을 작성하시면 됩니다.**
![image](https://github.com/kookmin-sw/capstone-2024-09/assets/61531215/6dffa9af-1901-4445-904e-ce398626526f)

**2. 어느정도 진로 상담을 한 뒤 직업을 추천 받고 싶으면 "직업을 추천해주세요"라는 문구를 작성하면 직업을 추천해줍니다.**
![image](https://github.com/kookmin-sw/capstone-2024-09/assets/61531215/4d27e2dd-1560-42db-b2b8-fd192a4bdf9b)

**3. 추천 받은 직업 중 더 자세하게 알고 싶은 직업의 경우 번호를 입력하면 직업에 대한 자세한 정보를 제공해줍니다.**
![image](https://github.com/kookmin-sw/capstone-2024-09/assets/61531215/02602319-c086-474b-93ea-b3ae458ce4d1)



## 서비스 구축
### Ubuntu 환경
#### Docker Install
```
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo systemctl status docker
```

#### Docker compose Install
**버전의 경우 아래 사이트 접속하여 최신 버전으로 설치하시면 됩니다**\
*https://github.com/docker/compose/releases*
```
sudo curl -L https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

#### React 및 FastAPI Docker iamge 받기
```
# React image
docker pull iscmyoo/capstone_design-react:latest
docker tag iscmyoo/capstone_design-react:latest capstone_design-react:latest
docker rmi -f iscmyoo/capstone_design-react:latest

# FastAPI image
docker pull iscmyoo/capstone_design-fastapi:latest
docker tag iscmyoo/capstone_design-fastapi:latest capstone_design-fastapi:latest
docker rmi -f iscmyoo/capstone_design-fastapi:latest
```

#### 서비스에 필요한 환경변수 세팅
**환경변수 세팅에 앞서 Open AI API와 커리어넷 API 토큰이 필요합니다. 아래 링크를 통해 API 토큰 발급 받으세요**\
**Open AI : https://openai.com/** \
**커리어넷 : https://www.career.go.kr/cnet/front/openapi/openApiUseGuideCenter.do** 

**또한 AWS RDS 서비스를 이용하기에 세팅이 필요하다.**\
**RDS 세팅의 경우 아래 블로그를 참고하자**\
*https://cloud-oky.tistory.com/976*

**API 토큰과 RDS 설정에서 사용자, 비밀번호, 접속 Host, DB 이름을 설정했으면 아래와 같이 .env 환경변수 파일을 만들어 해당 내용을 저장한다.**
```
# API environments
OPENAI_API_KEY = [OPEN AI 토큰]
career_api_key = [커리어넷 토큰]
REACT_APP_API_BASE_URL = [fastapi 서버가 구동되는 서버 주소]

# DB environments
DB_USER = [DB 사용자 이름]
DB_PASSWORD = [DB 사용자 비밀번호]
DB_HOST = [DB Host 주소] # 블로그 내용 참고
DB_NAME = [사용하는 DB 이름]
```

#### CORS 문제 해결
**서버 구축 시 CORS 문제로 인해 설정 일부분을 변경해야 한다.** \
파일 경로 : /fastapi_app/package.json
```
"proxy": [fastapi 접속 주소]
```

#### 다운 받은 이미지를 기반으로 컨테이너 생성
```
docker-compose -f docker-compose.yml --env-file .env up --build -d
```

**위와 같이 수행하면 컨테이너 환경의 React와 FastAPI가 구축되고 서비스를 구축할 수 있다.**

# 5. 기타

## 중간발표자료
https://drive.google.com/drive/folders/1T09Pt0a32KGpKNjoF0JSmD79XqslpZvq?usp=sharing

## 포스터
![2024 9팀 캡스톤 포스터](https://github.com/kookmin-sw/capstone-2024-09/assets/29187870/b1f0cc9c-50f4-4126-bf81-e9667d02478d)
