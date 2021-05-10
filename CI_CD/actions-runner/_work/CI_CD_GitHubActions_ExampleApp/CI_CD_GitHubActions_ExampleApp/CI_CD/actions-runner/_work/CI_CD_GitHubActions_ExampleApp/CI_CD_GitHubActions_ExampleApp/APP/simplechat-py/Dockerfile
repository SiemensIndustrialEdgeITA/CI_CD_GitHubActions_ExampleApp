FROM python:3.7-alpine

WORKDIR /app

COPY app/ ./
RUN pip install -r requirements.txt

CMD [ "python", "./chat.py"]
#CMD [ "tail", "-f", "/dev/null"]