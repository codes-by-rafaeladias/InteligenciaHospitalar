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
st.subheader("Histórico Hospitalar do Paciente")

# seleção de paciente

patients = queries.get_patients()

selected_patient = st.selectbox(
    "Selecione o paciente:",
    options=patients,
    index=None,
    placeholder="Escolha um paciente"
)

if selected_patient is not None:
    df_patient = queries.get_patient_history(selected_patient)
    
    df_patient = df_patient.rename(columns={
    "id_paciente": "ID do paciente",
    "raca": "Raça",
    "genero": "Sexo",
    "total_internacoes": "Total de internações",
    "media_permanencia": "Média de permanência (dias)",
    "total_emergencias": "Atendimentos de emergência",
    "total_ambulatoriais": "Atendimentos ambulatoriais"
    })
    
    df_styled = df_patient.style.format({
    "Média de permanência (dias)": "{:.2f}",
    "Total de internações": "{:,.0f}",
    "Atendimentos de emergência": "{:,.0f}",
    "Atendimentos ambulatoriais": "{:,.0f}"
    })
    
    df_styled = (
    df_patient.style
    .format({
    "Média de permanência (dias)": "{:.2f}",
    "Total de internações": "{:,.0f}",
    "Atendimentos de emergência": "{:,.0f}",
    "Atendimentos ambulatoriais": "{:,.0f}"
    })
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
    df_styled,
    width="stretch",
    hide_index=True
    )   