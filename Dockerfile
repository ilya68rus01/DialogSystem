FROM python:3.6

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install flask

EXPOSE 8080

CMD ["python", "app.py" ]