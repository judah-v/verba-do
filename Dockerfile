FROM python:3.14.8-alpine3.24

WORKDIR /apps

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80
CMD ["python", "manage.py", "runserver"]
