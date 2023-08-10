FROM python:3.8-slim-buster

RUN apt update -y && \
    apt install awscli -y && \
    apt install -y git

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]