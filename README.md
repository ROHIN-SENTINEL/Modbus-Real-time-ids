# TON_IoT Modbus Intrusion Detection System (IDS) 🧠⚡

A real-time, ML-powered IDS for industrial Modbus traffic. It watches a folder (`modbus_input`) for incoming `.csv` files and flags each row as ✅ Normal or ⚠️ Attack.

## 🔧 How to Run

1. Install dependencies (Python ≥ 3.9):
```bash
pip install -r requirements.txt
```

2. Start the IDS:
```bash
python main.py
```

3. Drop `.csv` files into `modbus_input/`. Each row will be classified and logged.

## 📦 Contents

- `main.py`: Real-time IDS.
- `train_model.py`: Train new Random Forest model.
- `modbus_auto_label.py`: Converts raw data to labeled format.
- `models/`: Holds `modbus_rf_model.joblib`.
- `processed/`: Automatically stores processed files.
- `utils/`: Utility functions or scripts.
- `requirements.txt`: Python dependency list.

## ✅ Output

- **Console Output**: Shows line-by-line classification.
- **detection_log.txt** *(optional)*: Log file of results.
- **Processed Files**: Automatically moved to `processed/` after analysis.

## 💬 Author

Rohin H
