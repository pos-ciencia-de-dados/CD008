import streamlit as st
import pandas as pd
import altair as alt
from menu import menu_barra

# Initialize st.session_state.regiao to NORDESTE
if "regiao" not in st.session_state:
    st.session_state.regiao = "NORDESTE"

st.title(f"Gráfico de Linha (Região {st.session_state.regiao})")

dataset = st.session_state.dataset

# Mantém apenas os registros onde o valor da colunas 'SITUACAO_CURSO' é 'Em atividade'
emAtividadeDS = dataset[dataset['SITUACAO_CURSO'] == 'Em atividade']

# Mantem apenas cursos de Bacharelado
bachareladoDS = emAtividadeDS[emAtividadeDS['GRAU'] == 'Bacharelado']

presencialDS = bachareladoDS[bachareladoDS['MODALIDADE'] == 'Educação Presencial']

st.markdown(f"Quantidade de cursos presenciais em atividade por UF (Na Região {st.session_state.regiao}).")

regiaoDS = presencialDS[presencialDS['REGIAO'] == st.session_state.regiao]

line = alt.Chart(regiaoDS).mark_line().encode(
    alt.X('UF:N'),
    alt.Y('count(NOME_CURSO)')
)

point = alt.Chart(regiaoDS).mark_circle().encode(
    alt.X('UF:N'),
    alt.Y('count(NOME_CURSO)')
)

c01 = line + point

st.altair_chart(c01, use_container_width=True)
    
menu_barra() # Render the dynamic menu!

