FROM python:3.9.2
ENV PYTHONUNBUFFERED=1
RUN apt-get update
RUN apt install sqlite3
WORKDIR /code
COPY requirements-dev.txt /code/
COPY requirements.txt /code/
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements-dev.txt
COPY . /code/
