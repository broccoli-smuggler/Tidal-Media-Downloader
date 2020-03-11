FROM python:slim-buster

WORKDIR /usr/src/app
COPY requirements.txt .
RUN apt update
RUN apt-get install -y build-essential ffmpeg
RUN pip3 install -r requirements.txt

COPY . .
RUN pip3 install .

EXPOSE 8000
EXPOSE 5000
CMD [ "python3", "tidal_dl/server.py", "&&", "python3", "tidal_dl/flask_server.py"]
