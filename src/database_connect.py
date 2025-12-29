import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

user = "SA"
password = quote_plus("d@taSc1entist2025")
server = "localhost:1433"
database = "AdventureWorks2025"
driver = quote_plus("ODBC Driver 18 for SQL Server")

connection_string = (
    f"mssql+pyodbc://{user}:{password}@{server}/{database}"
    f"?driver={driver}&Encrypt=yes&TrustServerCertificate=yes"
)

engine = create_engine(connection_string)

try:
    with engine.connect():
        print("Connection to SQL server successful!")
except Exception as e:
    print("Connection to SQL server failed!", e)

def query_df(sql: str):
    with engine.connect() as con:
        return pd.read_sql(sql, con)