<div align="center">

<a name="top"></a>
# 🏭 Industrial IoT & Predictive Maintenance Analytics
### *Driving Smart Manufacturing through Data Science & Machine Learning*

<img src="https://img.shields.io/badge/Python-3.13.7-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Role-Data%20Analyst-FF6F61?style=for-the-badge&logo=google-colab&logoColor=white" />
<img src="https://img.shields.io/badge/Algorithm-Linear%20Regression-success?style=for-the-badge" />

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

## 🎯 Project Impact & Key Findings
Based on the analysis of the CNC telemetry data, here are the actual results derived from the code:

| **Metric** | **Result** | **Business Impact** |
| :--- | :--- | :--- |
| **Correlation** | **Positive Trend** | Higher RPM and Operation Time directly increase *Vibration*. |
| **Model Prediction** | **High Risk @ 1250 RPM** | Predicted Temp spike (>50°C) at high speeds, signaling overload. |
| **Data Quality** | **Outliers Fixed** | Corrected sensor glitches (850°C spikes) using Median Imputation. |
| **Root Cause (RCA)** | **Cooling Failure** | **Temperature** (not Pressure) was identified as the main cause of batch failures. |

---

<a name="-project-tasks--analysis"></a>
## 📂 Project Tasks & Analysis
*Detailed breakdown of the 5 Tasks completed using Python:*

### ✅ Task 1: Data Sanitization (Cleaning)
* **Code Logic:** Handling sensor errors where Temperature spiked to unrealistic values (e.g., 850°C).
* **Action:**
  * Removed duplicate timestamp entries.
  * **Imputation:** Used `median()` for temperature outliers and `mean()` for missing RPM values.
  * **Feature Engineering:** Created a `Status` column to flag vibrations > 0.17 mm/s as "Maintenance Required".

### ✅ Task 2: Exploratory Data Analysis (EDA)
* **Code Logic:** Dual-axis visualization using `matplotlib`.
* **Visuals:** Plotted **Temperature (Left Axis)** vs. **Vibration (Right Axis)** over time.
* **Finding:** Observed a synchronized increase in temperature and vibration, confirming mechanical stress accumulation.

### ✅ Task 3: Statistical Process Control (SPC)
* **Code Logic:** Threshold detection using Standard Deviation.
* **Formula:** `Limit = Mean + (1.5 * Std_Dev)`.
* **Outcome:** Categorized machine health into three zones: **Safe**, **Caution**, and **Critical**.
* **Alerts:** Successfully flagged specific timestamps where vibration exceeded the safety threshold.

### ✅ Task 4: Predictive Analytics (ML)
* **Code Logic:** Training a **Linear Regression** model on RPM vs. Temperature.
* **Prediction:** The model predicted the Spindle Temperature for a hypothetical high-speed operation (**1250 RPM**).
* **Assessment:** The system automatically flags "HIGH RISK - Overload" if the predicted temperature exceeds **50°C**.

### ✅ Task 5: Root Cause Analysis (RCA)
* **Code Logic:** A/B Testing of "Failed" vs. "Passed" batches.
* **Comparison:** Calculated mean Temperature and Pressure for both groups.
* **Conclusion:** The algorithm detected that **Average Temperature in Failed Batches (~26°C)** was significantly higher than in Passed Batches (~21°C), recommending a reduction in Cooling Temp.

---

<a name="-model-performance--key-insights"></a>
## 📈 Technical Implementation Details
The project utilizes a robust Python stack for analysis:

* **Linear Regression:** Used to calculate Slope and Intercept for thermal forecasting.
* **Pandas GroupBy:** Used in Task 5 to isolate failure patterns.
* **Twin-Axis Plotting:** Used in Task 2 to correlate two different physical units (Celsius & mm/s).

---

## 🛠️ Tech Stack
<div align="center">
  <img src="https://img.shields.io/badge/Language-Python%203.13-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Library-Pandas-150458?logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Library-NumPy-013243?logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/Library-Matplotlib-ffffff?logo=matplotlib&logoColor=black">
  <img src="https://img.shields.io/badge/Library-Scikit_Learn-F7931E?logo=scikit-learn&logoColor=white">
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

3.  **Run Analysis**
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
