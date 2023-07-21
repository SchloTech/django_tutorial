FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/mypage
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

VOLUME ["/app"]
