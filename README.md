# 📌 AI Based Online Fraud Transaction Detection System

---

## 🔍 Project Overview

The **AI Based Online Fraud Transaction Detection System** is a Flask-based web application integrated with Machine Learning and Rule-Based logic to detect fraudulent UPI transactions in real-time.

It classifies transactions into:

- ✅ Safe Transaction  
- ⚠️ Suspicious Transaction  
- ❌ Fraudulent Transaction  

The system enhances financial security using:

- Machine Learning prediction model  
- Rule-based fraud detection engine  
- OTP-based user authentication  
- Admin monitoring dashboard  

---

## 🚀 Key Features

---

### 👤 User Features

- User registration with OTP verification (Email-based)
- Secure login system
- Real-time fraud prediction
- Transaction input form
- Result classification (Safe / Suspicious / Fraud)
- Password reset via OTP

---

### 🔐 Admin Features

- Admin dashboard
- View all registered users
- View all transactions
- Fraud analytics overview
- Delete users (except admin)

---

### 🤖 AI / ML Features

- Fraud detection using trained ML model
- Rule-based fraud detection logic
- Feature analysis:
  - Transaction amount
  - Balance changes
  - Device change
  - Location change
- Hybrid decision system (ML + Rules)

---

## 🛠️ Tech Stack

- Frontend: HTML, CSS  
- Backend: Flask (Python)  
- Machine Learning: Scikit-learn  
- Database: SQLite  
- Email Service: Flask-Mail (SMTP Gmail)  
- Security: Session management + OTP authentication  

---

## 📂 Project Structure

```txt
AiBasedOnlineFraudTransactionDetectionSystem/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── utils/
│   ├── auth.py
│   ├── database.py
│   ├── predict.py
│   ├── fraud_rules.py
│   ├── analytics.py
│   ├── preprocess.py
│
├── model/
│   ├── train_model.py
│   └── (ML model files stored externally)
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── user_dashboard.html
│   ├── admin_dashboard.html
│   ├── result.html
│   ├── forgot_password.html
│   ├── index.html
│   ├── reset_password.html
│   ├── verify_otp.html
│   ├── verify_reset_otp.html
│
├── static/
│   ├── css/
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/Rishika-Reddy-18/AiBasedOnlineFraudTransactionDetectionSystem.git
cd AiBasedOnlineFraudTransactionDetectionSystem
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Environment Variables

Create a .env file:

MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
SECRET_KEY=your_secret_key
5️⃣ Run Application
python app.py

Open in browser:

http://127.0.0.1:5000/
🧠 Machine Learning Model

The system uses a trained supervised ML model for fraud detection.

Features used:
Transaction amount
Old and new balances
Device change
Location change
Output:
0 → Safe Transaction
1 → Fraudulent Transaction
📊 System Flow

User Login → Transaction Input → ML Prediction + Rule Engine → Result Display → Store in Database → Admin Monitoring

🔐 Security Features
OTP-based email verification
Password protection in login/register
Session-based authentication
Admin-only access control
Environment variable protection
📈 Future Improvements
Cloud deployment (AWS / Render / Railway)
Real-time fraud alert system
SMS OTP authentication
Deep learning model integration
API-based microservice architecture
👩‍💻 Author

Rishika Reddy
AI-Based Online Fraud Transaction Detection System
Domain: Artificial Intelligence / Machine Learning

⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork it
🚀 Share it
