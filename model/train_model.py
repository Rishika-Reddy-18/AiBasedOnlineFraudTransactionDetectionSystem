import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from utils.preprocess import load_and_preprocess

# =========================
# LOAD DATA
# =========================

X, y = load_and_preprocess()

print("Data loaded and preprocessed successfully")

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# =========================
# MODEL
# =========================

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=2,
    class_weight="balanced",
    random_state=42
)

# =========================
# TRAIN MODEL
# =========================

model.fit(X_train, y_train)

print("\nModel Training Completed")

# =========================
# PREDICTIONS
# =========================

y_pred = model.predict(X_test)

# =========================
# EVALUATION
# =========================

print("\nMODEL PERFORMANCE")
print("--------------------")

print("Accuracy :", accuracy_score(y_test, y_pred))

print("Precision:", precision_score(y_test, y_pred))

print("Recall   :", recall_score(y_test, y_pred))

print("F1 Score :", f1_score(y_test, y_pred))

# =========================
# CONFUSION MATRIX
# =========================

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

# =========================
# CLASSIFICATION REPORT
# =========================

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# =========================
# FEATURE IMPORTANCE
# =========================

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance")
print(feature_importance)

# =========================
# SAVE MODEL
# =========================

joblib.dump(model, "fraud_model.pkl")

print("\nModel saved successfully as fraud_model.pkl")