# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

ENV PORT 8989

WORKDIR /app

COPY requirements.txt requirements.txt

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8900

CMD exec gunicorn --bind :$PORT --workers 1 --threads 2 --timeout 0 app:app

# EXPOSE 5000
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]