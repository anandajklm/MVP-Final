# MVP Final - Modelo de Machine Learning com Aplicação Full Stack

Este repositório contém o projeto final da disciplina **Qualidade de Sofware, Segurança e Sistemas**. Foi desenvolvido um modelo de machine learning para classificar inadimplência com base em dados financeiros e uma aplicação full stack em Flask para entrada e predição de novos dados, além de um teste automatizado com PyTest.


---

## ▶️ Como executar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e ative um ambiente virtual

**No macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**No Windows (PowerShell):**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install flask scikit-learn pandas joblib pytest
```

---

## 🚀 Executar a aplicação

Após instalar as dependências, rode o servidor local com:

```bash
python app.py
```


---

## 🧪 Rodar os testes automatizados

Para verificar se o modelo atende ao desempenho mínimo (recall):

```bash
pytest test_model.py
```

Se o recall da classe 1 (inadimplentes) for maior ou igual a 0.30, o teste será aprovado com sucesso.

---

## 🧠 Sobre o modelo

- Dataset: [Default of Credit Card Clients Dataset](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)
- O objetivo é prever inadimplência com base em dados como limite de crédito, histórico de pagamento e idade.
- Modelos testados:
  - K-Nearest Neighbors (KNN)
  - Árvore de Decisão
  - Naive Bayes
  - Suporte a Vetores (SVM)
- Apesar do SVM ter apresentado melhor desempenho em métricas, ele foi descartado por **problemas de performance na exportação** com base grande de dados.
- O modelo escolhido foi o **KNN**, por equilibrar bem desempenho e velocidade, com recall satisfatório.
- Métrica principal: **Recall da classe 1** (inadimplentes)



---


