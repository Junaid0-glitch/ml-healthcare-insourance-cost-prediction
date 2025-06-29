Here's a detailed and professional README tailored for your ML Healthcare Insurance Cost Prediction project:

---

# 🏥 ML Healthcare Insurance Cost Prediction

![Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-brightgreen)

A complete **end-to-end Machine Learning project** that predicts healthcare insurance costs based on user attributes such as age, BMI, smoking status, and more. The project is backed by a **FastAPI** backend, a user-friendly **Streamlit frontend**, and fully **deployed using Docker on AWS**.

🔗 **Live App**: [Launch Here 🚀](https://ml-healthcare-insourance-cost-prediction-qbmwupheyvejgcf6mpmv8.streamlit.app/)

---

## 🧠 Project Overview

This project is designed to provide **accurate healthcare insurance cost predictions** using advanced machine learning models. It includes:

* EDA and insightful data visualization
* Segmented model training for different age groups
* XGBoost and regression-based models with hyperparameter tuning
* Seamless deployment using FastAPI, Docker, and Streamlit Cloud

---

## 📊 Dataset

* **Size:** 50,000 rows
* **Features:** age, sex, BMI, children, smoker, region, charges
---

## 🔍 Exploratory Data Analysis (EDA)

* Visualized feature distributions and correlations
* Detected strong influence of **smoking status**, **BMI**, and **age** on insurance charges
* Identified non-linear patterns leading to model segmentation

---

## ⚙️ Model Strategy

### 🔹 Age-Based Segmentation

To improve prediction accuracy:

* **Group 1:** Age ≤ 25

  * Algorithms tested: `Linear Regression`, `Ridge Regression`, `XGBoost`
  * **Final Model:** `XGBoost Regressor` with hyperparameter tuning via `RandomizedSearchCV`
  * **Accuracy:** **98%**

* **Group 2:** Age > 25

  * Algorithms tested: `Linear Regression`, `Ridge Regression`, `XGBoost`
  * **Final Model:** `XGBoost Regressor` with `RandomizedSearchCV`
  * **Accuracy:** **99%**

---

## 🚀 Deployment Architecture

### 🔧 Backend

* **Framework:** FastAPI
* **Purpose:** Hosts ML models and exposes prediction endpoints
* **Deployment:** Dockerized and deployed on **AWS Ubuntu EC2 instance**

### 🎨 Frontend

* **Framework:** Streamlit
* **Purpose:** Interactive web UI for entering user data and viewing predictions
* **Deployment:** Hosted via **Streamlit Cloud**

### 🐳 Containerization

* **Docker:** Backend containerized and pushed to **Docker Hub**
* Docker image used for production on AWS

---

## 🛠️ Technologies Used

| Category     | Tools / Libraries            |
| ------------ | ---------------------------- |
| Language     | Python                       |
| ML Libraries | Scikit-learn, XGBoost        |
| Backend      | FastAPI                      |
| Frontend     | Streamlit                    |
| Deployment   | Docker, AWS, Streamlit Cloud |
| EDA & Viz    | Pandas, Matplotlib, Seaborn  |

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Junaid0-glitch/ml-healthcare-insourance-cost-prediction.git
cd healthcare-cost-predictor
```

### 2. Backend Setup (FastAPI)

```bash
cd backend
docker build -t healthcare-app .
docker run -d -p 8000:8000 healthcare-app
```

### 3. Frontend Setup (Streamlit)

```bash
cd ../frontend
streamlit run main.py
```

---

## 🌐 API Endpoints (FastAPI)

| Method | Endpoint   | Description                      |
| ------ | ---------- | -------------------------------- |
| POST   | `/predict` | Returns cost prediction          |
| GET    | `/`        | Returns Hello!                   |
| GET    | '/home'    | Returns Welcome! The API is live |

---

## 📈 Model Performance

| Group    | Model             | Accuracy |
| -------- | ----------------- | -------- |
| Age ≤ 25 | XGBoost Regressor | 98%      |
| Age > 25 | XGBoost Regressor | 99%      |

* Hyperparameter tuning done via `RandomizedSearchCV`
* Metrics used: `R² Score`, `MAE`, `RMSE`

---

## 💡 Key Insights

* Smokers incur significantly higher insurance charges
* Age and BMI are strong predictors
* Model segmentation greatly improved performance

---
![Screenshot 2025-06-29 114724](https://github.com/user-attachments/assets/d15d9a73-9c31-42d3-9d42-b3cef11c1d61)
