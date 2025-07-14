import numpy as np
import pandas as pd
import seaborn as sns

# Estilo visual dos gráficos
sns.set_theme(style="whitegrid")

# Semente para gerar os mesmos dados sempre
np.random.seed(42)

# Número de chamados simulados
n = 100

# Gerar dados fictícios
dados = pd.DataFrame({
    'ID': range(1, n + 1),
    'Tipo': np.random.choice(['Incidente', 'Requisição'], size=n),
    'Prioridade': np.random.choice(['Alta', 'Média', 'Baixa'], size=n, p=[0.2, 0.5, 0.3]),
    'Departamento': np.random.choice(['Infraestrutura', 'Sistemas', 'Suporte'], size=n),
    'Data_Abertura': pd.date_range(start='2024-01-01', periods=n, freq='D')
})

# Tempo de resolução em horas (simulado com base na prioridade)
def gerar_tempo(prioridade):
    if prioridade == 'Alta':
        return abs(np.random.normal(8, 2))
    elif prioridade == 'Média':
        return abs(np.random.normal(16, 4))
    else:
        return abs(np.random.normal(24, 6))

dados['Tempo_Resolucao_h'] = dados['Prioridade'].apply(gerar_tempo)

# Data de fechamento = abertura + tempo
dados['Data_Fechamento'] = dados['Data_Abertura'] + pd.to_timedelta(dados['Tempo_Resolucao_h'], unit='h')

# Status final (95% resolvidos, 5% cancelados)
dados['Status'] = np.random.choice(['Resolvido', 'Cancelado'], size=n, p=[0.95, 0.05])

# Exibir os 5 primeiros registros
print(dados.head())

np.random.choice(['Incidente', 'Requisição'], size=n)

np.random.choice(['Alta', 'Média', 'Baixa'], size=n, p=[0.2, 0.5, 0.3])

def gerar_tempo(prioridade):
    if prioridade == 'Alta':
        return abs(np.random.normal(8, 2))

dados['Tempo_Resolucao_h'] = dados['Prioridade'].apply(gerar_tempo)

pd.to_timedelta(dados['Tempo_Resolucao_h'], unit='h')

import matplotlib.pyplot as plt
import seaborn as sns

# Estilo visual
sns.set(style="whitegrid")

# Gráfico 1 – Quantidade de chamados por prioridade
plt.figure(figsize=(6, 4))
sns.countplot(data=dados, x="Prioridade", hue="Prioridade", palette="pastel", legend=False)
plt.title("Quantidade de Chamados por Prioridade")
plt.xlabel("Prioridade")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig('../output/grafico 1.png')
plt.show()

# Gráfico 2 – Tempo de resolução por departamento (boxplot)
plt.figure(figsize=(6, 4))
sns.boxplot(data=dados, x="Departamento", hue="Departamento", y="Tempo_Resolucao_h", palette="Set2", legend=False)
plt.title("Tempo de Resolução por Departamento")
plt.xlabel("Departamento")
plt.ylabel("Horas")
plt.tight_layout()
plt.savefig('../output/grafico 2.png')
plt.show()

# Gráfico 3 – Status dos chamados (Resolvido x Cancelado)
plt.figure(figsize=(6, 4))
sns.countplot(data=dados, x="Status", hue="Status", palette="muted", legend=False)
plt.title("Status Final dos Chamados")
plt.xlabel("Status")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig('../output/grafico 3.png')
plt.show()
