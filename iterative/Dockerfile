FROM python:3.6-slim

COPY . /code
WORKDIR /code

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

ENTRYPOINT python ./mypackage/run.py