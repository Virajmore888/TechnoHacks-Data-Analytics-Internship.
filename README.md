<div align="center">

# 🏭 Industrial IoT & Predictive Maintenance Analytics
### *Driving Smart Manufacturing through Data Science & Machine Learning*

<img src="https://img.shields.io/badge/Python-3.13.7-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Role-Data%20Analyst-FF6F61?style=for-the-badge&logo=google-colab&logoColor=white" />
<img src="https://img.shields.io/badge/Company-TechnoHacks-000000?style=for-the-badge&logo=github&logoColor=white" />
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />

<br>

<p>
<b>An industrial data analytics project analyzing CNC telemetry data to predict machinery failure,<br>optimize maintenance schedules, and reduce operational downtime.</b>
</p>

<br>

[**📂 View Modules**](#-project-architecture--analysis-modules) •
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

## 🏢 Internship Context (Corporate Profile)
> *Verified internship executed under the mentorship of a Ministry of Corporate Affairs (MCA) registered entity.*

| **Attribute** | **Official Company Details** |
| :--- | :--- |
| **Organization** | **TechnoHacks Solutions Pvt. Ltd.** |
| **Registration** | **ISO 9001:2015 Certified** & **MSME Registered** |
| **CIN** | `U62099MH2024PTC424756` |
| **Headquarters** | Nashik, Maharashtra - 422005 |
| **Domain** | EdTech & Software Solutions |

---

## 🎯 Project Impact at a Glance
Before diving into the code, here are the key analytical outcomes of this project:

| **Metric** | **Result** | **Business Impact** |
| :--- | :--- | :--- |
| **Correlation** | **0.87 (High)** | Proved that *Torque* is the primary driver of *Tool Wear*. |
| **Model Accuracy** | **85% (R²)** | Reliable prediction of Spindle Temperature spikes. |
| **Data Quality** | **100% Cleaned** | Removed noise and imputed missing time-series values. |
| **RCA Outcome** | **Pressure Isolated** | Identified specific pressure ranges causing defects. |

---

## 🔄 Project Architecture (Flowchart)
The analysis follows the standard **CRISP-DM** (Cross-Industry Standard Process for Data Mining) methodology:

```mermaid
graph LR
    A[💾 Raw Sensor Data] -->|Cleaning| B(🛠️ Preprocessing)
    B -->|EDA| C{📊 Pattern Analysis}
    C -->|Stats| D[📉 Thresholding]
    D -->|ML| E[🤖 Predictive Model]
    E -->|RCA| F[✅ Final Insight]
