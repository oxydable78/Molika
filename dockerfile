FROM debian:12-slim

## part install 
RUN apt update && apt install -y python3 pip
#RUN pip install --requirements /molika/python/requirements.txt

## part create folder
RUN mkdir -p molika/log

## part copy
COPY ./python  /molika/python
#COPY ./config  /molika/config

RUN echo "alias molika='python3 /molika/python/Molika.py'" >> /root/.bashrc