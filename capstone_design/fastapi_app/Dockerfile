FROM python:3.10

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository "deb http://security.ubuntu.com/ubuntu focal-security main" && \
    apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

RUN mkdir -p /Final_Project
WORKDIR /Final_Project
COPY ./ ./
WORKDIR ./capstone_design/fastapi_app
RUN pip3 install --upgrade pip
RUN pip3 install -r ./etc/requirement.txt

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]