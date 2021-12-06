import sys; sys.path.append('..')

import os
import mysql.connector as mysql
import getpass

from mysql.connector import Error
from dotenv import load_dotenv
from utils.profiling import timeit
from utils.read_files import read_file

load_dotenv()

try:
    pwd = os.environ['MYSQL_DB_PASSWORD']
except KeyError:
    pwd = getpass.getpass()

class ToSQL:
    def __init__(self, host, user, port=None, password=pwd, database=None):
        if database is None:
            self.conn = mysql.connect(host=host, user=user, password=password, port=port)
        else:
            self.conn = mysql.connect(host=host, user=user, password=password, database=database, port=port)

    def get_conn(self):
        return self.conn

    @timeit
    def from_csv(self, files, db_name, table_name, query):
        df = read_file(files)
        try:
            if self.conn.is_connected():
                cursor = self.conn.cursor()
                cursor.execute(f"create database if not exists {db_name};")
                print(f"Database: {db_name} is created")
                cursor.execute(f"use {db_name};")
                print(f"You're connected to database: {db_name}")
                cursor.execute(f'DROP TABLE IF EXISTS {table_name};')
                print('Creating table....')
                cursor.execute(query)
                print("Table is created....")
                for i, row in df.iterrows():
                    if 'auto_increment' in query:
                        sql = f"INSERT INTO {db_name}.{table_name} VALUES {tuple({i+1}) + tuple('%s' for _ in range(len(df.columns)))}".replace("'", '')
                    else:
                        sql = f"INSERT INTO {db_name}.{table_name} VALUES {tuple('%s' for _ in range(len(df.columns)))}".replace("'", '')
                    cursor.execute(sql, tuple(row))
                    self.conn.commit()
                print(f"Success convert {files} to MySQL db")
                return
        except Error as e:
            print("Error while connecting to MySQL", e)
