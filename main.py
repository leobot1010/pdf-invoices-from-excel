import pandas as pd
import glob

filepaths = glob.glob("invoices/*.xlsx")   # imports all .xlsx files in a list

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)

