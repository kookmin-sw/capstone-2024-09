FROM openjdk:11-jdk

# 파이썬 설치
RUN apt-get update && apt-get install -y python3 python3-pip

# 작업 디렉터리 설정
RUN mkdir -p /Final_Project
WORKDIR /Final_Project

# 소스 코드 복사
COPY ./ ./

# 작업 디렉터리 변경
WORKDIR /Final_Project/capstone_design/fastapi_app

# pip 업그레이드 및 의존성 설치
RUN pip3 install --upgrade pip
RUN pip3 install -r ./etc/requirement.txt

# 포트 노출
EXPOSE 5000

# 애플리케이션 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]