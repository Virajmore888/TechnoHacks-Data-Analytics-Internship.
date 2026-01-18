"""
--------------------------------------------------------------------------------
TASK 1: Industrial Data Sanitization & Cleaning
--------------------------------------------------------------------------------
Author: Viraj Uttam More
Batch:  119 (TechnoHacks Internship)
Domain: Data Science & Analytics

OBJECTIVE:
The goal is to sanitize raw sensor data by removing duplicates, handling missing 
values, and correcting sensor outliers (glitches) to prepare it for analysis.

METHODOLOGY:
1. Duplicate Removal: Eliminated repeated timestamps.
2. Outlier Treatment: Replaced unrealistic temp spikes (850°C) with Median value.
3. Imputation: Filled missing RPM and Temp values using Column Mean.
4. Feature Engineering: Created a 'Status' flag for maintenance alerts.

EXPECTED OUTPUT:
- Cleaned dataset with no null values.
- New 'Status' column added.
--------------------------------------------------------------------------------
"""

import pandas as pd
import numpy as np

# --- 1. Load Raw Sensor Data ---
raw_data = {
    'Timestamp': ['08:00', '08:05', '08:10', '08:05', '08:20', '08:25', '08:30', '08:35'],
    'Machine_ID': ['CNC-01', 'CNC-01', 'CNC-01', 'CNC-01', 'CNC-01', 'CNC-01', 'CNC-01', 'CNC-01'],
    'Spindle_Speed_RPM': [1200, 1205, 1198, 1205, 1210, 1202, 1200, None],
    'Temp_Celsius': [42.5, 43.1, 850.0, 43.1, 45.4, 44.2, None, 43.8],
    'Vibration_mm_s': [0.12, 0.15, 0.11, 0.15, 0.18, 0.14, 0.12, 0.13]
}

df = pd.DataFrame(raw_data)
print("--- Raw Data ---")
print(df)

# --- 2. Data Cleaning ---
df = df.drop_duplicates().reset_index(drop=True)
median_temp = df.loc[df['Temp_Celsius'] <= 100, 'Temp_Celsius'].median()
df.loc[df['Temp_Celsius'] > 100, 'Temp_Celsius'] = median_temp
df['Spindle_Speed_RPM'] = df['Spindle_Speed_RPM'].fillna(df['Spindle_Speed_RPM'].mean())
df['Temp_Celsius'] = df['Temp_Celsius'].fillna(df['Temp_Celsius'].mean())

# --- 3. Status Check ---
df['Status'] = np.where(df['Vibration_mm_s'] > 0.17, 'Maintenance Required', 'Optimal')

print("\n--- Cleaned Data ---")
print(df)
