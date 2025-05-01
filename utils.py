import pandas as pd
import os

def load_file(filename):
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    if ext == ".csv":
        return pd.read_csv(filename)
    elif ext in [".xls", ".xlsx"]:
        return pd.read_excel(filename, engine="openpyxl")
    else:
        raise ValueError("Unsupported file format. Please select a .csv or .xlsx file.")
