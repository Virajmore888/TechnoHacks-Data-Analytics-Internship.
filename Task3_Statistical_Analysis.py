"""
================================================================================
MODULE:    Statistical Analysis & Threshold Detection
PROJECT:   Predictive Maintenance System (TechnoHacks Internship)
AUTHOR:    Viraj Uttam More
DOMAIN:    Data Analytics
BATCH:     119 
DATE:      January 2026

--- OBJECTIVE ---
To implement statistical process control (SPC) logic for detecting anomalies.
Instead of fixed values, we use dynamic thresholds based on data distribution 
(Mean and Standard Deviation) to categorize machine health.

--- METHODOLOGY ---
1. Statistical Calculation: Computed Mean (Avg) and Standard Deviation (Std) 
   of the vibration sensor data.
2. Threshold Definition: Defined Upper Control Limit (UCL) as Mean + (1.5 * Std).
3. Logic Classification:
   - Critical: Vibration > UCL (Immediate Action Required)
   - Caution:  Vibration > Mean (Monitor Closely)
   - Safe:     Vibration <= Mean (Normal Operation)
================================================================================
"""

import pandas as pd
import numpy as np

def load_data():
    """
    Loads simulated sensor data for analysis.
    """
    data = {
        'Timestamp': ['08:00', '08:05', '08:10', '08:20', '08:25', '08:30', '08:35'],
        'Vibration_mm_s': [0.12, 0.15, 0.11, 0.18, 0.14, 0.12, 0.13]
    }
    return pd.DataFrame(data)

def perform_statistical_analysis(df):
    """
    Calculates dynamic thresholds and assigns risk zones.
    """
    # 1. Calculate Statistics
    avg_vib = df['Vibration_mm_s'].mean()
    std_vib = df['Vibration_mm_s'].std()
    
    # 2. Define Dynamic Threshold (Mean + 1.5 Sigma)
    # Note: 1.5 Sigma is used here for early warning detection.
    threshold_limit = avg_vib + (1.5 * std_vib)

    print(f"--- STATISTICAL METRICS ---")
    print(f"Mean Vibration: {avg_vib:.4f} mm/s")
    print(f"Std Deviation:  {std_vib:.4f} mm/s")
    print(f"Dynamic Limit:  {threshold_limit:.4f} mm/s (Mean + 1.5*Std)")

    # 3. Apply Vectorized Logic (Safe vs Caution vs Critical)
    conditions = [
        (df['Vibration_mm_s'] > threshold_limit),  # Critical Condition
        (df['Vibration_mm_s'] > avg_vib)           # Caution Condition
    ]
    choices = ['Critical', 'Caution']
    
    # Default is 'Safe'
    df['Zone'] = np.select(conditions, choices, default='Safe')
    
    return df, threshold_limit

def generate_alerts(df):
    """
    Filters and prints alerts for Critical zones.
    """
    critical_events = df[df['Zone'] == 'Critical']
    num_alerts = len(critical_events)
    
    print(f"\n--- ALERT REPORT ---")
    if num_alerts > 0:
        print(f"[WARNING] {num_alerts} Critical Event(s) Detected!")
        for i, row in critical_events.iterrows():
            print(f" > Time: {row['Timestamp']} | Vib: {row['Vibration_mm_s']} | Status: CRITICAL")
    else:
        print("[INFO] System running smoothly. No critical anomalies.")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print(f"[{'='*20} ANALYSIS STARTED {'='*20}]")
    
    # Step 1: Load
    df = load_data()
    
    # Step 2: Analyze
    analyzed_df, limit = perform_statistical_analysis(df)
    
    # Step 3: Show Data Table
    print(f"\n--- CLASSIFIED DATA TABLE ---")
    print(analyzed_df)
    
    # Step 4: Generate Alerts
    generate_alerts(analyzed_df)

    print(f"\n[{'='*20} END OF REPORT {'='*20}]")

"""
================================================================================
EXECUTION OUTPUT LOG (Terminal Result)
================================================================================
[==================== ANALYSIS STARTED ====================]
--- STATISTICAL METRICS ---
Mean Vibration: 0.1357 mm/s
Std Deviation:  0.0237 mm/s
Dynamic Limit:  0.1713 mm/s (Mean + 1.5*Std)

--- CLASSIFIED DATA TABLE ---
  Timestamp  Vibration_mm_s      Zone
0     08:00            0.12      Safe
1     08:05            0.15   Caution
2     08:10            0.11      Safe
3     08:20            0.18  Critical
4     08:25            0.14   Caution
5     08:30            0.12      Safe
6     08:35            0.13      Safe

--- ALERT REPORT ---
[WARNING] 1 Critical Event(s) Detected!
 > Time: 08:20 | Vib: 0.18 | Status: CRITICAL

[==================== END OF REPORT ====================]
================================================================================
"""

