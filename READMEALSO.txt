ANOMALY-BASED INTRUSION DETECTION SYSTEM FOR MODBUS TRAFFIC IN HYBRID POWER INFRASTRUCTURE



-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-8--8-8-8-8-8-8-8-8-8-8-8-8-8-8-8-



SMALL DESCRIPTION ABT THE FILES INSIDE

main.py: Real-time IDS. (only using VSCODE)

train_model.py: Train new Random Forest model.

modbus_auto_label.py: Converts raw data to labeled format.

models/: Holds modbus_rf_model.joblib.

processed/: Automatically stores processed files.(I mean the converted  unlabled messed up file(Energy_Management_System_Raw_Data) to labled clean dataset)

utils/: Utility functions or scripts.


FOR TESTING THE IDS INSTALL THE NECESSARY DEPENDENCIES

MAKE SURE THE SAMPLE IS INSIDE THE "modbus_input"

IF U DONT HAVE A SAMPLE DATA, U CAN GET IT FROM "TON_IoT\models" --->>>
CHOOSE "Energy_Management_System_Raw_Data.csv" AND PASTE IT IN "modbus_input" 

AND THEN RUN IT

#note this is not a real time ids as running this ids cant monitor ur system network traffic in real time, it only monitors a specific folder(modbus_input).#

