FROM python:3
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY ./flask_backend.py /app/flask_backend.py
CMD python ./flask_backend.py