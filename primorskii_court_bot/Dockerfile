FROM python:3.10
WORKDIR /primorskii_court_bot
COPY . ./primorskii_court_bot
COPY requirements.txt /primorskii_court_bot/
ENV PYTHONPATH "${PYTHONPATH}:/primorskii_court_bot/"

RUN python -m venv /opt/venv
RUN pip install --upgrade pip
RUN pip install --requirement /primorskii_court_bot/requirements.txt
