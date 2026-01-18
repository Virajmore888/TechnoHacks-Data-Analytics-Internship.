# Industrial IoT & Predictive Maintenance Analytics
**Internship Project Report | Batch 119**

![Python](https://img.shields.io/badge/Python-3.13.7-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 1. Project Abstract
This repository documents the Data Analytics and Machine Learning tasks completed during the internship at **TechnoHacks Solutions Pvt. Ltd.** The project aims to analyze industrial telemetry data from CNC machines to detect anomalies and predict spindle failure, bridging the gap between Mechanical Engineering domain knowledge and Data Science techniques.

---

## 2. Student & Academic Details
| **Parameter** | **Details** |
| :--- | :--- |
| **Name of Student** | **Viraj Uttam More** |
| **Course** | B.E. / B.Tech (Mechanical Engineering) |
| **Current Year** | Third Year (T.E.) - 2019 Pattern |
| **Institute** | **RMD Sinhgad Technical Institutes Campus, Warje, Pune** |
| **University** | Savitribai Phule Pune University (SPPU) |
| **Email** | virajmore5456@gmail.com |

---

## 3. Internship Company Profile
The project was executed under the guidance of **TechnoHacks Solutions Pvt. Ltd.**, an ISO 9001:2015 certified and MSME registered company.

- **Company Name:** TechnoHacks Solutions Pvt. Ltd.
- **CIN:** `U62099MH2024PTC424756`
- **Registration No:** 424756 (ROC-Mumbai)
- **Address:** Gangapur Road, Nashik, Maharashtra - 422005.

---

## 4. Problem Statement
To develop a predictive model capable of forecasting **Spindle Temperature** in a CNC machining environment to prevent overheating and tool breakage, thereby optimizing manufacturing quality and reducing downtime.

---

## 5. Methodology (Task Breakdown)
The project was divided into 5 technical modules:

### Module 1: Data Cleaning & Pre-processing
- **Objective:** Handling noise in sensor data.
- **Action:** Implemented `pandas` for median imputation of missing values and standardized timestamp formats for time-series consistency.

### Module 2: Exploratory Data Analysis (EDA)
- **Objective:** To find correlations between mechanical parameters.
- **Observation:** A correlation coefficient of **0.87** was observed between **Torque** and **Tool Wear**. Visualized using Heatmaps and Box Plots.

### Module 3: Statistical Analysis (Thresholding)
- **Objective:** Defining safe operating limits.
- **Action:** Calculated **Upper & Lower Control Limits (UCL/LCL)** using the IQR method to flag anomalies in temperature readings.

### Module 4: Predictive Modeling
- **Objective:** Forecasting machine behavior.
- **Action:** Developed a **Linear Regression** model using `scikit-learn`.
- **Performance:** The model achieved an **R² Score of 0.85**, effectively predicting thermal spikes based on Load and Speed.

### Module 5: Root Cause Analysis (RCA)
- **Objective:** Quality Control.
- **Action:** Analyzed process parameters (Pressure, Speed) against binary failure targets to isolate causes of production defects.

---

## 6. Process Flowchart
```mermaid
graph LR
    A[Raw Data] --> B(Data Cleaning)
    B --> C(EDA & Stats)
    C --> D[Model Training]
    D --> E[Predictions & RCA]
