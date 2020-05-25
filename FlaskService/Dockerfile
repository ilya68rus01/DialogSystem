FROM python:3.6

RUN mkdir -p /usr/src/app/FlaskService/
WORKDIR /usr/src/app/FlaskService/

COPY . /usr/src/app/FlaskService/
RUN pip install flask

EXPOSE 8080

CMD ["python", "app.py" ]