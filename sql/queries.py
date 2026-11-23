from database import engine
import pandas as pd

#1. Retorne a quantidade total de internações
def get_count_admissions():
    query = """
        SELECT COUNT(DISTINCT id_internacao) AS quantidade_internacoes
        FROM readmissoes_diabetes;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#2. Retorne a quantidade de pacientes únicos.
def get_count_patients():
    query = """
        SELECT COUNT(DISTINCT id_paciente) AS quantidade_pacientes
        FROM readmissoes_diabetes;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#3. Calcule o tempo médio de internação.
def get_average_time_hospital():
    query = """
        SELECT AVG(tempo_internacao) AS tempo_medio_hospital
        FROM readmissoes_diabetes;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#4. Identifique os cinco pacientes com maior quantidade de internações registradas.
def get_most_admissions_patients():
    query = """
        SELECT id_paciente, COUNT(id_paciente) AS quantidade_internacoes
        FROM readmissoes_diabetes
        GROUP BY id_paciente
        ORDER BY quantidade_internacoes DESC
        LIMIT 5;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#5. Conte a quantidade de registros por categoria de readmissão.
def get_count_readmissions_by_type():
    query = """
        SELECT readmissao AS tipo_readmissao, COUNT(readmissao) AS quantidade
        FROM readmissoes_diabetes
        WHERE readmissao != 'NO'
        GROUP BY tipo_readmissao
        ORDER BY quantidade DESC;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#6. Calcule a quantidade de internações por faixa etária.
def get_count_admissions_by_age_group():
    query = """
        SELECT age AS faixa_etaria, COUNT(age) AS quantidade_internacoes
        FROM readmissoes_diabetes
        WHERE readmissao != 'NO'
        GROUP BY faixa_etaria
        ORDER BY quantidade_internacoes DESC;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#7. Calcule a taxa de readmissão em até 30 dias por faixa etária.
def get_tax_readmissions_by_age_group():
    query = """
    WITH total_internacoes AS (
        SELECT age, COUNT(*) AS total
        FROM readmissoes_diabetes
        GROUP BY age
        ),
    readmissoes AS (
        SELECT age, COUNT(*) AS total_readmissoes
        FROM readmissoes_diabetes
        WHERE readmissao = '<30'
        GROUP BY age
        )
        SELECT t.age AS faixa_etaria, COALESCE(r.total_readmissoes, 0) AS total_readmissoes, t.total AS total_internacoes, 
        ROUND(COALESCE(r.total_readmissoes, 0) * 100.0 / t.total,2) AS taxa_readmissao
        FROM total_internacoes t
        LEFT JOIN readmissoes r ON t.age = r.age
        ORDER BY taxa_readmissao DESC;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#8. Calcule a média de dias de internação por gênero.
def get_average_time_hospital_by_gender():
    query = """
        SELECT genero, AVG(tempo_internacao) AS tempo_medio_internacao
        FROM readmissoes_diabetes
        GROUP BY genero
        ORDER BY tempo_medio_internacao DESC;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#9. Identifique os tipos de internação mais frequentes.
def get_most_frequent_admissions_type():
    query = """
        SELECT tipo_internacao, COUNT(*) AS quantidade_internacoes
        FROM readmissoes_diabetes
        GROUP BY tipo_internacao
        ORDER BY quantidade_internacoes DESC;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#10. Calcule a quantidade média de exames laboratoriais por categoria de readmissão.
def get_average_lab_procedures_by_readmission():
    query = """
        SELECT readmissao AS tipo_readmissao, AVG(qtd_exames_laboratoriais) AS qtd_media_exames_laboratoriais
        FROM readmissoes_diabetes
        WHERE readmissao != 'NO'
        GROUP BY tipo_readmissao
        ORDER BY qtd_media_exames_laboratoriais DESC;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#11. Identifique os pacientes que tiveram mais de três internações registradas.
