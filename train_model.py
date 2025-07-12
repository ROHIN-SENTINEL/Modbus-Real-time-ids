import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

# === Step 1: Load Data ===
data_path = 'data/Energy_Management_System_LABELED.csv'
df = pd.read_csv(data_path)

# === Step 2: Preprocess ===
# Drop any non-numeric, non-informative columns
df = df.drop(columns=['raw_packet', 'timestamp'], errors='ignore')

# Drop nulls just in case
df = df.dropna()

# === Step 3: Split ===
X = df.drop(columns=['label'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Step 4: Train ===
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# === Step 5: Evaluate ===
y_pred = model.predict(X_test)
print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred))

# === Step 6: Save Model ===
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/modbus_rf_model.joblib")
print("✅ Model saved to: models/modbus_rf_model.joblib")
