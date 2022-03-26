FROM python:3.8

ENV PORT=8080
ENV HOST=0.0.0.0
ENV PYTHONUNBUFFERED True

ENV APP_HOME /app 
WORKDIR $APP_HOME
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

EXPOSE 80


CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 run:app