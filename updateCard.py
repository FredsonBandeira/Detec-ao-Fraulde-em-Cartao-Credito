# Importar bibliotecas
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import joblib
import shap
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("creditcard/creditcard_2023.csv")


X = data.drop("Class", axis=1)  # 'Class' é a variável alvo (0: legítimo, 1: fraudulento)
y = data["Class"]

# Escalonar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir o dataset em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Balancear os dados usando SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_resampled, y_resampled)


y_pred = model.predict(X_test)

# Avaliar o modelo
print("Matriz de Confusão:")
print(confusion_matrix(y_test, y_pred))
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

# Calcular a Curva ROC e AUC
y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = roc_auc_score(y_test, y_prob)

# Plotar a Curva ROC
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC Curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC)')
plt.legend(loc="lower right")
plt.show()

# Avaliar o modelo com validação cruzada
cv_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='accuracy')
print(f"Acurácia média em Cross Validation: {np.mean(cv_scores):.4f}")

# Exibir a importância das variáveis
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

# Exibir as features mais importantes
print("\nImportância das Variáveis:")
for f in range(X.shape[1]):
    print(f"{f + 1}. Feature {indices[f]} ({importances[indices[f]]})")

# Plotar a importância das features
plt.figure(figsize=(10, 6))
plt.title("Feature Importance")
plt.bar(range(X.shape[1]), importances[indices], align='center')
plt.xticks(range(X.shape[1]), X.columns[indices], rotation=90)
plt.tight_layout()
plt.show()

# Ajuste de Hiperparâmetros com RandomizedSearchCV
param_dist = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
}

random_search = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=100, cv=3, random_state=42, n_jobs=-1)
random_search.fit(X_resampled, y_resampled)

print(f"\nMelhores parâmetros: {random_search.best_params_}")

# Avaliar o modelo ajustado
best_model = random_search.best_estimator_
y_pred_best = best_model.predict(X_test)
print(confusion_matrix(y_test, y_pred_best))
print(classification_report(y_test, y_pred_best))


explainer = shap.TreeExplainer(best_model)
shap_values = explainer.shap_values(X_test)


shap.summary_plot(shap_values[1], X_test, plot_type="bar")


joblib.dump(best_model, 'random_forest_model.pkl')


loaded_model = joblib.load('random_forest_model.pkl')
