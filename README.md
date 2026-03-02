# 🎬 Netflix Customer Churn Prediction

A behavior-driven machine learning pipeline designed to predict future user engagement decline (churn) using temporal feature engineering and multi-model evaluation.

---

## 📌 Project Overview

This project implements a complete churn prediction system using:

- SQL-based temporal feature engineering
- Behavior-driven churn definition
- Multiple ML models for benchmarking
- Automated evaluation and visualization
- Deployment-ready model saving

The system predicts whether a user will significantly reduce engagement in the following month.

---

## 🛠 Tech Stack

### Backend & Modeling
- Python 3.9+
- Scikit-learn
- XGBoost
- Pandas
- NumPy

### Database
- PostgreSQL
- SQL Window Functions (LAG, LEAD, Rolling Metrics)

### Visualization
- Matplotlib
- Seaborn

### Model Serialization
- Joblib


---

## ⚙️ Setup Instructions

### 1️ Clone Repository
git clone https://github.com/Jayz-yuors/NETFLIX-Customer-Churn-Prediction.git
- cd NETFLIX-Customer-Churn-Prediction
### 2 Create Virtual Environment 
- python -m venv venv
- source venv/bin/activate  # Mac/Linux
- venv\Scripts\activate     # Windows
### 3 Install Dependencies
- pip install -r requirements.txt
### 4 Update Database
- db_config_1.py
- USE YOUR CREDENTIALS
- POPULATE YOUR DATABASE [ refer sql folder for sql scripts and also .. final_ml_dataset.csv in artefacts folder [ as a reference for data INGESTION ] 
### 5 Run Model Training
- python -m models.train_models


### Outputs Generated

- All outputs are saved inside:
- artifacts/

# LinkedIn Profile : www.linkedin.com/in/jay-keluskar-b17601358
- Kindly Visit my LinkedIn to know more about the Technicalities and Details related to the project.

