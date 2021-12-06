import pandas as pd

def read_files(file_path, *args, **kwargs):
    if ".csv" in file_path:
        df = pd.read_csv(file_path, *args, **kwargs)
    if ".tsv" in file_path:
        df = pd.read_csv(file_path, sep='\t', *args, **kwargs)
    if ".xlsx" in file_path:
        df = pd.read_excel(file_path, *args, **kwargs)
    if ".xls" in file_path:
        df = pd.read_excel(file_path, *args, **kwargs)
    if ".txt" in file_path:
        df = pd.read_csv(file_path, *args, **kwargs)
    else:
        print("File format not supported")
    return df