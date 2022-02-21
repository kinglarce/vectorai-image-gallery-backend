FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./init_db.py /code/init_db.py

RUN python init_db.py

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]