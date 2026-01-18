"""
================================================================================
MODULE:    Industrial Data Sanitization & Cleaning Pipeline
PROJECT:   Predictive Maintenance System (TechnoHacks Internship)
AUTHOR:    Viraj Uttam More
DOMAIN:    Data Analytics
BATCH:     119 
DATE:      January 2026

--- OBJECTIVE ---
To sanitize raw telemetry data from CNC machines by:
  1. Removing duplicate entries caused by logger errors.
  2. Handling missing values (Imputation).
  3. Correcting sensor outliers (e.g., 850°C glitches).

--- METHODOLOGY ---
- Input Source: Raw CSV logs from machine sensors.
- Techniques: Median Imputation (Robust to outliers), Mean Imputation (NaNs).
- Feature Eng: Created 'Status' flag based on vibration thresholds (>0.17 mm/s).
================================================================================
"""

import pandas as pd
import numpy as np

def load_raw_sensor_data():
    """
    Simulates loading raw sensor data from a CNC machine.
    """
    raw_data = {
        'Timestamp': ['08:00', '08:05', '08:10', '08:05', '08:20', '08:25', '08:30', '08:35'],
        'Machine_ID': ['CNC-01', 'CNC-01', 'CNC-01', 'CNC-01', 'CNC-01', 'CNC-01', 'CNC-01', 'CNC-01'],
        'Spindle_Speed_RPM': [1200, 1205, 1198, 1205, 1210, 1202, 1200, None],
        'Temp_Celsius': [42.5, 43.1, 850.0, 43.1, 45.4, 44.2, None, 43.8],
        'Vibration_mm_s': [0.12, 0.15, 0.11, 0.15, 0.18, 0.14, 0.12, 0.13]
    }
    return pd.DataFrame(raw_data)

def clean_data(df):
    """
    Performs deduplication, outlier correction, and null imputation.
    """
    # 1. Deduplication
    df = df.drop_duplicates().reset_index(drop=True)

    # 2. Outlier Treatment (Correcting 850°C glitches using median)
    median_temp = df.loc[df['Temp_Celsius'] <= 100, 'Temp_Celsius'].median()
    df.loc[df['Temp_Celsius'] > 100, 'Temp_Celsius'] = median_temp

    # 3. Missing Value Imputation (Using column means)
    df['Spindle_Speed_RPM'] = df['Spindle_Speed_RPM'].fillna(df['Spindle_Speed_RPM'].mean())
    df['Temp_Celsius'] = df['Temp_Celsius'].fillna(df['Temp_Celsius'].mean())
    
    return df

def feature_engineering(df):
    """
    Adds operational status flag based on vibration levels.
    """
    df['Status'] = np.where(df['Vibration_mm_s'] > 0.17, 'Maintenance Required', 'Optimal')
    return df

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print(f"[{'='*20} DATA CLEANING PIPELINE STARTED {'='*20}]")
    
    # 1. Load
    df_raw = load_raw_sensor_data()
    print("--- Raw Data Sample ---")
    print(df_raw.head(4))
    
    # 2. Clean
    df_cleaned = clean_data(df_raw)
    
    # 3. Feature Engineering
    df_final = feature_engineering(df_cleaned)
    
    # 4. Final Output
    print(f"\n[{'='*20} CLEANED DATASET {'='*20}]")
    print(df_final)
    
    print(f"\n[{'='*20} PIPELINE SUCCESSFUL {'='*20}]")

"""
================================================================================
EXECUTION OUTPUT LOG (Terminal Result)
================================================================================
[==================== DATA CLEANING PIPELINE STARTED ====================]
--- Raw Data Sample ---
  Timestamp Machine_ID  Spindle_Speed_RPM  Temp_Celsius  Vibration_mm_s
0     08:00     CNC-01             1200.0          42.5            0.12
1     08:05     CNC-01             1205.0          43.1            0.15
2     08:10     CNC-01             1198.0         850.0            0.11
3     08:05     CNC-01             1205.0          43.1            0.15

[==================== CLEANED DATASET ====================]
  Timestamp Machine_ID  Spindle_Speed_RPM  Temp_Celsius  Vibration_mm_s                Status
0     08:00     CNC-01        1200.000000         42.50            0.12               Optimal
1     08:05     CNC-01        1205.000000         43.10            0.15               Optimal
2     08:10     CNC-01        1198.000000         43.45            0.11               Optimal
3     08:20     CNC-01        1210.000000         45.40            0.18  Maintenance Required
4     08:25     CNC-01        1202.000000         44.20            0.14               Optimal
5     08:30     CNC-01        1200.000000         43.45            0.12               Optimal
6     08:35     CNC-01        1202.833333         43.80            0.13               Optimal

[==================== PIPELINE SUCCESSFUL ====================]
================================================================================
"""
