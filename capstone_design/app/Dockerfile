FROM python:3.10.10
# python 3.10.12 버전의 컨테이너 이미지를 base 이미지

MAINTAINER iscmyoo <sung32114@gmail.com>

RUN mkdir -p /capstone_design/app
WORKDIR /capstone_design/app
COPY /capstone_design/app/ /capstone_design/app

# requirements.txt 실행
RUN pip3 install --upgrade pip
RUN pip3 install -r ./etc/requirements.txt