📌 AI-Based Online UPI Fraud Detection System
🔍 Project Overview

This project is an AI + Rule-Based Fraud Detection System built using Flask and Machine Learning.
It detects whether a UPI transaction is Safe, Suspicious, or Fraudulent using:

Machine Learning model prediction
Rule-based fraud detection logic
User authentication system with OTP verification
Admin dashboard for monitoring users and transactions
🚀 Features
👤 User Features
User registration with OTP verification (Email-based)
Secure login system
Real-time fraud prediction for transactions
Transaction history tracking
Result classification:
✅ Safe Transaction
⚠️ Suspicious Transaction
❌ Fraud Detected
🔐 Admin Features
Admin login system
View all users
View all transactions
Fraud analytics dashboard
Delete user (except admin)
🤖 AI/ML Features
Fraud prediction using trained ML model (fraud_model.pkl)
Feature-based input analysis:
Transaction amount
Balance changes
Device change
Location change
Hybrid decision system:
ML Model + Rule-based logic
🛠️ Tech Stack
Frontend: HTML, CSS
Backend: Flask (Python)
Machine Learning: Scikit-learn
Database: SQLite
Email Service: Flask-Mail (SMTP Gmail)
Others: Session management, OTP authentication
📂 Project Structure
AiBasedOnlineFraudTrasactionDetectionSystem/
│
├── app.py
├── utils/
│   ├── auth.py
│   ├── database.py
│   ├── predict.py
│   ├── fraud_rules.py
│   ├── analytics.py
|   |__ preprocess.py
│
├── model/
│   ├── train_model.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── user_dashboard.html
│   ├── admin_dashboard.html
|   |__ forgot_password.html
|   |__ index.html
|   |__ reset_password.html
|   |__ verify_otp.html
|   |__ verify_reset_otp.html
│   ├── result.html
│
├── static/
│   ├── css/
│
├── requirements.txt
├── .gitignore
└── README.md
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/Rishika-Reddy-18/AiBasedFraudTransactionDetectionSystem.git
cd AiBasedFraudTransactionDetectionSystem
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set Environment Variables

Create .env file:

MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
SECRET_KEY=your_secret_key
5️⃣ Run Project
python app.py

Open in browser:

http://127.0.0.1:5000/
🧠 Machine Learning Model

The model uses supervised learning to detect fraud based on:

Transaction amount
Balance before & after transaction
Device change
Location change
Output Classes:
0 → Safe Transaction
1 → Fraudulent Transaction
📊 System Flow
User Login → Enter Transaction → ML Model Prediction + Rules
        ↓
   Result Display (Safe / Fraud / Suspicious)
        ↓
   Stored in Database
        ↓
   Admin Dashboard Monitoring
🔐 Security Features
Password hidden in login/register forms
OTP-based email verification
Session-based authentication
Environment variables for sensitive data
Admin-only access control
📈 Future Improvements
Deploy on cloud (AWS / Render / Railway)
Add payment gateway simulation
Improve ML accuracy with deep learning
Add SMS OTP verification
Real-time fraud alert system
👩‍💻 Author

Rishika Reddy

Project: AI-Based Online Fraud Detection System
Domain: AI Ml,AI DEVELOPER

⭐ If you like this project

Give a ⭐ on the repository and feel free to contribute!