FROM python:3.10
WORKDIR /api_db
COPY . ./api_db
COPY requirements.txt /api_db/
ENV PYTHONPATH "${PYTHONPATH}:/api_db/"

RUN python -m venv /opt/venv
RUN pip install --upgrade pip
RUN pip install --requirement /api_db/requirements.txt
