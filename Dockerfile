FROM python:3.7

WORKDIR /app

ENV PORT=8000

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "config.wsgi", "--bind 0.0.0.0:$PORT"]