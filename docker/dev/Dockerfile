FROM ubuntu:16.04
MAINTAINER Raju Dawadi <rajudawadinp@gmail.com>

RUN apt-get update && \
    apt-get install -qy python-virtualenv python-dev curl nano

RUN virtualenv /venv && \
    . /venv/bin/activate && \
    pip install pip --upgrade

COPY scripts/entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh

COPY src /application

WORKDIR /application

ENTRYPOINT ["entrypoint.sh"]

ENV DJANGO_ALLOWED_HOSTS "0.0.0.0"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]