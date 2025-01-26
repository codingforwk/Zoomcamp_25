import os
import argparse
import pandas as pd
from sqlalchemy import create_engine


def main(params):
    # Unpack parameters
    user, password, host, port, db, table_name, url, second_url = (
        params.user, params.password, params.host, 
        params.port, params.db, params.table_name, params.url, params.second_url
    )
    
    # Download and process the first CSV
    csv_name = 'output.csv.gz' if url.endswith('.csv.gz') else 'output.csv'
    os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    # Load the first CSV into a DataFrame
    df = pd.read_csv(csv_name)
    
    # Process datetime columns if necessary for the first CSV
    df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
    df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])

    # Insert the first CSV into the Postgres table
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

    # Download and process the second CSV (different table)
    second_csv_name = 'second_output.csv.gz' if second_url.endswith('.csv.gz') else 'second_output.csv'
    os.system(f"wget {second_url} -O {second_csv_name}")

    # Load the second CSV into a DataFrame (no datetime columns to process)
    df2 = pd.read_csv(second_csv_name)

    # Insert the second CSV into a different table (e.g., 'zones')
    df2.to_sql(name='zones', con=engine, if_exists='replace', index=False)


if __name__ == '__main__':
    # Argument parsing
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    parser.add_argument('--user', required=True)
    parser.add_argument('--password', required=True)
    parser.add_argument('--host', required=True)
    parser.add_argument('--port', required=True)
    parser.add_argument('--db', required=True)
    parser.add_argument('--table_name', required=True)
    parser.add_argument('--url', required=True)
    parser.add_argument('--second_url', required=True, help="URL of the second CSV")

    args = parser.parse_args()
    main(args)
