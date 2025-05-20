# 🧠 Sales Forecasting

A full-stack machine learning project that predicts **future product sales** based on historical retail data.  
Built using **time series models (ARIMA/SARIMA)** and deployed as a **live Flask API on Render**, with a **Streamlit dashboard** for visualization.

---

## 📌 Project Highlights

- 📊 Real-world retail dataset (multi-year sales records)
- 🧼 Full data cleaning, aggregation, and feature engineering
- 📈 Time series modeling with ARIMA & SARIMA
- 📤 14-day forward forecast with model evaluation
- 🌐 Live API endpoint + 🖥️ Interactive dashboard

---

## 📂 Dataset Information

**Source**: Custom retail dataset  
**Records**: 4 years of daily sales  
**Target**: `Sales` (Numeric)

---

## ⚙️ Technologies Used

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green)
![Statsmodels](https://img.shields.io/badge/Statsmodels-0.13.x-orange)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)

- **Data Processing**: Pandas, NumPy
- **Visualization**: Seaborn, Matplotlib
- **Time Series Modeling**: ARIMA, SARIMA (Statsmodels)
- **API Development**: Flask
- **Frontend Visualization**: Streamlit
- **Deployment**: Render (API), Streamlit Cloud (Dashboard)
- **Version Control**: Git & GitHub

---

## 📈 Model Performance

| Model   | MAE     | RMSE  | MAPE       | Period |
|---------|---------|-------|------------|--------|
| SARIMA  | 1557.48 | 2208.97 | 102.93%  | Last 14 Days |
| ARIMA   | 1710.80 | 2422.67 | 114.03%  | Last 14 Days |
| XGBoost   | 1315.72 | 1542.60 | 183.66%  | Last 14 Days |
| XGBoost (Log-Transformed)  | 1300.52 | 1784.77 | 73.69%  | Last 14 Days |

> *Models evaluated on last 14 days of sales, following walk-forward validation.*
## ✨ Author

**Manish Saini**  
🎓 B.E. in Computer Science, Chandigarh University  
📍 Alwar, Rajasthan  
🔗 [LinkedIn](https://www.linkedin.com/in/manish-saini-274a371b4/)  
🛠️ 6-Star HackerRank | 1500+ DSA Problems Solved

---

## 🧠 Contact Me

Looking for a Data Scientist, freelance ML developer or intern?

📧 **Email**: [msaini720415@gmail.com](mailto:msaini720415@gmail.com)

---


