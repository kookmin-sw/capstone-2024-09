FROM python:3.10

RUN apt-get update && \
    apt-get install -y ca-certificates wget && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz && \
    tar -xzf openjdk-11.0.2_linux-x64_bin.tar.gz && \
    rm openjdk-11.0.2_linux-x64_bin.tar.gz

ENV JAVA_HOME=/jdk-11.0.2/
ENV LD_LIBRARY_PATH=$JAVA_HOME/lib/server
RUN ln -s /jdk-11.0.2/lib/server/libjvm.so /usr/lib/libjvm.so

RUN mkdir -p /Final_Project
WORKDIR /Final_Project
COPY ./ ./
WORKDIR ./capstone_design/fastapi_app
RUN pip3 install --upgrade pip
RUN pip3 install -r ./etc/requirement.txt

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]