FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 80

CMD ["python3", "app.py"]
