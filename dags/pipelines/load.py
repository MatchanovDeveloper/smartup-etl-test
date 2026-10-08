# import psycopg2
import pandas as pd
import json
from config import db_url
from sqlalchemy import create_engine

engine = create_engine(db_url)

def loader(df: pd.DataFrame, table_name:str, conn=engine):

    if df.empty:
        print("Bu jadval bo'sh!")
        return

    df.to_sql(table_name, con=conn, if_exists='replace', index=False)
