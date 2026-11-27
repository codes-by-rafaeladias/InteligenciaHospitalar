import queries
import streamlit as st
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
st.subheader("Análise de Admissões Hospitalares")

# métricas
count_admissions = queries.get_count_admissions()
count_patients = queries.get_count_patients()
average_time = f"{queries.get_average_time_hospital()} dias"

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

col1, col2 = st.columns(2)

with col1:
    st.metric("Internações", count_admissions, border=True)

with col2:
    st.metric("Hospitais", 130, border=True)
    
col3, col4 = st.columns(2)

with col3:
    st.metric("Pacientes", count_patients, border=True)

with col4:
    st.metric("Tempo médio de internação", average_time, border=True)

#graficos de barra
col1, col2 = st.columns(2)

with col1:
    df_age = queries.get_count_admissions_by_age_group()
    
    fig = px.bar(
        df_age,
        x="faixa_etaria",
        y="quantidade_internacoes",
        title="Admissões por faixa etária",
        labels={
        "faixa_etaria": "Faixa etária",
        "quantidade_internacoes": "Internações"
        }
    )
    
    fig.update_layout(title_x=0.25)

    st.plotly_chart(fig, width='stretch')
    
    
with col2:
    df_gender = queries.get_count_admissions_by_gender()
    
    fig = px.bar(
        df_gender,
        x="sexo",
        y="quantidade_internacoes",
        title="Admissões por sexo",
        labels={
        "sexo": "Sexo",
        "quantidade_internacoes": "Internações"
        }
    )
    
    fig.update_xaxes(
    ticktext=["Masculino", "Feminino"],
    tickvals=["Male", "Female"])
    
    fig.update_layout(title_x=0.35)

    st.plotly_chart(fig, width='stretch')

#grafico de barra + tabela
col1, col2 = st.columns(2)

with col1:
    df_race = queries.get_count_admissions_by_race()
    
    fig = px.bar(
        df_race,
        x="raca",
        y="quantidade_internacoes",
        title="Admissões por raça",
        labels={
        "raca": "Raça",
        "quantidade_internacoes": "Internações"
        }
    )
    
    fig.update_xaxes(
    ticktext=["Afro-americano", "Asiático", "Branco", "Hispânico", "Outros"],
    tickvals=["AfricanAmerican", "Asian", "Caucasian", "Hispanic", "Other"])
    
    fig.update_layout(title_x=0.25)

    st.plotly_chart(fig, width='stretch')

with col2:
    df_admissions = queries.get_count_admissions_by_category()
    
    st.markdown(
    "<p style='text-align: center; font-size:16px; font-weight:600; color:#F1F5F9;'>Categorias de internação mais frequentes</p>",
    unsafe_allow_html=True)
    
    df_estilizado = (
    df_admissions.style
    .set_properties(**{
        "background-color": "#213B4F",
        "color": "#FFFFFF",
        "text-align": "center",
        "padding": "12px",
        "border": "1px solid #4B7892"
    })
    .set_table_styles([
        {
            "selector": "th",
            "props": [
                ("background-color", "#172B3A"),
                ("color", "#42B8A5"),
                ("font-weight", "bold"),
                ("text-align", "center"),
                ("padding", "14px"),
                ("border", "1px solid #4B7892")
            ]
        },
        {
            "selector": "td",
            "props": [
                ("padding", "12px")
            ]
        }
    ])
)

    st.dataframe(
        df_estilizado,
        width='stretch',
        hide_index=True
    )
    
#histograma

df_time_hospital = queries.get_time_in_hospital_distribution()

fig = px.histogram(
    df_time_hospital,
    x="tempo_internacao",
    title="Distribuição do tempo de internação",
    labels={
        "tempo_internacao": "Dias de internação",
        "count": "Quantidade de internações"
    },
    opacity=0.9
)

fig.update_traces(
    marker_line_color="#172B3A",
    marker_line_width=1
)

fig.update_layout(
    template="plotly_dark",
    title={
        "text": "Distribuição do tempo de internação",
        "x": 0.35,
        "font": {
            "size": 18,
            "color": "#F1F5F9"
        }
    },
    xaxis_title="Dias de internação",
    yaxis_title="Quantidade de internações",
    font_color="#DCE7EF",
    bargap=0.15,
    paper_bgcolor="#172B3A",
    plot_bgcolor="#213B4F",
    margin=dict(l=20, r=20, t=60, b=20)
)

fig.update_xaxes(
    dtick=1,
    showgrid=False
)

fig.update_yaxes(
    gridcolor="#4B7892",
    zeroline=False
)

st.plotly_chart(fig, width="stretch")