FROM python:2.7
MAINTAINER Alex Recker <alex@reckerfamily.com>

RUN mkdir -p /app
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

RUN mkdir -p /app/images
RUN mkdir -p /app/cache
COPY server.py /app

WORKDIR /app
EXPOSE 80
ENTRYPOINT ["gunicorn"]
CMD ["--bind", "0.0.0.0:80", "server:app"]
