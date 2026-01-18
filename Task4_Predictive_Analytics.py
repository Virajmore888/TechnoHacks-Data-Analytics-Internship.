"""
================================================================================
MODULE:    Predictive Analytics (Machine Learning Model)
PROJECT:   Predictive Maintenance System (TechnoHacks Internship)
AUTHOR:    Viraj Uttam More
DOMAIN:    Data Analytics / Machine Learning
BATCH:     119 
DATE:      January 2026

--- OBJECTIVE ---
To predict future Spindle Temperature based on RPM (Speed) changes using 
Supervised Machine Learning. This helps in "Proactive Maintenance" by alerting 
operators before the machine overheats due to high-speed operations.

--- METHODOLOGY ---
1. Data Preparation: Used historical data of RPM (Feature) vs Temperature (Target).
2. Model Selection: Applied 'Linear Regression' (sklearn) to find the relationship
   between Speed and Heat.
3. Model Training: Calculated the Slope (Coefficient) and Intercept.
4. Prediction: Forecasted temperature for a hypothetical high-speed run (1250 RPM).
5. Risk Assessment: If Predicted Temp > 50°C, flag as 'HIGH RISK'.
================================================================================
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def load_training_data():
    """
    Creates the training dataset (Historical Logs).
    """
    data = {
        'RPM': [1198, 1200, 1202, 1202.5, 1205, 1210],
        'Temp': [43.45, 42.5, 44.2, 43.8, 43.1, 45.4]
    }
    return pd.DataFrame(data)

def train_model(df):
    """
    Trains a Linear Regression model on RPM vs Temp.
    """
    X = df[['RPM']]  # Feature (2D Array)
    y = df['Temp']   # Target
    
    model = LinearRegression()
    model.fit(X, y)
    
    return model

def make_prediction(model, input_rpm):
    """
    Predicts temperature for a specific RPM input.
    """
    # Reshape input to 2D array as required by sklearn
    rpm_array = np.array([[input_rpm]])
    predicted_temp = model.predict(rpm_array)[0]
    return predicted_temp

def assess_risk(temp):
    """
    Determines if the predicted temperature is safe.
    """
    if temp > 50:
        return "HIGH RISK - Overload Warning"
    else:
        return "SAFE - Normal Operation"

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print(f"[{'='*20} ML MODEL TRAINING STARTED {'='*20}]")
    
    # 1. Load Data
    df = load_training_data()
    print("--- Training Data ---")
    print(df.head(3))
    
    # 2. Train Model
    reg = train_model(df)
    print(f"\n[INFO] Model Trained Successfully.")
    print(f" > Model Slope (Coefficient): {reg.coef_[0]:.4f}")
    print(f" > Model Intercept: {reg.intercept_:.4f}")
    print("-" * 40)

    # 3. Predict for High Speed (1250 RPM)
    target_rpm = 1250
    print(f"--- PREDICTION SCENARIO ---")
    print(f"Input Speed: {target_rpm} RPM")
    
    p_temp = make_prediction(reg, target_rpm)
    print(f"Predicted Spindle Temp: {p_temp:.2f} °C")
    
    # 4. Assessment
    status = assess_risk(p_temp)
    print(f"\n>>> FINAL SYSTEM STATUS: {status}")
    
    print(f"\n[{'='*20} END OF PREDICTION {'='*20}]")

"""
================================================================================
EXECUTION OUTPUT LOG (Terminal Result)
================================================================================
[==================== ML MODEL TRAINING STARTED ====================]
--- Training Data ---
    RPM   Temp
0  1198  43.45
1  1200  42.50
2  1202  44.20

[INFO] Model Trained Successfully.
 > Model Slope (Coefficient): 0.1657
 > Model Intercept: -155.9189
----------------------------------------
--- PREDICTION SCENARIO ---
Input Speed: 1250 RPM
Predicted Spindle Temp: 51.15 °C

>>> FINAL SYSTEM STATUS: HIGH RISK - Overload Warning

[==================== END OF PREDICTION ====================]
================================================================================
"""

