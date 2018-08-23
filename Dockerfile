FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /cvitae_api
WORKDIR /cvitae_api
ADD requirements.txt /cvitae_api
RUN pip install -r requirements.txt
ADD . /cvitae_api