import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
import joblib


def load_and_preprocess():

    # =========================
    # PROJECT ROOT
    # =========================
    BASE_DIR = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )

    # =========================
    # DATASET PATH
    # =========================
    file_path = os.path.join(
        BASE_DIR,
        "model",
        "transactions.csv"
    )

    print("Loading dataset from:", file_path)

    # =========================
    # LOAD DATASET
    # =========================
    data = pd.read_csv(file_path, nrows=50000)

    # =========================
    # HANDLE NULL VALUES
    # =========================
    data = data.fillna(0)

    # =========================
    # BALANCE DATASET
    # =========================
    fraud = data[data["isFraud"] == 1]

    normal = data[data["isFraud"] == 0].sample(
        n=len(fraud) * 3,
        random_state=42
    )

    data = pd.concat([fraud, normal])

    # =========================
    # FEATURE ENGINEERING
    # =========================

    # sender balance difference
    data["balanceDiffOrig"] = (
        data["oldbalanceOrg"] - data["newbalanceOrig"]
    )

    # receiver balance difference
    data["balanceDiffDest"] = (
        data["newbalanceDest"] - data["oldbalanceDest"]
    )

    # amount ratio
    data["amount_ratio"] = (
        data["amount"] / (data["oldbalanceOrg"] + 1)
    )

    # =========================
    # REALISTIC DEVICE CHANGE
    # =========================
    data["device_change"] = np.where(
        data["isFraud"] == 1,
        np.random.binomial(1, 0.45, len(data)),
        np.random.binomial(1, 0.1, len(data))
    )

    # =========================
    # REALISTIC LOCATION CHANGE
    # =========================
    data["location_change"] = np.where(
        data["isFraud"] == 1,
        np.random.binomial(1, 0.35, len(data)),
        np.random.binomial(1, 0.05, len(data))
    )

    # =========================
    # NIGHT TRANSACTION
    # =========================
    data["night_transaction"] = np.where(
        (data["step"] % 24 <= 5),
        1,
        0
    )

    # =========================
    # SLIGHT FRAUD AMOUNT BOOST
    # =========================
    data.loc[data["isFraud"] == 1, "amount"] *= 1.1

    # =========================
    # SMALL NOISE
    # =========================
    data["amount"] = data["amount"] * (
    1 + np.random.normal(0, 0.05, len(data))
    )

    # =========================
    # ENCODE TRANSACTION TYPE
    # =========================
    encoder = LabelEncoder()

    data["type"] = encoder.fit_transform(data["type"])

    joblib.dump(encoder, "type_encoder.pkl")

    # =========================
    # FEATURES
    # =========================
    features = [
        "step",
        "type",
        "amount",
        "oldbalanceOrg",
        "newbalanceOrig",
        "oldbalanceDest",
        "newbalanceDest",
        "balanceDiffOrig",
        "balanceDiffDest",
        "amount_ratio",
        "device_change",
        "location_change",
        "night_transaction"
    ]

    X = data[features]

    y = data["isFraud"]

    return X, y