import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Create models folder
os.makedirs('models', exist_ok=True)

# Load dataset
df = pd.read_csv('datasets/diabetes.csv')

print("Diabetes Dataset Loaded")
print(df.head())

# Check columns
print("Columns:", df.columns)

# Split
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier(class_weight='balanced', random_state=42)
model.fit(X_train, y_train)
from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
# Save model
with open('models/diabetes_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Diabetes model created successfully!")