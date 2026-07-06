import pandas as pd

df = pd.read_excel(
    r"C:\Users\anwar\Desktop\Report\RX_DATA.xls", engine="xlrd"
)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print(df)
