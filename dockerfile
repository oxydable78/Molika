FROM debian:12-slim

## part install 
RUN apt update && apt install python3 pip ssh
RUN pipx install --requirements /molika/python/requirements.txt

## part create folder
RUN mkdir -p molika/

## part copy
COPY ./python  /molika