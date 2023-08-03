FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# RUN python manage.py makemigrations && python manage.py migrate

# WORKDIR /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

VOLUME ["/app"]
