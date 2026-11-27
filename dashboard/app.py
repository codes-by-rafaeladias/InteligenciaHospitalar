import streamlit as st

# configuração das páginas do dashboard

st.set_page_config(
    page_title="Admissões Hospitalares",
    layout="wide"
)

admissoes = st.Page("pages/Admissoes.py", title="Admissões Hospitalares")
readmissoes = st.Page("pages/Readmissoes.py", title="Readmissões Hospitalares")
historico_paciente = st.Page("pages/Historico_Paciente.py", title="Histórico do Paciente")

pg = st.navigation([
    admissoes,
    readmissoes,
    historico_paciente
])

pg.run()