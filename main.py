import pandas as pd
file_path = "C:/Users/wajee/OneDrive/Desktop/output.xlsx"
df = pd.read_excel(file_path)

print("Original DataFrame:")
print(df)
df['AQ date'] = pd.to_datetime(df['AQ date'])
df['end Aq date'] = pd.to_datetime(df['end Aq date'])

df['Validation'] = df['AQ date'] >= df['end Aq date']
print("\nDataFrame with Data Validation:")
print(df)

df['Difference'] = (df['end Aq date'] - df['AQ date']).dt.days
print("\nDataFrame with Formula:")

print(df)


df.to_excel(file_path, index=False)
