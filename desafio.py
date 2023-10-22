# Extrair os dados
import pandas as pd
#Importa dos dados dos candidatos e score de aderêcia numa vaga de Analista de Dados
df = pd.read_csv('dados_candidato.csv')
print(df)

# Transformação
# Agora vamos calcular o total de vendas por produto e por mês.
# Calculando a média
media_score = df['Score'].mean()
print("Média dos Scores dos Candidatos:", media_score)


# Load

import matplotlib.pyplot as plt
# Criando gráfico de barras para os scores do gráfico
# Cores personalizadas para as barras
cores = ['purple', 'green', 'red', 'blue', 'orange']

plt.bar(df['Candidato'], df['Score'], color=cores)

# Adicionando os valores das barras como rótulos
for i, score in enumerate(df['Score']):
    plt.text(i, score, f'{score:.2f}', ha='center', va='bottom')
plt.xlabel('Candidatos')
plt.ylabel('Scores')
plt.title('Scores dos candidatos')
plt.xticks(rotation=45, ha='right')
plt.show()


# Criando um gráfico de barras
plt.figure(figsize=(10, 6))

# Plotando a média dos scores como uma linha
plt.axhline(media_score, color='red', linestyle='--', label='Média dos Scores')

# Criando um gráfico de comparação dos scores dos candidatos com a média
plt.bar(df['Candidato'], df['Score'], color=cores, label='Score dos Candidatos')


for i, score in enumerate(df['Score']):
    plt.text(i, score, f'{score:.2f}', ha='center', va='bottom')

plt.xlabel('Candidato')
plt.ylabel('Score')
plt.title('Comparação da Média e Scores dos Candidatos')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()

plt.show()