FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["uvicorn","main:app","--reload","--port=8000","--host=0.0.0.0"]