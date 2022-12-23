FROM python:3.10
WORKDIR /alert_status
COPY . ./alert_status
COPY requirements.txt /alert_status/
ENV PYTHONPATH "${PYTHONPATH}:/alert_status/"

RUN python -m venv /opt/venv
RUN pip install --upgrade pip
RUN pip install --requirement /alert_status/requirements.txt
