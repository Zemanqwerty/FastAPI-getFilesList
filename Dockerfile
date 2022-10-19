FROM python:3.6

COPY . /src

COPY ./requirements.txt /src/requirements.txt

WORKDIR src

EXPOSE 8000:8000

RUN pip install fastapi uvicorn

CMD [ "python", "main.py" ]