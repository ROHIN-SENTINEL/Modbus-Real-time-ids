# inspect_csv.py

import pandas as pd

df = pd.read_csv("data/IoT_injection_normal_modbus.csv")

print("=== Column Names ===")
print(df.columns.tolist())

if 'label' in df.columns:
    print("\n=== Unique values in 'label' ===")
    print(df['label'].unique())
else:
    print("\n⚠️ 'label' column not found.")

print("\n=== Sample Rows ===")
print(df.head())
