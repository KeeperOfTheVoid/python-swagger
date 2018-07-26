FROM python:3

ADD app.py /

RUN pip install flask

RUN pip install flask_restplus

CMD [ "python", "./app.py" ]