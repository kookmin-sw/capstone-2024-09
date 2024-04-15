FROM python:3.10-alpine
RUN mkdir -p /Final_Project
WORKDIR /Final_Project
COPY . ./
RUN pip3 install --upgrade pip
RUN pip3 install -r ./capstone_design/app/etc/requirement.txt
RUN chmod +x ./app/app.py
EXPOSE 5000

CMD ["python3", "./app/app.py"]