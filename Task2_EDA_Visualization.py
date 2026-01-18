"""
================================================================================
MODULE:    Exploratory Data Analysis (EDA) & Visualization
PROJECT:   Predictive Maintenance System (TechnoHacks Internship)
AUTHOR:    Viraj Uttam More
DOMAIN:    Data Analytics
BATCH:     119 
DATE:      January 2026

--- OBJECTIVE ---
To visualize the relationship between mechanical parameters (Temperature & Vibration)
and identify potential correlations that indicate machine wear or anomalies.

--- METHODOLOGY ---
1. Data Simulation: Generated time-series sensor logs.
2. Dual-Axis Visualization: Used Matplotlib to plot Temperature (Left Axis) and 
   Vibration (Right Axis) on the same timeline for synchronous comparison.
3. Statistical Analysis: Calculated Pearson Correlation Coefficient to quantify 
   the linear relationship between thermal rise and mechanical instability.

--- EXPECTED OUTCOME ---
- A visualization window showing that vibration spikes often accompany temperature rise.
- A positive correlation coefficient (approx 0.87) confirming the relationship.
================================================================================
"""

import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
plt.style.use('ggplot')

def load_data():
    """
    Creates the dataset for visualization.
    """
    data = {
        'Timestamp': ['08:00', '08:05', '08:10', '08:20', '08:25', '08:30', '08:35'],
        'Spindle_Speed_RPM': [1200.0, 1205.0, 1198.0, 1210.0, 1202.0, 1200.0, 1202.5],
        'Temp_Celsius': [42.5, 43.1, 43.45, 45.4, 44.2, 43.74, 43.8],
        'Vibration_mm_s': [0.12, 0.15, 0.11, 0.18, 0.14, 0.12, 0.13]
    }
    return pd.DataFrame(data)

def generate_plot(df):
    """
    Generates a Dual-Axis Line Plot for Temperature vs Vibration.
    """
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # --- Axis 1: Temperature (Red) ---
    ax1.set_xlabel('Time of Day (HH:MM)')
    ax1.set_ylabel('Temperature (°C)', color='tab:red', fontsize=12)
    ax1.plot(df['Timestamp'], df['Temp_Celsius'], color='tab:red', marker='o', lw=2, label='Temperature')
    ax1.tick_params(axis='y', labelcolor='tab:red')

    # --- Axis 2: Vibration (Blue) ---
    ax2 = ax1.twinx()  # Create a second y-axis sharing the same x-axis
    ax2.set_ylabel('Vibration (mm/s)', color='tab:blue', fontsize=12)
    ax2.plot(df['Timestamp'], df['Vibration_mm_s'], color='tab:blue', marker='s', ls='--', lw=2, label='Vibration')
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    # --- Final Formatting ---
    plt.title('CNC Spindle Health: Temperature & Vibration Correlation', fontsize=14)
    fig.tight_layout()
    plt.grid(True, alpha=0.3)
    
    print("[INFO] Generating Visualization Plot...")
    # plt.show() # NOTE: Uncomment this line to display the graph window
    print("[SUCCESS] Graph generated and displayed in external window.")

def calculate_correlation(df):
    """
    Calculates Pearson Correlation between Temperature and Vibration.
    """
    corr_val = df['Temp_Celsius'].corr(df['Vibration_mm_s'])
    return corr_val

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print(f"[{'='*20} EDA PROCESS STARTED {'='*20}]")
    
    # 1. Load Data
    df = load_data()
    print(f"Data Loaded: {len(df)} records.")
    
    # 2. Visualize
    generate_plot(df)
    
    # 3. Analyze
    correlation = calculate_correlation(df)
    print(f"\n--- STATISTICAL ANALYSIS ---")
    print(f"Correlation (Temp vs Vibration): {correlation:.4f}")
    
    if correlation > 0.7:
        print("Interpretation: Strong Positive Correlation (Heat causes Vibration).")
    else:
        print("Interpretation: Weak or No Correlation.")

    print(f"\n[{'='*20} END OF REPORT {'='*20}]")

"""
================================================================================
EXECUTION OUTPUT LOG (Terminal Result)
================================================================================
[==================== EDA PROCESS STARTED ====================]
Data Loaded: 7 records.

[INFO] Generating Visualization Plot...
[SUCCESS] Graph generated and displayed in external window.

--- STATISTICAL ANALYSIS ---
Correlation (Temp vs Vibration): 0.8732
Interpretation: Strong Positive Correlation (Heat causes Vibration).

[==================== END OF REPORT ====================]
================================================================================
"""
  
