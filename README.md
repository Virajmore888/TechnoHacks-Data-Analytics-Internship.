# 🏭 Industrial Data Analytics & Predictive Maintenance
**Official Internship Documentation | Batch 119**

---

## 📋 Document Control Information
| **Attribute** | **Details** |
| :--- | :--- |
| **Project Title** | Industrial IoT & Predictive Maintenance Analytics |
| **Domain** | Data Science & Smart Manufacturing (Industry 4.0) |
| **Student Name** | **Viraj Uttam More** |
| **Affiliation** | RMD Sinhgad Technical Institutes Campus, Warje, Pune |
| **Submission To** | Savitribai Phule Pune University (SPPU) |
| **Company** | TechnoHacks Solutions Pvt. Ltd. |
| **Status** | ✅ Completed & Verified |

---

## 1. Executive Summary
This repository serves as the technical submission for the internship curriculum at **TechnoHacks Solutions Pvt. Ltd.** The project focuses on bridging the gap between **Mechanical Engineering** and **Data Science** by analyzing high-frequency telemetry data from CNC machines. The objective was to implement **Condition-Based Maintenance (CBM)** to predict spindle failures and optimize production quality.

---

## 2. Industrial Profile (Company Details)
The research and development were conducted under the mentorship of:

* **Organization:** TechnoHacks Solutions Pvt. Ltd.
* **Registration:** ISO 9001:2015 Certified & MSME Registered.
* **CIN:** `U62099MH2024PTC424756`
* **Headquarters:** Nashik, Maharashtra - 422005.

---

## 3. Technical Methodology
The project workflow follows standard Data Science pipelines tailored for Industrial IoT:

* **Module 1: Data Sanitization:** Implemented median imputation strategies to handle missing sensor data without data loss.
* **Module 2: Exploratory Analysis (EDA):** Identified a strong correlation (**0.87**) between Torque and Tool Wear using Heatmaps.
* **Module 3: Statistical Thresholding:** Defined Upper/Lower Control Limits (UCL/LCL) for Spindle Temperature using IQR Z-Scores.
* **Module 4: Predictive Modeling:** Developed a **Linear Regression Model** (Accuracy: 85%) to forecast thermal anomalies based on RPM and Load.
* **Module 5: Root Cause Analysis:** Isolated specific pressure ranges contributing to manufacturing defects.

---

## 4. Technology Stack
* **Language:** Python 3.13.7
* **Environment:** Visual Studio Code (VS Code) / Jupyter Notebook
* **Libraries:** `pandas` (ETL), `numpy` (Math), `seaborn` (Visualization), `scikit-learn` (Modeling).

---

## 5. How to Replicate (Setup Instructions)
To verify the results locally:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/virajmore/TechnoHacks-Internship.git](https://github.com/virajmore/TechnoHacks-Internship.git)
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run Analysis:**
    ```bash
    jupyter notebook
    ```

---

## 📜 6. Author Declaration & Ownership
**I, Viraj Uttam More, hereby declare that:**

1.  The work presented in this repository is my original contribution completed during the **TechnoHacks Solutions Pvt. Ltd.** Internship (Batch 119).
2.  The code and analysis are submitted for the partial fulfillment of the requirements for the **Third Year (T.E.) Mechanical Engineering** course at **SPPU**.
3.  All sources of data and external libraries have been duly acknowledged.

<br>

| **Verified By** | **Student Details** |
| :--- | :--- |
| **Signature:** | *Viraj Uttam More* |
| **Date:** | 2026 |
| **Institute:** | RMD Sinhgad Technical Institutes Campus, Warje |
| **Department:** | Mechanical Engineering |

<div align="center">
  <br>
  <b>© 2026 Viraj Uttam More. All Rights Reserved.</b>
  <br>
  <i>Unauthorized copying of this repository's content is strictly prohibited.</i>
</div>
