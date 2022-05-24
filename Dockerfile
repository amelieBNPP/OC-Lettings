FROM python:3.7

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0 --chdir=./"
COPY . .

EXPOSE 8000

CMD ["gunicorn", "config.wsgi"]