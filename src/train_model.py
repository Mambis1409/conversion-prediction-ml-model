from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

from src.preprocess import load_and_clean

def train():
    df = load_and_clean()

    X = df.drop("converted", axis=1)
    y = df["converted"]

    X = pd.get_dummies(X)  # encode categorical features

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    return model, X_test, y_test
