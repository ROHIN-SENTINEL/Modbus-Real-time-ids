import pandas as pd
import os
import time
import joblib
from sklearn.exceptions import NotFittedError

# === CONFIG ===
MODEL_PATH = "models/modbus_rf_model.joblib"
INPUT_FOLDER = "modbus_input"
PROCESSED_FOLDER = "processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# === Load Trained Model ===
print("🔄 Loading model and initializing...")
try:
    model = joblib.load(MODEL_PATH)
except (FileNotFoundError, NotFittedError):
    print("❌ ERROR: Trained model not found or invalid.")
    exit(1)

print(f"✅ IDS is active. Watching folder: {INPUT_FOLDER}\n")

def extract_function_code(hex_str):
    try:
        return int(hex_str[2:4], 16)
    except:
        return -1

def predict_file(file_path):
    try:
        df = pd.read_csv(file_path, header=None)
        df.columns = ['raw_packet', 'f1', 'f2', 'f3', 'f4', 'timestamp']

        df['function_code'] = df['raw_packet'].apply(extract_function_code)

        # Drop all non-feature columns
        features = ['f1', 'f2', 'f3', 'f4', 'function_code']
        df = df[features]

        # Predict
        preds = model.predict(df)

        for i, pred in enumerate(preds):
            print(f"[{os.path.basename(file_path)}] Row {i}: {'⚠️ ATTACK' if pred == 1 else '✅ Normal'}")

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")


def run_monitor_loop():
    seen = set()
    while True:
        files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith('.csv')]
        for f in files:
            full_path = os.path.join(INPUT_FOLDER, f)
            if f not in seen:
                print(f"\n📥 Processing: {f}")
                predict_file(full_path)
                seen.add(f)

                # Move to processed folder
                os.rename(full_path, os.path.join(PROCESSED_FOLDER, f))

        time.sleep(2)  # Poll every 2 seconds

if __name__ == "__main__":
    run_monitor_loop()
