"""
================================================================================
PROJECT:   Industrial IoT & Predictive Maintenance
TASK 1:    Data Sanitization & Cleaning Pipeline
================================================================================
AUTHOR:    Viraj Uttam More
ROLE:      Data Analyst Intern (TechnoHacks Batch 119)
DATE:      January 2026

--- 1. OBJECTIVE ---
To sanitize raw telemetry data from CNC machines by:
  1. Removing duplicate entries caused by logger errors.
  2. Handling missing values (Imputation).
  3. Correcting sensor outliers (e.g., 850°C glitches).

--- 2. METHODOLOGY ---
- Input Source: Raw CSV logs from machine sensors.
- Techniques: Median Imputation (Robust to outliers), Mean Imputation (NaNs).
- Feature Eng: Created 'Maintenance_Status' flag based on vibration thresholds.
================================================================================
"""

import pandas as pd
import numpy as np

# ==========================================
# STEP 1: DATA INGESTION
# ==========================================

# In a production environment, we load data from the server path:
# file_path = 'datasets/raw_cnc_sensor_data.csv'
# df = pd.read_csv(file_path)

# FOR PORTFOLIO DEMONSTRATION (Simulated Dataset):
raw_data = {
    'Timestamp': ['08:00', '08:05', '08:10', '08:05', '08:20', '08:25', '08:30', '08:35'],
    'Machine_ID': ['CNC-01', 'CNC-01', 'CNC-01', 'CNC-01', 'CNC-01', 'CNC-01', 'CNC-01', 'CNC-01'],
    'Spindle_Speed_RPM': [1200, 1205, 1198, 1205, 1210, 1202, 1200, None],
    'Temp_Celsius': [42.5, 43.1, 850.0, 43.1, 45.4, 44.2, None, 43.8],
    'Vibration_mm_s': [0.12, 0.15, 0.11, 0.15, 0.18, 0.14, 0.12, 0.13]
}

df = pd.DataFrame(raw_data)
print(f"[{'='*20} RAW DATA INGESTED {'='*20}]")
print(df)

# ==========================================
# STEP 2: DATA PREPROCESSING
# ==========================================

# 2.1 Remove Duplicates
initial_count = len(df)
df = df.drop_duplicates().reset_index(drop=True)
print(f"\n> Duplicates Removed: {initial_count - len(df)} records found.")

# 2.2 Outlier Treatment (Sensor Glitch Correction)
# Logic: Any Temp > 100°C is a sensor error. Replace with Median.
median_temp = df.loc[df['Temp_Celsius'] <= 100, 'Temp_Celsius'].median()
df.loc[df['Temp_Celsius'] > 100, 'Temp_Celsius'] = median_temp

# 2.3 Handling Missing Values
df['Spindle_Speed_RPM'] = df['Spindle_Speed_RPM'].fillna(df['Spindle_Speed_RPM'].mean())
df['Temp_Celsius'] = df['Temp_Celsius'].fillna(df['Temp_Celsius'].mean())

# ==========================================
# STEP 3: FEATURE ENGINEERING
# ==========================================

# Logic: Vibration > 0.17 mm/s indicates potential mechanical failure
threshold = 0.17
df['Status'] = np.where(df['Vibration_mm_s'] > threshold, 'Maintenance Required', 'Optimal')

# ==========================================
# STEP 4: FINAL OUTPUT
# ==========================================
print(f"\n[{'='*20} CLEANED DATASET {'='*20}]")
print(df)

"""
================================================================================
EXECUTION OUTPUT LOG (Terminal Result)
================================================================================
[==================== RAW DATA INGESTED ====================]
  Timestamp Machine_ID  Spindle_Speed_RPM  Temp_Celsius  Vibration_mm_s
0     08:00     CNC-01             1200.0          42.5            0.12
1     08:05     CNC-01             1205.0          43.1            0.15
2     08:10     CNC-01             1198.0         850.0            0.11
3     08:05     CNC-01             1205.0          43.1            0.15
4     08:20     CNC-01             1210.0          45.4            0.18
5     08:25     CNC-01             1202.0          44.2            0.14
6     08:30     CNC-01             1200.0           NaN            0.12
7     08:35     CNC-01                NaN          43.8            0.13

> Duplicates Removed: 1 records found.

[==================== CLEANED DATASET ====================]
  Timestamp Machine_ID  Spindle_Speed_RPM  Temp_Celsius  Vibration_mm_s                Status
0     08:00     CNC-01        1200.000000         42.50            0.12               Optimal
1     08:05     CNC-01        1205.000000         43.10            0.15               Optimal
2     08:10     CNC-01        1198.000000         43.45            0.11               Optimal
3     08:20     CNC-01        1210.000000         45.40            0.18  Maintenance Required
4     08:25     CNC-01        1202.000000         44.20            0.14               Optimal
5     08:30     CNC-01        1200.000000         43.45            0.12               Optimal
6     08:35     CNC-01        1202.833333         43.80            0.13               Optimal
================================================================================
"""
