FROM python:3.6.1-alpine
WORKDIR /src
ADD . /src
RUN pip install -r requirements.txt
ENV FLASK_APP=src
CMD ["flask","db-init"]
CMD ["flask", "run"]
#CMD ["python","app.py"]
