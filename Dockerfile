FROM python:3.9-slim-buster

COPY aws_requirements.txt /tmp
RUN mkdir -p /src
RUN pip install -t src/vendor -r /tmp/aws_requirements.txt
COPY src/ /src/
RUN pip install -e /src
COPY tests/ /tests/

WORKDIR /src
CMD flask run --host=0.0.0.0 --port=80
