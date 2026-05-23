import joblib
import numpy as np

# =========================
# LOAD MODEL
# =========================

model = joblib.load("model/fraud_model.pkl")


def predict_fraud(data):

    step = float(data["step"])

    type_ = float(data["type"])

    amount = float(data["amount"])

    oldbalanceOrg = float(data["oldbalanceOrg"])

    newbalanceOrig = float(data["newbalanceOrig"])

    oldbalanceDest = float(data["oldbalanceDest"])

    newbalanceDest = float(data["newbalanceDest"])

    device_change = float(data["device_change"])

    location_change = float(data["location_change"])

    # =========================
    # FEATURE ENGINEERING
    # =========================

    balanceDiffOrig = (
        oldbalanceOrg - newbalanceOrig
    )

    balanceDiffDest = (
        newbalanceDest - oldbalanceDest
    )

    amount_ratio = (
        amount / (oldbalanceOrg + 1)
    )

    # night transaction
    night_transaction = 1 if (step % 24 <= 5) else 0

    # =========================
    # FEATURE ARRAY
    # =========================

    features = np.array([[
        step,
        type_,
        amount,
        oldbalanceOrg,
        newbalanceOrig,
        oldbalanceDest,
        newbalanceDest,
        balanceDiffOrig,
        balanceDiffDest,
        amount_ratio,
        device_change,
        location_change,
        night_transaction
    ]])

    # =========================
    # PREDICTION
    # =========================

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0][1]

    fraud_probability = round(probability * 100, 2)

    return int(prediction), fraud_probability