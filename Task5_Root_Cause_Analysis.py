"""
================================================================================
MODULE:    Root Cause Analysis (Manufacturing Quality Optimization)
PROJECT:   Predictive Maintenance System (TechnoHacks Internship)
AUTHOR:    Viraj Uttam More
DOMAIN:    Data Analytics / Quality Control
BATCH:     119 
DATE:      January 2026

--- OBJECTIVE ---
To identify the root cause of batch failures in the manufacturing line.
By comparing process parameters (Pressure & Temperature) of Failed Batches vs. 
Successful Batches, we generate actionable insights to optimize quality.

--- METHODOLOGY ---
1. Data Ingestion: Loaded production logs containing Pressure, Temperature, and 
   Quality Status (0 = Failed, 1 = Passed).
2. Comparative Analysis: Used GroupBy aggregation to calculate the Mean (Average) 
   values for both Failed and Passed groups.
3. Root Cause Logic: Compared the 'Temperature' of failed batches against passed 
   batches.
4. Recommendation: If Failed Temp > Passed Temp, the system suggests reducing 
   the cooling temperature by the exact difference calculated.
================================================================================
"""

import pandas as pd

def load_quality_data():
    """
    Simulates production line data.
    Status 0 = Failed Batch
    Status 1 = Passed Batch
    """
    data = {
        'Pressure_PSI': [92, 98, 91, 99, 93, 100, 92, 99],
        'Temp_Celsius': [25.5, 22.1, 26.2, 21.8, 25.8, 22.0, 26.5, 21.5],
        'Status': [0, 1, 0, 1, 0, 1, 0, 1] 
    }
    return pd.DataFrame(data)

def perform_audit(df):
    """
    Groups data by Status to find average operating conditions.
    """
    # Group by 'Status' (0 or 1) and calculate mean of other columns
    audit_summary = df.groupby('Status').mean()
    return audit_summary

def generate_recommendation(summary):
    """
    Compares Failed (0) vs Passed (1) stats to suggest fixes.
    """
    # Extract Average Temperatures
    avg_temp_failed = summary.loc[0, 'Temp_Celsius']
    avg_temp_passed = summary.loc[1, 'Temp_Celsius']
    
    print(f"--- DIAGNOSTIC REPORT ---")
    print(f"Avg Temp (Failed Batches): {avg_temp_failed:.2f} °C")
    print(f"Avg Temp (Passed Batches): {avg_temp_passed:.2f} °C")
    
    # Logic for Recommendation
    diff = avg_temp_failed - avg_temp_passed
    
    print(f"\n--- ACTIONABLE INSIGHT ---")
    if avg_temp_failed > avg_temp_passed:
        print(f"[ROOT CAUSE FOUND]: Overheating detected in failed batches.")
        print(f"[RECOMMENDATION]: Reduce Cooling System Temperature by {diff:.2f} °C")
    else:
        print("[INFO]: Temperature is within normal range. Check Pressure settings.")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print(f"[{'='*20} QUALITY AUDIT STARTED {'='*20}]")
    
    # 1. Load Data
    df = load_quality_data()
    print(f"Data Loaded: {len(df)} batches analyzed.")
    
    # 2. Analyze
    summary = perform_audit(df)
    print("\n--- Process Parameter Averages ---")
    print(summary)
    print("-" * 30)
    
    # 3. Report
    generate_recommendation(summary)
    
    print(f"\n[{'='*20} AUDIT COMPLETE {'='*20}]")

"""
================================================================================
EXECUTION OUTPUT LOG (Terminal Result)
================================================================================
[==================== QUALITY AUDIT STARTED ====================]
Data Loaded: 8 batches analyzed.

--- Process Parameter Averages ---
        Pressure_PSI  Temp_Celsius
Status                            
0               92.0         26.00
1               99.0         21.85
------------------------------
--- DIAGNOSTIC REPORT ---
Avg Temp (Failed Batches): 26.00 °C
Avg Temp (Passed Batches): 21.85 °C

--- ACTIONABLE INSIGHT ---
[ROOT CAUSE FOUND]: Overheating detected in failed batches.
[RECOMMENDATION]: Reduce Cooling System Temperature by 4.15 °C

[==================== AUDIT COMPLETE ====================]
================================================================================
"""

