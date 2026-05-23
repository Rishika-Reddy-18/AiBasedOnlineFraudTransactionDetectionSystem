from flask import Flask, render_template, request, redirect, session
from flask_mail import Mail, Message
import random
import os
from dotenv import load_dotenv

from utils.database import init_db, get_connection
from utils.auth import register_user, validate_user
from utils.predict import predict_fraud
from utils.fraud_rules import rule_based_check
from utils.analytics import get_user_stats

# ================= LOAD ENV VARIABLES =================
load_dotenv()

# ================= APP CONFIG =================
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback_secret")

# ================= MAIL CONFIG =================
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)

# ================= INIT DB =================
init_db()


# ================= HOME =================
@app.route("/")
def home():
    return redirect("/login")


# ================= REGISTER PAGE =================
@app.route("/register")
def register():
    return render_template("register.html")


# ================= SEND OTP =================
@app.route("/send_otp", methods=["POST"])
def send_otp():

    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    otp = str(random.randint(100000, 999999))

    session["temp_username"] = username
    session["temp_email"] = email
    session["temp_password"] = password
    session["temp_otp"] = otp

    msg = Message(
        "OTP Verification",
        sender=app.config['MAIL_USERNAME'],
        recipients=[email]
    )

    msg.body = f"Your OTP is: {otp}"
    mail.send(msg)

    return render_template("verify_otp.html")


# ================= VERIFY OTP =================
@app.route("/verify_otp", methods=["POST"])
def verify_otp():

    otp = request.form.get("otp")

    if otp == session.get("temp_otp"):

        register_user(
            session.get("temp_username"),
            session.get("temp_email"),
            session.get("temp_password"),
            role="user"
        )

        session.pop("temp_username", None)
        session.pop("temp_email", None)
        session.pop("temp_password", None)
        session.pop("temp_otp", None)

        return redirect("/login")

    return "Invalid OTP"


# ================= LOGIN =================
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = validate_user(username, password)

        if user:
            session["user"] = user[1]
            session["role"] = user[4]

            if user[4] == "admin":
                return redirect("/admin_dashboard")
            else:
                return redirect("/user_dashboard")

        return "Invalid credentials"

    return render_template("login.html")


# ================= USER DASHBOARD =================
@app.route("/user_dashboard")
def user_dashboard():

    if "user" not in session:
        return redirect("/login")

    return render_template("user_dashboard.html")


# ================= FRAUD PREDICTION =================
@app.route("/predict", methods=["POST"])
def predict():

    if "user" not in session:
        return redirect("/login")

    data = {
        "step": float(request.form["step"]),
        "type": float(request.form["type"]),
        "amount": float(request.form["amount"]),
        "oldbalanceOrg": float(request.form["oldbalanceOrg"]),
        "newbalanceOrig": float(request.form["newbalanceOrig"]),
        "oldbalanceDest": float(request.form["oldbalanceDest"]),
        "newbalanceDest": float(request.form["newbalanceDest"]),
        "device_change": float(request.form["device_change"]),
        "location_change": float(request.form["location_change"])
    }

    ml_result, fraud_probability = predict_fraud(data)
    rule_result = rule_based_check(data)

    if fraud_probability >= 75 or rule_result == "FRAUD":
        final_result = "FRAUD DETECTED"
        color = "red"
    elif fraud_probability >= 40 or rule_result == "SUSPICIOUS":
        final_result = "SUSPICIOUS TRANSACTION"
        color = "orange"
    else:
        final_result = "SAFE TRANSACTION"
        color = "green"

    # ================= SAVE TRANSACTION =================
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions (username, amount, prediction, fraud_probability)
        VALUES (?, ?, ?, ?)
    """, (
        session["user"],
        data["amount"],
        final_result,
        fraud_probability
    ))

    conn.commit()
    conn.close()

    return render_template(
        "result.html",
        prediction=final_result,
        color=color,
        fraud_probability=fraud_probability,
        ml_result=ml_result,
        rule_flag=rule_result
    )


# ================= ADMIN DASHBOARD =================
@app.route("/admin_dashboard")
def admin_dashboard():

    if "user" not in session or session["role"] != "admin":
        return redirect("/login")

    view = request.args.get("view", "home")
    stats = get_user_stats()

    conn = get_connection()
    cursor = conn.cursor()

    users = []
    if view == "users":
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

    conn.close()

    return render_template(
        "admin_dashboard.html",
        view=view,
        users=users,
        total_users=stats["total_users"],
        total_txn=stats["total_transactions"],
        fraud_count=stats["fraud_count"],
        safe_count=stats["safe_count"],
        accuracy=97.5,
        precision=0.92,
        recall=0.88
    )


# ================= DELETE USER =================
@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):

    if "user" not in session or session["role"] != "admin":
        return redirect("/login")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT role FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    if user and user[0] == "admin":
        return "Cannot delete admin user"

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

    return redirect("/admin_dashboard?view=users")


# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)