FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD req.txt /code/
RUN pip install -r req.txt
ADD ./. /code/

EXPOSE 8000
