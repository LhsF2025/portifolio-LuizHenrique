# 1. Importa as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Lê o arquivo do Forms
arquivo = '../data/respostas.xlsx'  # Caminho até o arquivo
df = pd.read_excel(arquivo)         # Lê o arquivo usando pandas

# 3. Mostra as 5 primeiras respostas
print("Pré-visualização dos dados:")
print(df.head())

# 4. Mostra as perguntas (nomes das colunas)
print("\nPerguntas disponíveis:")
print(df.columns)

# 5. Nome exato da pergunta (como apareceu no print do df.columns)
pergunta = "Você indicaria esse produto? (Sim/Não)"

# 6. Conta as respostas
contagem = df[pergunta].value_counts()

# 7. Mostra no terminal
print(f"\nRespostas para: {pergunta}")
print(contagem)

# 8. Gera um gráfico de barras
sns.set(style="whitegrid")
plt.figure(figsize=(8,5))
sns.barplot(x=contagem.values, y=contagem.index,)
plt.title(pergunta)
plt.xlabel("Quantidade de respostas")
plt.ylabel("Opções")
plt.tight_layout()

# 9. Salva o gráfico como imagem
plt.savefig('../output/grafico.png')
plt.show()
