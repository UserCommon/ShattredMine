FROM python:3.12.2-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install packages
RUN apt update -y && apt upgrade -y
RUN apt install openssl libssl-dev -y


# working dir
WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

COPY ./static /home/django/www-data/shattredmine/static
