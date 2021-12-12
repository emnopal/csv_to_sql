def convert_datatypes(datatype):
    if datatype == 'object':
        return "TEXT"
    elif datatype == 'int64':
        return "INT"
    elif datatype == 'float64':
        return "DECIMAL(32, 5)"
    elif datatype == 'bool':
        return "BOOL"
    elif datatype == 'datetime64':
        return "DATETIME"
    else:
        return None