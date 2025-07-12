import pandas as pd

def extract_function_code(hex_str):
    try:
        return int(hex_str[2:4], 16)
    except:
        return -1  # malformed

def label_from_function(func_code):
    if func_code == 3:    # Read Holding Registers
        return 0
    elif func_code == 16:  # Write Multiple Registers
        return 1
    else:
        return -1  # unknown or unsupported

# Load your raw dataset
df = pd.read_csv("data/Energy_Management_System_Raw_Data.csv", header=None)

# Rename for clarity
df.columns = ['raw_packet', 'f1', 'f2', 'f3', 'f4', 'timestamp']

# Extract and label
df['function_code'] = df['raw_packet'].apply(extract_function_code)
df['label'] = df['function_code'].apply(label_from_function)

# Filter out unknowns
df = df[df['label'] != -1]

# Save labeled output
df.to_csv("data/Energy_Management_System_LABELED.csv", index=False)
print("✅ Labeled dataset saved to: data/Energy_Management_System_LABELED.csv")
