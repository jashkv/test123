FROM python:3.9-slim

WORKDIR /app

COPY app.py /app/

RUN pip install requests

RUN mkdir -p /report

CMD ["python", "app.py"]
