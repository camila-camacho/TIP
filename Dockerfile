FROM python:3

ENV PORT=8080
ENV HOST=0.0.0.0
ENV PYTHONUNBUFFERED True
EXPOSE 80

WORKDIR $APP_HOME
ADD . /app
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 run:app