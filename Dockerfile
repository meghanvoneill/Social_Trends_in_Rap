# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD exec gunicorn --bind :5000 --workers 1 --threads 8 --timeout 0 main:app

# EXPOSE 5000
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]