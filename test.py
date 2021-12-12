import os
from src.convert import Convert
from dotenv import load_dotenv

load_dotenv()

host = os.environ['HOST']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
database = os.environ['DATABASE']

conn = Convert(host=host, user=username, password=password, database=database)
conn.from_csv(path='csv_test.csv')
