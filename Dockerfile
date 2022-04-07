FROM python:3.9-slim

COPY . /app

WORKDIR /app

RUN pip3 install --user -r requirements.txt
RUN python3 -m flask db init
RUN python3 -m flask db migrate
RUN python3 -m flask db upgrade

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
