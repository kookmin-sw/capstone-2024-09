FROM python:3.10

RUN mkdir -p /Final_Project
WORKDIR /Final_Project
COPY . ./
RUN pip3 install --upgrade pip
RUN pip3 install -r ./etc/requirement.txt


EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]