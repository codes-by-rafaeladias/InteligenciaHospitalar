from database import engine
import pandas as pd

#------- MÉTRICAS ------

# quantidade total de internações
def get_count_admissions():
    query = """
        SELECT COUNT(DISTINCT id_internacao) AS quantidade_internacoes
        FROM readmissoes_diabetes;
    """
    
    df = pd.read_sql(query, con=engine)

    return df["quantidade_internacoes"].iloc[0]

# quantidade de pacientes únicos.
def get_count_patients():
    query = """
        SELECT COUNT(DISTINCT id_paciente) AS quantidade_pacientes
        FROM readmissoes_diabetes;
    """
    
    df = pd.read_sql(query, con=engine)

    return df["quantidade_pacientes"].iloc[0]

# tempo medio de internacao
def get_average_time_hospital():
    query = """
        SELECT ROUND(AVG(tempo_internacao), 2) AS tempo_medio_hospital
        FROM readmissoes_diabetes;
    """
    
    df = pd.read_sql(query, con=engine)

    return df["tempo_medio_hospital"].iloc[0]

# taxa de readmissão
def get_overall_readmission_tax():
    query = """
        SELECT ROUND(
        COUNT(*) FILTER (WHERE readmissao != 'NO') * 100.0
        / COUNT(*), 2) AS taxa_readmissao
        FROM readmissoes_diabetes
    """
    
    df = pd.read_sql(query, con=engine)

    return df["taxa_readmissao"].iloc[0]

#taxa de readmissão em até 30 dias
def get_less_30_readmission_tax():
    query = """
        SELECT ROUND(
        COUNT(*) FILTER (WHERE readmissao = '<30') * 100.0
        / COUNT(*), 2) AS taxa_readmissao
        FROM readmissoes_diabetes
    """
    
    df = pd.read_sql(query, con=engine)

    return df["taxa_readmissao"].iloc[0]

#taxa de readmissão após 30 dias
def get_more_30_readmission_tax():
    query = """
        SELECT ROUND(
        COUNT(*) FILTER (WHERE readmissao = '>30') * 100.0
        / COUNT(*), 2) AS taxa_readmissao
        FROM readmissoes_diabetes
    """
    
    df = pd.read_sql(query, con=engine)

    return df["taxa_readmissao"].iloc[0]

# ----- GRÁFICOS -------
#Admissões por faixa etária
def get_count_admissions_by_age_group():
    query = """
        SELECT age AS faixa_etaria, COUNT(*) AS quantidade_internacoes
        FROM readmissoes_diabetes
        GROUP BY faixa_etaria
        ORDER BY faixa_etaria ASC;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#Admissões por sexo
def get_count_admissions_by_gender():
    query = """
        SELECT
        TRIM(genero) AS sexo,
        COUNT(*) AS quantidade_internacoes
        FROM readmissoes_diabetes
        WHERE genero IS NOT NULL
        AND TRIM(genero) != ''
        AND genero != 'Unknown/Invalid'
        GROUP BY TRIM(genero)
        ORDER BY sexo ASC;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#Admissões por raça/etnia
def get_count_admissions_by_race():
    query = """
        SELECT raca, COUNT(*) AS quantidade_internacoes
        FROM readmissoes_diabetes
        WHERE raca != '?'
        GROUP BY raca
        ORDER BY raca ASC;
    """
    
    df = pd.read_sql(query, con=engine)

    return df
    
#Admissões por categoria
def get_count_admissions_by_category():
    query = """
        SELECT tipo_internacao, COUNT(*) AS quantidade_internacoes
        FROM readmissoes_diabetes
        GROUP BY tipo_internacao
        ORDER BY quantidade_internacoes DESC;
    """
    
    df = pd.read_sql(query, con=engine)
    
    df = df.rename(columns={"tipo_internacao": "Categoria", "quantidade_internacoes": "Quantidade"})
    
    df["Categoria"] = df["Categoria"].replace({
    "Emergency": "Emergência",
    "Elective": "Eletiva",
    "Urgent": "Urgente",
    "Not specified": "Não especificado",
    "Not Available": "Não disponível",
    "Not Mapped": "Não mapeado",
    "Trauma Center": "Centro de Trauma",
    "Newborn": "Recém-nascido"
    })

    return df

#Distribuição do tempo de permanência
def get_time_in_hospital_distribution():
    query = """
        SELECT tempo_internacao
        FROM readmissoes_diabetes;
    """

    df = pd.read_sql(query, con=engine)

    return df

# Distribuição das taxas de readmissão
def get_readmission_taxes():
    query = """
        SELECT
        readmissao,
        ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM readmissoes_diabetes),
        2
        ) AS taxa_readmissao
    FROM readmissoes_diabetes
    GROUP BY readmissao
    ORDER BY taxa_readmissao DESC;
    """

    df = pd.read_sql(query, con=engine)

    return df

# taxa de readmissões por faixa etária
def get_readmissions_by_age_group():
    query = """
    SELECT
    age AS faixa_etaria,
    ROUND(
        SUM(CASE WHEN readmissao IN ('<30', '>30') THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
        ) AS taxa_readmissao
    FROM readmissoes_diabetes
    GROUP BY faixa_etaria
    ORDER BY faixa_etaria ASC;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#taxa de readmissão por sexo
def get_readmissions_by_gender():
    query="""
    SELECT
    genero,
    ROUND(
        SUM(CASE WHEN readmissao IN ('<30', '>30') THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS taxa_readmissao
    FROM readmissoes_diabetes
    WHERE genero IN ('Male', 'Female')
    GROUP BY genero;
    """
    
    df = pd.read_sql(query, con=engine)

    return df
    
# taxa de readmissão por raça
def get_readmissions_by_race():
    query="""
        SELECT
        raca,
        ROUND(
            SUM(CASE WHEN readmissao IN ('<30', '>30') THEN 1 ELSE 0 END)
            * 100.0 / COUNT(*),
            2
        ) AS taxa_readmissao
        FROM readmissoes_diabetes
        WHERE raca IS NOT NULL
            AND TRIM(raca) != '' AND raca != '?'
        GROUP BY raca
        ORDER BY taxa_readmissao DESC;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

# Todos os pacientes únicos
def get_patients():
    query="""
        SELECT DISTINCT id_paciente
        FROM readmissoes_diabetes
        ORDER BY id_paciente ASC
    """
    
    df = pd.read_sql(query, con=engine)

    return df["id_paciente"].tolist()

# histórico de um paciente
def get_patient_history(patient_id):
    query = """
        SELECT id_paciente,
        COUNT(*) AS total_internacoes,
        AVG(tempo_internacao) AS media_permanencia,
        MAX(number_emergency) AS total_emergencias,
        MAX(number_outpatient) AS total_ambulatoriais
        FROM readmissoes_diabetes
        WHERE id_paciente = %s
        GROUP BY id_paciente
        ORDER BY id_paciente;
    """
    
    return pd.read_sql(query, con=engine, params=(patient_id,))