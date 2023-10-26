FROM python
  
WORKDIR /app

COPY * /app/

RUN pip install -U pip 
RUN pip install --no-cache-dir -r requirements.txt


ENV TZ="America/Sao_Paulo" 

EXPOSE 5001
CMD uvicorn app:app --port 5001 --host 0.0.0.0
