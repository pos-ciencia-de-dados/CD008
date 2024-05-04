import streamlit as st
import pandas as pd
import altair as alt
from menu import menu_barra

# Initialize st.session_state.regiao to NORDESTE
if "regiao" not in st.session_state:
    st.session_state.regiao = "NORDESTE"

st.title(f"Gráfico de Pizza (Região {st.session_state.regiao})")

dataset = st.session_state.dataset

# Mantém apenas os registros onde o valor da colunas 'SITUACAO_CURSO' é 'Em atividade'
emAtividadeDS = dataset[dataset['SITUACAO_CURSO'] == 'Em atividade']

# Mantem apenas cursos de Bacharelado
bachareladoDS = emAtividadeDS[emAtividadeDS['GRAU'] == 'Bacharelado']

presencialDS = bachareladoDS[bachareladoDS['MODALIDADE'] == 'Educação Presencial']

st.markdown(f"Quantidade de vagas autorizadas em cursos presenciais por UF (Na Região {st.session_state.regiao}).")

regiaoDS = presencialDS[presencialDS['REGIAO'] == st.session_state.regiao]

c01 = alt.Chart(regiaoDS).mark_arc().encode(
    theta="sum(QT_VAGAS_AUTORIZADAS)",
    color="UF:N"
)

st.altair_chart(c01, use_container_width=True)
    
menu_barra() # Render the dynamic menu!

