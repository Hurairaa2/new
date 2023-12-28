import pandas as pd
import openpyxl
dfs = pd.read_excel(r"C:\Users\wajee\OneDrive\Desktop\output.xlsx",sheet_name=["Sheet1","Sheet2"])
print(dfs)
