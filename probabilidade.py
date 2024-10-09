import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregue seu dataset a partir do arquivo CSV
df = pd.read_csv('creditcard/creditcard_2023.csv')

# Exibir os nomes das colunas
print("Colunas do dataset:")
print(df.columns)
# Exiba as primeiras linhas do DataFrame para entender sua estrutura
print(df.head())

# Escolher a coluna para análise (exemplo: 'Amount')
coluna = 'Amount'  # Pode ajustar para outra coluna relevante do dataset

# Cálculo das estatísticas
media = df[coluna].mean()
mediana = df[coluna].median()
desvio_padrao = df[coluna].std()

# Exibir as estatísticas
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Desvio Padrão: {desvio_padrao}")

# Plotar histograma com média, mediana e desvio padrão
plt.figure(figsize=(10, 6))
sns.histplot(df[coluna], bins=30, kde=True)
plt.axvline(media, color='red', linestyle='dashed', linewidth=1, label='Média')
plt.axvline(mediana, color='green', linestyle='dashed', linewidth=1, label='Mediana')
plt.axvline(media + desvio_padrao, color='orange', linestyle='dashed', linewidth=1, label='Desvio Padrão (+)')
plt.axvline(media - desvio_padrao, color='orange', linestyle='dashed', linewidth=1, label='Desvio Padrão (-)')
plt.title('Histograma com Média, Mediana e Desvio Padrão')
plt.xlabel(coluna)
plt.ylabel('Frequência')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de frequência (quantidade de ocorrências de cada valor)
plt.figure(figsize=(10, 6))
sns.histplot(df[coluna].value_counts(), bins=30, kde=True)
plt.title(f'Gráfico de Frequência - {coluna}')
plt.xlabel('Frequência')
plt.ylabel('Ocorrências')
plt.grid(True)
plt.show()

# Cálculo e exibição da frequência média (quantidade média de vezes que cada valor aparece)
frequencia_media = df[coluna].value_counts().mean()
print(f'Frequência média: {frequencia_media}')