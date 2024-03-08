FROM python:3.8.18-slim

WORKDIR /app

COPY  ./modules/ /app/modules

COPY check_pid_json_file.py /app/


CMD ["python3", "./check_pid_json_file.py"]