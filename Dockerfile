FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY app.py app.py

COPY __main__.py __main__.py

CMD ["python3", "."]
