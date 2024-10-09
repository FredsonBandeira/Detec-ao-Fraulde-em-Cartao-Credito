# Importar bibliotecas
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Carregar dataset
data = pd.read_csv("creditcard/creditcard_2023.csv")


# Separar recursos e rótulo
X = data.drop("Class", axis=1)  # 'Class' é a variável alvo (0: legítimo, 1: fraudulento)
y = data["Class"]

# Escalonar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir o dataset em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Treinar o modelo de Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliar o modelo
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