def get_patients_with_more_3_admissions():
    query = """
        WITH frequencia_internacoes AS(
            SELECT id_paciente, COUNT(*) AS quantidade_internacoes
            FROM readmissoes_diabetes
            GROUP BY id_paciente
        )
        SELECT *
        FROM frequencia_internacoes
        WHERE quantidade_internacoes > 3;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#12. Identifique as categorias de internação com taxa de readmissão acima da taxa geral.
def get_admissions_type_with_bigger_tax():
    query = """
    WITH taxa_por_categoria AS (
        SELECT
            tipo_internacao,
            COUNT(*) AS total_internacoes,
            COUNT(*) FILTER (
                WHERE readmissao != 'NO'
            ) AS total_readmissoes,
            ROUND(
                COUNT(*) FILTER (WHERE readmissao != 'NO') * 100.0
                / COUNT(*),
                2
            ) AS taxa_readmissao
        FROM readmissoes_diabetes
        GROUP BY tipo_internacao
    ),

    taxa_geral AS (
        SELECT
            ROUND(
                COUNT(*) FILTER (WHERE readmissao != 'NO') * 100.0
                / COUNT(*),
                2
            ) AS taxa_geral
        FROM readmissoes_diabetes
    )

    SELECT
        c.tipo_internacao,
        c.total_internacoes,
        c.total_readmissoes,
        c.taxa_readmissao,
        g.taxa_geral
    FROM taxa_por_categoria c
    CROSS JOIN taxa_geral g
    WHERE c.taxa_readmissao > g.taxa_geral
    ORDER BY c.taxa_readmissao DESC;
    """

    df = pd.read_sql(query, con=engine)

    return df

#13. Utilize uma subconsulta para identificar as faixas etárias cuja taxa de readmissão é superior à taxa geral.
def get_age_group_with_bigger_tax():
    query="""
    SELECT faixa_etaria, taxa_readmissao
    FROM (
    SELECT
        age AS faixa_etaria,
        ROUND(
            COUNT(*) FILTER (WHERE readmissao != 'NO') * 100.0
            / COUNT(*),
            2
        ) AS taxa_readmissao
    FROM readmissoes_diabetes
    GROUP BY age) AS taxas_por_faixa
    WHERE taxa_readmissao > (
    SELECT
        ROUND(
            COUNT(*) FILTER (WHERE readmissao != 'NO') * 100.0
            / COUNT(*),
            2
        )
    FROM readmissoes_diabetes)
    ORDER BY taxa_readmissao DESC;
    """
    
    df = pd.read_sql(query, con=engine)

    return df

#14. Utilize CASE WHEN para classificar os atendimentos conforme o tempo de permanência.
def get_time_hospital_by_patient():
    query="""
    SELECT id_paciente, tempo_internacao,
    CASE 
        WHEN tempo_internacao <= 3 THEN 'Curta permanência'
        WHEN tempo_internacao BETWEEN 4 AND 7 THEN 'Média permanência'
        WHEN tempo_internacao > 7 THEN 'Longa permanência'
    END AS classificacao_tempo_permanencia
    FROM readmissoes_diabetes;
        """
    
    df = pd.read_sql(query, con=engine)

    return df

#15. Histórico dos pacientes
def get_historical_patient():
    query="""
    SELECT id_paciente,
    COUNT(*) AS total_internacoes,
    AVG(tempo_internacao) AS media_permanencia,
    MAX(number_emergency) AS total_emergencias,
    MAX(number_outpatient) AS total_ambulatoriais
    FROM readmissoes_diabetes
    GROUP BY id_paciente
    ORDER BY total_internacoes DESC
    LIMIT 20;
    """
    
    df = pd.read_sql(query, con=engine)

    return df
    
if __name__ == "__main__":
    print(get_count_admissions())
    print(get_count_patients())
    print(get_average_time_hospital())
    print(get_most_admissions_patients())
    print(get_count_readmissions_by_type())
    print(get_count_admissions_by_age_group())
    print(get_tax_readmissions_by_age_group())
    print(get_average_time_hospital_by_gender())
    print(get_most_frequent_admissions_type())
    print(get_average_lab_procedures_by_readmission())
    print(get_patients_with_more_3_admissions())
    print(get_admissions_type_with_bigger_tax())
    print(get_age_group_with_bigger_tax())
    print(get_time_hospital_by_patient())
    print()
    print(get_historical_patient())