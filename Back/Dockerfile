FROM python:3.8
  
WORKDIR /app

COPY * /app/

RUN pip install -U pip 
RUN pip install --no-cache-dir -r requirements.txt
# unica forma de garantir que instala o whisper correto
RUN pip install -U openai-whisper

# Atualize o sistema e instale as dependências necessárias
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

ENV TZ="America/Sao_Paulo" 

EXPOSE 5001
CMD uvicorn app:app --port 5001 --host 0.0.0.0

