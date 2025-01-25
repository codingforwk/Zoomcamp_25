#!/usr/bin/env python
# coding: utf-8
import os
import argparse
from sqlalchemy import create_engine
import pandas as pd
import subprocess


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    database = params.database
    table_name = params.table_name
    url = params.url
    file_name = 'output.parquet'

    subprocess.run(f"wget {url} -O {file_name}", shell=True, check=True)



    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

    df = pd.read_parquet(file_name, engine='pyarrow')

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    pd.io.sql.get_schema(df, name=table_name)

    pd.to_datetime(df.tpep_pickup_datetime)

    print(pd.io.sql.get_schema(df, name=table_name))

    print(pd.io.sql.get_schema(df, name = table_name, con=engine))

    df = pd.read_parquet('output.parquet')

    len(df)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name,con = engine,if_exists='replace')

    df.to_sql(name=table_name,con = engine,if_exists='append')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Ingest parquet data to postgres')

    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--database', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table  for postgres')
    parser.add_argument('--url', help='url for parquet')

    args = parser.parse_args()

main(args)










