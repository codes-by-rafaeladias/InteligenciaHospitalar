import queries
import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("""
<style>
h1 {
    text-align: center;
}

h3 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)
st.title("INTELIGÊNCIA HOSPITALAR")
st.subheader("Análise de Readmissões Hospitalares")

# métricas
overall_readmission_tax = queries.get_overall_readmission_tax()
less_30_readmission_tax = queries.get_less_30_readmission_tax()
more_30_readmission_tax = queries.get_more_30_readmission_tax()

st.markdown("""
<style>

/* Cartões */
[data-testid="stMetric"] {
    background-color: #213B4F;
    border: 1px solid #4B7892;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}

/* Títulos dos indicadores */
[data-testid="stMetricLabel"] {
    display: flex;
    justify-content: center;
    width: 100%;
    text-align: center;
    color: #DCE7EF !important;
    font-size: 15px;
    font-weight: 600;
}

[data-testid="stMetricLabel"] > div {
    width: 100%;
    justify-content: center;
    text-align: center;
}

[data-testid="stMetricLabel"] p {
    width: 100%;
    text-align: center;
}

/* Valores dos indicadores */
[data-testid="stMetricValue"] {
    justify-content: center;
    color: #42B8A5 !important;
    font-size: 28px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Taxa Geral de Readmissão", overall_readmission_tax)

with col2:
    st.metric("Taxa de Readmissão em até 30 dias", less_30_readmission_tax)

with col3:
    st.metric("Taxa de Readmissão após 30 dias", more_30_readmission_tax)
    
# gráficos 
col1, col2 = st.columns(2)

with col1:
    df_readmission = queries.get_readmission_taxes()

    fig = px.pie(
        df_readmission,
        names="readmissao",
        values="taxa_readmissao",
        title="Distribuição das Readmissões por categorias",
        color_discrete_sequence=["#42B8A5", "#E87532", "#B8322A"]
    )

    fig.update_layout(
        template="plotly_dark",
        title={
            "text": "Distribuição das Readmissões por categorias",
            "x": 0.1
        },
        paper_bgcolor="#172B3A",
        plot_bgcolor="#213B4F",
        font_color="#F1F5F9"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="label+percent",
        hole=0.4
    )

    st.plotly_chart(fig, width="stretch")
    
with col2:
    df_age = queries.get_readmissions_by_age_group()
    
    fig = px.bar(
        df_age,
        x="faixa_etaria",
        y="taxa_readmissao",
        title="Taxa de readmissão por faixa etária",
        labels={
        "faixa_etaria": "Faixa etária",
        "taxa_readmissao": "Taxa de readmissão"
        }
    )
    
    fig.update_layout(title_x=0.2)

    st.plotly_chart(fig, width='stretch')
    
col3, col4 = st.columns(2)

with col3:
    df_gender = queries.get_readmissions_by_gender()
    
    fig = px.bar(
        df_gender,
        x="genero",
        y="taxa_readmissao",
        title="Taxa de readmissão por sexo",
        labels={
        "genero": "Sexo",
        "taxa_readmissao": "Taxa de readmissão"
        }
    )
    
    fig.update_xaxes(
    ticktext=["Masculino", "Feminino"],
    tickvals=["Male", "Female"])
    
    fig.update_layout(title_x=0.3)

    st.plotly_chart(fig, width='stretch')

with col4:
    df_race = queries.get_readmissions_by_race()
    
    fig = px.bar(
        df_race,
        x="raca",
        y="taxa_readmissao",
        title="Taxa de readmissão por raça",
        labels={
        "raca": "Raça",
        "taxa_readmissao": "Taxa de readmissão"
        }
    )
    
    fig.update_xaxes(
    ticktext=["Afro-americano", "Asiático", "Branco", "Hispânico", "Outros"],
    tickvals=["AfricanAmerican", "Asian", "Caucasian", "Hispanic", "Other"])
    
    fig.update_layout(title_x=0.3)

    st.plotly_chart(fig, width='stretch')