import pandas as pd

df = pd.read_csv("data/Energy_Management_System_Raw_Data.csv")

print("=== Column Names ===")
print(df.columns.tolist())

print("\n=== Data Types ===")
print(df.dtypes)

if 'label' in df.columns:
    print("\n=== Label Distribution ===")
    print(df['label'].value_counts())

print("\n=== Sample Rows ===")
print(df.head())
