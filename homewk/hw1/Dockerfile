FROM python:3.12.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow


WORKDIR /app
COPY ingest-hw1.py ingest-hw1.py

CMD [ "python", "ingest-hw1.py" ]