from sklearn.metrics import accuracy_score, classification_report
from src.train_model import train

def evaluate():
    model, X_test, y_test = train()
    predictions = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, predictions))
    print("\nClassification Report:\n", classification_report(y_test, predictions))
