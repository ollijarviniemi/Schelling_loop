FROM alpine:latest

RUN apk add --no-cache python3 py3-pip bash curl

RUN apk add sudo

RUN python3 -m venv venv && source venv/bin/activate && pip install pytest

WORKDIR /app
RUN mkdir -p /app/data

COPY data /app/data
COPY shuffle_files_script.py /app/shuffle_files_script.py
COPY key.txt /app/key.txt
COPY sampling_function.py /app/main.py

CMD ["/bin/bash"]