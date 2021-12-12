import pandas as pd

from utils.exceptions import FileNotSupported

def read_files(file_path, *args, **kwargs):
    if ".csv" in file_path:
        df = pd.read_csv(file_path, *args, **kwargs)
    elif ".tsv" in file_path:
        df = pd.read_csv(file_path, sep='\t', *args, **kwargs)
    elif ".xlsx" in file_path:
        df = pd.read_excel(file_path, *args, **kwargs)
    elif ".xls" in file_path:
        df = pd.read_excel(file_path, *args, **kwargs)
    elif ".txt" in file_path:
        df = pd.read_csv(file_path, *args, **kwargs)
    else:
        raise FileNotSupported("File format not supported")
    return df