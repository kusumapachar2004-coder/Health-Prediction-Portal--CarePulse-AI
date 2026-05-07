import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# ================= LOAD DATA =================
diabetes = pd.read_csv("datasets/diabetes.csv")
heart = pd.read_csv("datasets/heart.csv")

# ================= DIABETES MODEL =================
X_d = diabetes.drop("Outcome", axis=1)
y_d = diabetes["Outcome"]

X_train_d, X_test_d, y_train_d, y_test_d = train_test_split(X_d, y_d, test_size=0.2, random_state=42)

model_diabetes = XGBClassifier()
model_diabetes.fit(X_train_d, y_train_d)

y_pred_d = model_diabetes.predict(X_test_d)

print("\n===== DIABETES MODEL =====")
print("Accuracy:", accuracy_score(y_test_d, y_pred_d))
print("\nClassification Report:\n", classification_report(y_test_d, y_pred_d))
print("\nConfusion Matrix:\n", confusion_matrix(y_test_d, y_pred_d))

pickle.dump(model_diabetes, open("models/diabetes_model.pkl", "wb"))


# ================= HEART MODEL =================
X_h = heart.drop("target", axis=1)
y_h = heart["target"]

X_train_h, X_test_h, y_train_h, y_test_h = train_test_split(X_h, y_h, test_size=0.2, random_state=42)

model_heart = XGBClassifier()
model_heart.fit(X_train_h, y_train_h)

y_pred_h = model_heart.predict(X_test_h)

print("\n===== HEART MODEL =====")
print("Accuracy:", accuracy_score(y_test_h, y_pred_h))
print("\nClassification Report:\n", classification_report(y_test_h, y_pred_h))
print("\nConfusion Matrix:\n", confusion_matrix(y_test_h, y_pred_h))

pickle.dump(model_heart, open("models/heart_model.pkl", "wb"))