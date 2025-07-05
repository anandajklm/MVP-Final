from flask import Flask, render_template, request
import numpy as np
import joblib

# Inicializar a aplicação Flask
app = Flask(__name__)

# Carregar o modelo e o scaler
model = joblib.load("knn_model.pkl")
scaler = joblib.load("scaler.pkl")

# Página principal com formulário
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        # Coletar os dados do formulário e converter para array
        input_data = [
            float(request.form.get(col)) for col in request.form.keys()
        ]
        input_array = np.array(input_data).reshape(1, -1)

        # Escalar os dados
        input_scaled = scaler.transform(input_array)

        # Fazer a predição
        pred = model.predict(input_scaled)[0]
        prediction = "Inadimplente" if pred == 1 else "Adimplente"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    print("Iniciando aplicação Flask...")
    app.run(debug=True)

