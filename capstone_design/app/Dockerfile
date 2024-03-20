FROM python:3.10.10
# python 3.10.12 버전의 컨테이너 이미지를 base 이미지

MAINTAINER iscmyoo <sung32114@gmail.com>

RUN mkdir -p /Final_Project
WORKDIR /Final_Project
COPY . /Final_Project

# requirements.txt 실행
RUN pip3 install --upgrade pip
RUN pip3 install -r ./capstone_design/app/etc/requirement.txt