# Prediction of Temporal Series: Energy Consumption Forecasting

> **Objective**: Build a professional-grade, cloud-ready machine learning pipeline for energy consumption forecasting using multivariate time series data. The project is designed for high-level deployment and real-time applications, suitable for showcasing in a data science portfolio targeting top-tier tech companies.

---

## 🔍 Project Overview

This project focuses on forecasting electricity consumption using time series data provided by [Kaggle: Energy Consumption, Generation, Prices and Weather](https://www.kaggle.com/datasets/nicholasjhana/energy-consumption-generation-prices-and-weather).

The goal is to create a robust pipeline that handles data ingestion, exploratory analysis, feature engineering, model training (ML and DL), and deployment via containerized services.

---

## 📁 Project Structure

    ```
    .
    ├── configs/                # YAML/JSON configuration files (hyperparams, paths, DAGs)
    ├── data/                   # Raw and processed data files
    ├── docker/                 # (optional) Dockerfiles and Docker Compose configs
    ├── models/                 # Trained models and serialized objects
    ├── notebooks/             # EDA in R and modeling in Python
    │   ├── 01_EDA_in_R.Rmd
    │   └── 02_Modeling_in_Python.ipynb
    ├── reports/               # Generated reports and plots
    ├── src/                   # Source code modules
    │   ├── data/              # Data loading and preprocessing
    │   ├── features/          # Feature engineering
    │   ├── models/            # Training and prediction scripts
    ├── tests/                 # Unit tests
    ├── requirements.txt       # Python dependencies (legacy)
    ├── pyproject.toml         # Poetry environment configuration
    ├── Prediction-Temporal-Series.Rproj # RStudio project file
    ├── README.md
    └── .env                   # Environment variables (e.g., API keys)
    ```

---

## 🚀 Tech Stack

### Data Collection & Processing

* Python (pandas, numpy, requests)
* Apache Airflow (ETL orchestration)
* AWS S3 (cloud storage)

### Data Exploration & Visualization

* R (ggplot2, dplyr, tidyr)
* Python (matplotlib, seaborn, plotly)

### Modeling

* Scikit-learn, XGBoost, Prophet
* TensorFlow/Keras (LSTM, optional)
* PyTorch (optional for advanced DL)

### Deployment & DevOps

* FastAPI (model serving)
* Docker, Kubernetes (EKS)
* GitHub Actions (CI/CD)

---

## 📊 Goals

* [ ] Automate dataset ingestion with Airflow DAG
* [ ] Perform deep EDA in R and summarize for Python workflows
* [ ] Engineer temporal and exogenous features
* [ ] Train and evaluate multiple models (baseline, ML, DL)
* [ ] Deploy the best-performing model with FastAPI in Docker
* [ ] Monitor predictions and model drift
* [ ] Simulate or transition to a real-time ingestion pipeline

---

## 📊 EDA Notebook

A detailed exploratory data analysis was conducted in R, covering:

* Data quality inspection
* Temporal patterns (hourly, daily, monthly)
* Correlation analysis and actionable insights

🧾 [View the full EDA notebook (RPubs)](http://rpubs.com/Alex_matias_as/energy-weather-eda)

---

## 📦 Getting Started

    ```bash
    # Clone the repository
    $ git clone https://github.com/alexmatiasas/Prediction-Temporal-Series.git
    $ cd Prediction-Temporal-Series

    # Install dependencies (Python)
    $ poetry install

    # Set up R environment
    $ R
    > install.packages("renv")
    > renv::init()
    ```

---

## 🧪 Testing & Validation

* Unit testing with `pytest`
* Coverage reports (optional)
* CI workflows via GitHub Actions

---

## 📈 Deployment

* Model served via REST API (FastAPI)
* Deployed in Docker containers (AWS EC2/EKS)
* Optionally monitored using Prometheus & Grafana

---

## 🔒 Environment Variables

Create a `.env` file in the root folder for API keys and sensitive config:

    ```
    KAGGLE_USERNAME=your_username
    KAGGLE_KEY=your_key
    WEATHER_API_KEY=...
    ```

---

## 🧠 Author

**Alejandro Matías Astorga**
PhD in Physics | Data Scientist | Machine Learning Engineer
[Portfolio](https://alexmatiasas.github.io) | [GitHub](https://github.com/alexmatiasas)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
