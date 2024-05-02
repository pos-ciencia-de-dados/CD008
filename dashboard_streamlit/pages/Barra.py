import streamlit as st
import pandas as pd
import altair as alt
from menu_tarefa03 import menu_barra

# Initialize st.session_state.uf to None
if "uf" not in st.session_state:
    st.session_state.uf = None

st.title("Gráfico em Barra")

dataset = st.session_state.dataset

# Remove registros com valores NULO
nordesteDS = dataset.dropna()

# Mantém apenas os registros onde o valor da colunas 'SITUACAO_CURSO' é 'Em atividade'
nordesteDS = nordesteDS[nordesteDS['SITUACAO_CURSO'] == 'Em atividade']

# Mantem apenas da região Nordeste
nordesteDS = nordesteDS[nordesteDS['REGIAO'] == 'NORDESTE']

# Mantem apenas cursos de Bacharelado
nordesteDS = nordesteDS[nordesteDS['GRAU'] == 'Bacharelado']

nordesteDS = nordesteDS[nordesteDS['MODALIDADE'] == 'Educação Presencial']


tab01, tab02 = st.tabs(["CATEGORIA ADMINISTRATIVA", "Instituições de Ensino Superior"])


with tab01:
    st.markdown(f"Total de vagas autorizadas por `CATEGORIA_ADMINISTRATIVA` na região Nordeste.")
    c01 = alt.Chart(nordesteDS).mark_bar().encode(
        alt.Y('sum(QT_VAGAS_AUTORIZADAS)'),
        alt.X('CATEGORIA_ADMINISTRATIVA'),
        color='ORGANIZACAO_ACADEMICA',
        tooltip=['NOME_IES', 'NOME_CURSO', 'QT_VAGAS_AUTORIZADAS']
    ).interactive()
    st.altair_chart(c01, use_container_width=True)

with tab02:
    st.markdown(f"Quantidade de Instituições de Ensino Superior por UF (Em todo o Brasil).")

    iesDF = dataset[dataset['SITUACAO_CURSO'] == 'Em atividade']
    iesDF = iesDF[iesDF['UF'] != 'ZZ']

    # Instituições por UF
    df_uf_univ = iesDF.groupby('UF')['CODIGO_IES'].nunique().reset_index(name='quantidade').sort_values(by='quantidade', ascending=False)

    c02 = alt.Chart(df_uf_univ).mark_bar().encode(
        x=alt.X('UF:N', sort='-y'),
        y='quantidade:Q'
    )
    st.altair_chart(c02, use_container_width=True)


menu_barra() # Render the dynamic menu!

