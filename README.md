<div align="center">

<a name="top"></a>
# 🏭 Industrial IoT & Predictive Maintenance Analytics
### *Driving Smart Manufacturing through Data Science & Machine Learning*

<img src="https://img.shields.io/badge/Python-3.13.7-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Role-Data%20Analyst-FF6F61?style=for-the-badge&logo=google-colab&logoColor=white" />
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />

<br>

[**📂 View All Tasks**](#-project-tasks--analysis) •
[**📊 Model Results**](#-model-performance--key-insights) •
[**⚙️ Installation**](#-how-to-replicate-setup) •
[**📜 Ownership**](#-author-declaration--ownership)

</div>

---

## 👨‍💻 Author & Academic Profile
| **Parameter** | **Details** |
| :--- | :--- |
| **Analyst Name** | **Viraj Uttam More** |
| **Institution** | **RMD Sinhgad Technical Institutes Campus, Warje, Pune** |
| **Department** | Mechanical Engineering (T.E. 2019 Pattern) |
| **University** | Savitribai Phule Pune University (SPPU) |
| **Email** | virajmore5456@gmail.com |

---

## 🏢 Internship Context
> *Verified internship executed under the mentorship of a Ministry of Corporate Affairs (MCA) registered entity.*

| **Attribute** | **Official Company Details** |
| :--- | :--- |
| **Organization** | **TechnoHacks Solutions Pvt. Ltd.** |
| **Registration** | **ISO 9001:2015 Certified** & **MSME Registered** |
| **CIN** | `U62099MH2024PTC424756` |
| **Headquarters** | Nashik, Maharashtra - 422005 |

---

## 🎯 Project Impact at a Glance
Before diving into the code, here are the key analytical outcomes:

| **Metric** | **Result** | **Business Impact** |
| :--- | :--- | :--- |
| **Correlation** | **0.87 (High)** | Proved that *Torque* is the primary driver of *Tool Wear*. |
| **Model Accuracy** | **85% (R²)** | Reliable prediction of Spindle Temperature spikes. |
| **Data Quality** | **100% Cleaned** | Removed noise and imputed missing time-series values. |
| **RCA Outcome** | **Pressure Isolated** | Identified specific pressure ranges causing defects. |

---

<a name="-project-tasks--analysis"></a>
## 📂 Project Tasks & Analysis
*Detailed breakdown of the 5 Tasks completed during the internship:*

### ✅ Task 1: Data Sanitization (Cleaning)
* **Objective:** Handle noisy sensor data and missing values.
* **Solution:** Applied **Median Imputation** to preserve data distribution without dropping rows, ensuring 100% data consistency for time-series analysis.

### ✅ Task 2: Exploratory Data Analysis (EDA)
* **Objective:** Find relationships between mechanical parameters.
* **Key Finding:** A strong linear relationship (**r = 0.87**) exists between Torque and Tool Wear.
* **Visuals Used:** Heatmaps & Distribution Plots.

### ✅ Task 3: Statistical Process Control (SPC)
* **Objective:** Detect anomalies in machine temperature.
* **Outcome:** Calculated **Upper & Lower Control Limits (UCL/LCL)** using Z-Scores and IQR to flag overheating risks in real-time.

### ✅ Task 4: Predictive Modeling (Machine Learning)
* **Objective:** Forecast Spindle Failure.
* **Algorithm:** **Linear Regression** (Scikit-Learn).
* **Performance:** Achieved an **MAE (Mean Absolute Error) of 2.4K**, making the model suitable for industrial monitoring.

### ✅ Task 5: Root Cause Analysis (RCA)
* **Objective:** Investigate Manufacturing Defects.
* **Result:** Isolated specific high-pressure zones responsible for 60% of product defects by comparing "Failure" vs. "No Failure" states.

---

<a name="-model-performance--key-insights"></a>
## 📈 Model Performance & Key Insights
To validate the accuracy of the model, standard metrics were calculated:

* **R² Score:** 0.85 (High reliability)
* **MAE:** 2.4 Kelvin (Low error margin)
* **RMSE:** 3.1 Kelvin

---

## 🛠️ Tech Stack
<div align="center">
  <img src="https://img.shields.io/badge/Language-Python%203.13-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Library-Pandas-150458?logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Library-NumPy-013243?logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/Library-Scikit_Learn-F7931E?logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/Tool-VS%20Code-007ACC?logo=visual-studio-code&logoColor=white">
</div>

---

<a name="-how-to-replicate-setup"></a>
## ⚙️ How to Replicate (Setup)
To run this analysis on your local machine:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/virajmore/TechnoHacks-Internship.git](https://github.com/virajmore/TechnoHacks-Internship.git)
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch Notebook**
    ```bash
    jupyter notebook
    ```

---

<a name="-author-declaration--ownership"></a>
## 📜 Author Declaration & Ownership
**I, Viraj Uttam More, hereby declare that:**

1.  The work presented in this repository is my original contribution completed during the **TechnoHacks Solutions Pvt. Ltd.** Internship (Batch 119).
2.  The code and analysis are submitted for the partial fulfillment of the requirements for the **Third Year (T.E.) Mechanical Engineering** course at **SPPU**.
3.  All sources of data and external libraries have been duly acknowledged.

<br>

| **Verified By** | **Details** |
| :--- | :--- |
| **Signature** | *Viraj Uttam More* |
| **Submission Month** | **January 2026** |
| **Place** | **Pune, Maharashtra** |
| **Institute** | RMD Sinhgad Technical Institutes Campus, Warje |

<br>

<div align="center">
  <b>© 2026 Viraj Uttam More. All Rights Reserved.</b><br>
  <i>Unauthorized reproduction or plagiarism of this repository is strictly prohibited.</i>
  <br><br>
  <a href="#top">⬆️ Back to Top</a>
</div>
