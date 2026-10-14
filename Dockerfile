FROM python:3.14.8-alpine3.24
LABEL org.opencontainers.image.source=https://github.com/judah-v/verba-do

WORKDIR /apps

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80
CMD ["python", "manage.py", "runserver"]
