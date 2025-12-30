
# 🚗 AI Car Price Prediction System
[![Live Demo](https://img.shields.io/badge/Demo-Live%20App-success?style=for-the-badge&logo=render)](https://ai-car-price-prediction-system.onrender.com)

An end-to-end machine learning web application that predicts the resale price of used cars based on historical data and market-driven features. The system combines a robust ML pipeline with a production-grade Flask backend and an enterprise-style UI designed for real-world usability and interviews.

---

## 🔍 Project Overview

Estimating the resale value of used cars is a common real-world problem influenced by multiple factors such as car age, mileage, fuel type, ownership history, brand value, and transmission type.

This project solves that problem using **supervised machine learning regression**, enhanced with:

* Feature scaling
* Target encoding for high-cardinality categorical features
* Post-prediction constraints to enforce real-world realism
* A modern, interactive web interface

---

## ✨ Key Features

* 🎥 **Auto-Demo Mode**
  One-click automated demo that generates realistic, randomized inputs within safe feature ranges and instantly predicts results — ideal for interviews and quick showcases.

* 📊 **Prediction Confidence Score**
  A heuristic-based confidence percentage calculated from prediction deviation and feature stability, providing transparency to users.

* 🎨 **Enterprise Dark UI**
  Modern, responsive, recruiter-friendly interface with animations and clear visual hierarchy.

* 🧠 **Production-Safe ML Output**
  Post-processing logic prevents negative or unrealistic price predictions, mimicking real-world ML deployment practices.

---

## 🧠 Machine Learning Pipeline

1. **Data Preprocessing**

   * Handling numerical and categorical features
   * Normalization using `StandardScaler`
   * Brand feature encoded using **Target Encoding**

2. **Model Training**

   * Regression-based model trained on historical car resale data
   * Optimized for generalization across brands and price ranges

3. **Post-Prediction Processing**

   * Prediction clamping to realistic value ranges
   * Confidence estimation after correction

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Backend:** Flask
* **Machine Learning:** Scikit-learn
* **Data Processing:** Pandas, NumPy
* **Model Persistence:** Joblib
* **Frontend:** HTML, CSS (Custom Dark UI)

---

## 📁 Project Structure

```
ai-car-price-prediction-system/
│
├── app.py
├── reg_model.pkl
├── scaler.pkl
├── target_encode.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── styles.css
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/amareshtoxico/ai-car-price-prediction-system.git
cd ai-car-price-prediction-system
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🎥 Auto-Demo Mode (Interview Tip)

Click **“🎥 Run Auto Demo”** to:

* Auto-fill the form with realistic values
* Submit automatically
* Instantly display prediction + confidence

> Perfect for live demos without manual input.

---

## 📌 Why This Project Stands Out

* Realistic ML deployment considerations (output constraints)
* Clean separation of ML, backend, and frontend
* Interview-ready demo functionality
* Scalable architecture for future enhancements

---

## 📈 Future Enhancements

* Feature importance visualization (SHAP)
* Model performance dashboard
* User authentication
* Cloud deployment with CI/CD
* REST API for external consumption

---

## 🧑‍💻 Author

**Amaresh Virupakshi**
Machine Learning & Python Developer

---

## 📜 License

This project is licensed for educational and portfolio use.






