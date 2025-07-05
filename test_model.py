import joblib
import numpy as np
from sklearn.metrics import recall_score

def test_model_recall():
    # Carregar modelo e scaler
    model = joblib.load("knn_model.pkl")
    scaler = joblib.load("scaler.pkl")

    # Carregar dados de teste
    X_test = joblib.load("X_test.pkl")
    y_test = joblib.load("y_test.pkl")

    # Aplicar o scaler
    X_test_scaled = scaler.transform(X_test)

    # Fazer predição
    y_pred = model.predict(X_test_scaled)

    # Calcular o recall da classe 1
    recall = recall_score(y_test, y_pred, pos_label=1)

    # Definir o threshold mínimo aceitável
    assert recall >= 0.30, f"Recall muito baixo: {recall}"

