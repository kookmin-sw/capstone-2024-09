FROM python:3.10

# 패키지 리스트 업데이트 및 Java 설치
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:openjdk-r/ppa && \
    apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean;

# JAVA_HOME 환경 변수 설정
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
RUN export JAVA_HOME

RUN mkdir -p /Final_Project
WORKDIR /Final_Project
COPY ./ ./
WORKDIR ./capstone_design/fastapi_app
RUN pip3 install --upgrade pip
RUN pip3 install -r ./etc/requirement.txt

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]