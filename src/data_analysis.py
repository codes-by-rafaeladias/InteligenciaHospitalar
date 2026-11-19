import pandas as pd

#Arquivo de análise de dados: contém exploração inicial sobre o dataset

df = pd.read_csv("./data/processed/diabetic_data.csv")

# 1. Quantos atendimentos foram registrados?

print(df["id_internacao"].count())

# 2. Quantos pacientes diferentes aparecem na base?

print(df["id_paciente"].nunique())

# 3. Um paciente pode ter mais de uma internação?

print(df["id_paciente"].duplicated().sum())

# 4. Qual é o tempo médio de permanência hospitalar?

print(df["tempo_internacao"].mean())

