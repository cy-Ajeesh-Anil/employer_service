FROM nathanaelanil/inscholaris_base_python:1.0
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV prod

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "manage.py", "run"]