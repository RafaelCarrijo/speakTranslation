FROM python:3.9-alpine3.18
  
WORKDIR /app

COPY * /app/

RUN pip install -U pip 
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

ENV TZ="America/Sao_Paulo" 

EXPOSE 5001
CMD uvicorn app:app --port 5001 --host 0.0.0.0
