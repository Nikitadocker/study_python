FROM python:3.8.18-slim

WORKDIR /app

COPY  ./modules/ /app/modules

COPY psutil_pid_create_json.py /app/

RUN pip install psutil

ENV GET_METHOD psutil

CMD ["python3", "./psutil_pid_create_json.py"]