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
**서비스 접속 도메인** => http://capstone.sung4854.com
*사이트 접속 시 기존 챗봇 사용과 동일하게 사용하시면 됩니다*
*추 후 자세한 사용 사진과 설명 추가 예정*

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
추 후 작성 예정

# 5. 기타

## 중간발표자료
https://drive.google.com/drive/folders/1T09Pt0a32KGpKNjoF0JSmD79XqslpZvq?usp=sharing

## 포스터
![2024 9팀 캡스톤 포스터](https://github.com/kookmin-sw/capstone-2024-09/assets/29187870/b1f0cc9c-50f4-4126-bf81-e9667d02478d)
