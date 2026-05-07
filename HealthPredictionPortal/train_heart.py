import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

print("STARTED HEART MODEL")

# Create models folder
os.makedirs('models', exist_ok=True)

try:
    # Load dataset
    df = pd.read_csv('datasets/heart.csv')
    print("DATA LOADED SUCCESSFULLY")

    print("Columns:", df.columns)

    # Split data
    X = df.drop('target', axis=1)
    y = df['target']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save model
    with open('models/heart_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    print("HEART MODEL CREATED SUCCESSFULLY")

except Exception as e:
    print("ERROR:", e)