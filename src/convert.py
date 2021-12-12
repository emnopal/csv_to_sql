import sys; sys.path.append('..')
import re

from src.connection import Connection
from utils.read_files import read_files
from utils.datatypes import convert_datatypes
from utils.profiling import timeit

class Convert(Connection):

    NULL = "NULL"

    def __create_table(self, csv_file, table_name, columns, path, index=True):
        PATH_TO_TABLE = re.compile(r"[a-zA-Z]*")
        if not table_name:
            if "\\" in path:
                path = path.split('\\')[-1].split('.')[0]
            else:
                path = path.split('/')[-1].split('.')[0]
            table_name = "".join([i for i in PATH_TO_TABLE.findall(path) if i != ""])
        if not columns:
            if index:
                columns = f"{table_name}Index INT PRIMARY KEY AUTO_INCREMENT, "
            else:
                columns = ""
            for name, datatype in csv_file.dtypes.items():
                columns += f"{name} {convert_datatypes(datatype)} DEFAULT NULL, "
            columns = columns[:len(columns)-2]
        self.create_new_table(table_name=table_name, columns_query=columns)
        return table_name, columns

    def __insert_into_sql(self, table_name, columns, csv_file):
        for i, row in csv_file.iterrows():
            if 'AUTO_INCREMENT' in columns:
                query = f"INSERT INTO {self.get_db_name()}.{table_name} VALUES {tuple({i+1}) + tuple('%s' for _ in range(len(csv_file.columns)))}" % tuple(row)
                self.generate_query(query)
            else:
                query = f"INSERT INTO {self.get_db_name()}.{table_name} VALUES {tuple('%s' for _ in range(len(csv_file.columns)))}" % tuple(row)
                self.generate_query(query)

    @timeit
    def from_csv(self, path, table_name=None, columns=None, index=False):
        csv_file = read_files(path).fillna(self.NULL) # make sure you have clean all NaN values
        try:
            table_name, columns = self.__create_table(csv_file, table_name, columns, path, index)
            self.__insert_into_sql(table_name, columns, csv_file)
            print(f"Success insert {path} to SQL")
            return
        except Exception as e:
            raise Exception(f"Error insert {path} to SQL: {e}")
