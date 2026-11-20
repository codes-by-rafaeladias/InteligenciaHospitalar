import pandas as pd
import matplotlib.pyplot as plt

#Arquivo de visualizações de dados: contém a criação de gráficos estáticos analíticos

df = pd.read_csv("./data/processed/diabetic_data.csv")

# Distribuição dos pacientes por faixa etária

distribuicao_faixa_etaria = df.groupby("age")["id_paciente"].nunique()

plt.figure(figsize=(10, 5))

plt.bar(distribuicao_faixa_etaria.index, distribuicao_faixa_etaria.values)

plt.title("Distribuição dos pacientes por faixa etária")
plt.xlabel("Faixa etária")
plt.ylabel("Quantidade de pacientes")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Distribuição por gênero

df["genero"] = df["genero"].replace({
    "Male": "Masculino",
    "Female": "Feminino",
    "Unknown/Invalid": "Desconhecido"
})

distribuicao_genero = df.groupby("genero")["id_paciente"].nunique()

distribuicao_genero.plot(
    kind="bar",
    figsize=(10, 5),
    color= "red"
)

plt.title("Distribuição dos pacientes por gênero")
plt.xlabel("Gênero")
plt.ylabel("Quantidade de pacientes")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Distribuição por raça

df["raca"] = df["raca"].replace({
    "?": "Não informado",
    "AfricanAmerican": "Afro-americano",
    "Asian": "Asiático",
    "Caucasian": "Branco",
    "Hispanic": "Hispânico",
    "Other": "Outro"
})

distribuicao_raca = df.groupby("raca")["id_paciente"].nunique()

distribuicao_raca.plot(
    kind="bar",
    figsize=(10, 5),
    color= "orange"
)

plt.title("Distribuição dos pacientes por raça")
plt.xlabel("Raça")
plt.ylabel("Quantidade de pacientes")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Quantidade de internações por grupo etário

internacoes_faixa_etaria = df.groupby("age")["id_internacao"].nunique()

internacoes_faixa_etaria.plot(
    kind="bar",
    figsize=(10, 5),
    color="green"
)

plt.title("Distribuição das internações por faixa etária")
plt.xlabel("Faixa etária")
plt.ylabel("Quantidade de internações")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Média de dias de internação

df["tipo_internacao"] = df["tipo_internacao"].replace({
    "Male": "Masculino",
    "Female": "Feminino",
    "Unknown/Invalid": "Desconhecido"
})

media_dias_internacao = df.groupby("tipo_internacao")["tempo_internacao"].mean()

media_dias_internacao.plot(kind="bar", figsize=(10,5), color="skyblue")

plt.title("Tempo médio de internação em dias por tipo de internação")
plt.xlabel("Tipo de internação")
plt.ylabel("Média de dias de internação")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Distribuição do tempo de permanência

dias_internacao = df["tempo_internacao"]

plt.hist(dias_internacao, color="blue", edgecolor="black")

plt.title("Distribuição do tempo de permanência")
plt.xlabel("Tempo de internação em dias")
plt.ylabel("Frequência")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# KPIs
media_dias_internacao = df["tempo_internacao"].mean()

media_exames_laboratoriais = df["qtd_exames_laboratoriais"].mean()

media_medicamentos = df["qtd_medicamentos"].mean()

taxa_readmissao = ((df['readmissao'] == '<30').sum() / len(df)) * 100

import matplotlib.pyplot as plt

kpis = [
    ('Tempo médio de internação', f'{media_dias_internacao:.1f} dias'),
    ('Quantidade média de exames laboratoriais', f"{media_exames_laboratoriais:.1f} exames"),
    ('Quantidade média de medicamentos administrados', f"{media_medicamentos:.0f}"),
    ('Taxa de Readmissão em até 30 dias', f"{taxa_readmissao:.2f}%")
]

# Criando os cartões
fig, axes = plt.subplots(1, 4, figsize=(16, 3))

colors = ['#3498DB', '#2ECC71', '#E67E22', '#9B59B6']

for ax, (titulo, valor), cor in zip(axes, kpis, colors):

    ax.set_facecolor('#F4F6F7')

    ax.text(
        0.5, 0.65, valor,
        fontsize=20,
        fontweight='bold',
        color=cor,
        ha='center',
        va='center'
    )

    ax.text(
        0.5, 0.30, titulo,
        fontsize=8,
        color='#555555',
        ha='center',
        va='center'
    )

    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(False)

plt.tight_layout()
plt.show()

#Readmissões - distribuição

distribuicao_readmissoes = (df[df["readmissao"] != "NO"].groupby("age").size())

distribuicao_readmissoes.plot(
    kind="bar",
    figsize=(10, 5),
    color= "purple"
)

plt.title("Distribuição das readmissões por faixa etária")
plt.xlabel("Faixa Etária")
plt.ylabel("Quantidade de readmissões")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

distribuicao_readmissoes = (df[df["readmissao"] != "NO"].groupby("readmissao").size())

distribuicao_readmissoes.plot(
    kind="bar",
    figsize=(10, 5),
    color= "gray"
)

plt.title("Distribuição das readmissões")
plt.xlabel("Tipo de readmissão")
plt.ylabel("Quantidade de readmissões")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

distribuicao_readmissoes = (df[df["readmissao"] != "NO"].groupby("hbA1c_resultado").size())

distribuicao_readmissoes.plot(
    kind="bar",
    figsize=(10, 5),
    color= "blue"
)

plt.title("Distribuição das readmissões por valor da HbA1c")
plt.xlabel("HbA1c")
plt.ylabel("Quantidade de readmissões")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

distribuicao_readmissoes = (df[df["readmissao"] != "NO"].groupby("number_inpatient").size())

distribuicao_readmissoes.plot(
    kind="bar",
    figsize=(10, 5),
    color= "black"
)

plt.title("Distribuição das readmissões por quantidade de internações anteriores")
plt.xlabel("Quantidade de internações anteriores")
plt.ylabel("Quantidade de readmissões")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()