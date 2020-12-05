# pull official base image
FROM python:3.5

# set environment variables
# PYTHONDONTWRITEBYTECODE Prevents Python from writing pyc files to disc 
# PYTHONUNBUFFERED Prevents Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set working directory 
# ADD deepsea_test /apps/deepsea_test
# RUN chown -R www-data:www-data /apps

WORKDIR /apps/deepsea_test

# install dependencies

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt 






