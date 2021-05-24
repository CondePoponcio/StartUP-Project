FROM python:3.9
ENV PYTHONNUNBUFFERED 1
RUN mkdir /code

WORKDIR /code

ENV FLASK_APP App.py

ENV FLASK_RUN_HOST 0.0.0.0

ENV FLASK_DEBUG=1

COPY requirements.txt /code/

RUN python -m pip install -r requirements.txt

COPY ./ /code/

CMD flask run -h 0.0.0.0 -p 8080