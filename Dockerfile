FROM python:3.11.5

WORKDIR /app

RUN python -m venv .env
RUN /bin/bash -c "source .env/bin/activate"

COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app

CMD [ "bash", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:5000" ]