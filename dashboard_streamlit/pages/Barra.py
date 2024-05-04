import streamlit as st
import pandas as pd
import altair as alt
from menu import menu_barra

# Initialize st.session_state.regiao to NORDESTE
if "regiao" not in st.session_state:
    st.session_state.regiao = "NORDESTE"

st.title(f"Gráfico em Barra (Região {st.session_state.regiao})")

dataset = st.session_state.dataset

# Mantém apenas os registros onde o valor da colunas 'SITUACAO_CURSO' é 'Em atividade'
emAtividadeDS = dataset[dataset['SITUACAO_CURSO'] == 'Em atividade']

# Mantem apenas cursos de Bacharelado
bachareladoDS = emAtividadeDS[emAtividadeDS['GRAU'] == 'Bacharelado']

presencialDS = bachareladoDS[bachareladoDS['MODALIDADE'] == 'Educação Presencial']

tab01, tab02, tab03, tab04, tab05 = st.tabs(["Categorias Administrativas", "Instituições de Ensino Superior", "Top 10 Municípios", "Top 10 Cursos", "Top 10 Cursos (Por UF)"])


with tab01:
    st.markdown(f"Total de vagas autorizadas por `CATEGORIA_ADMINISTRATIVA` (Na Região {st.session_state.regiao}).")

    regiaoDS = presencialDS[presencialDS['REGIAO'] == st.session_state.regiao]

    c01 = alt.Chart(regiaoDS).mark_bar().encode(
        alt.Y('sum(QT_VAGAS_AUTORIZADAS)'),
        alt.X('CATEGORIA_ADMINISTRATIVA'),
        color='ORGANIZACAO_ACADEMICA',
        tooltip=['NOME_IES', 'NOME_CURSO', 'QT_VAGAS_AUTORIZADAS']
    ).interactive()
    st.altair_chart(c01, use_container_width=True)

with tab02:
    st.markdown(f"Quantidade de Instituições de Ensino Superior por UF (Na Região {st.session_state.regiao}).")

    iesDS = emAtividadeDS[emAtividadeDS['UF'] != 'ZZ']

    # Instituições por REGIAO e UF
    iesDS = iesDS.groupby(['REGIAO', 'UF'])['CODIGO_IES'].nunique().reset_index(name='quantidade').sort_values(by='quantidade', ascending=False)

    regiaoDS = iesDS[iesDS['REGIAO'] == st.session_state.regiao]

    c02 = alt.Chart(regiaoDS).mark_bar().encode(
        x=alt.X('UF:N', sort='-y'),
        y='quantidade:Q'
    )
    st.altair_chart(c02, use_container_width=True)


with tab03:
    st.markdown(f"Top 10 Municípios com mais instituições de ensino superior (Na Região {st.session_state.regiao}).")

    muniDS = presencialDS.groupby(['REGIAO', 'MUNICIPIO'])['CODIGO_IES'].nunique().reset_index(name='quantidade').sort_values(by='quantidade', ascending=False)

    regiaoDS = muniDS[muniDS['REGIAO'] == st.session_state.regiao]

    # Top 10 Municípios com mais instituições de ensino superior
    top10DF = regiaoDS.head(10)

    c03 = alt.Chart(top10DF).mark_bar().encode(
        x=alt.X('MUNICIPIO:N', sort='-y'),
        y='quantidade:Q'
    )
    st.altair_chart(c03, use_container_width=True)


with tab04:
    st.markdown(f"Top 10 cursos com mais vagas autorizadas (Na Região {st.session_state.regiao}).")

    cursoDS = presencialDS.groupby(['REGIAO', 'AREA_OCDE'])['QT_VAGAS_AUTORIZADAS'].sum().reset_index(name='quantidade').sort_values(by='quantidade', ascending=False)

    regiaoDS = cursoDS[cursoDS['REGIAO'] == st.session_state.regiao]

    # Top 10 cursos com mais vagas
    top10CursoDS = regiaoDS.head(10)

    c04 = alt.Chart(top10CursoDS).mark_bar().encode(
        x=alt.X('AREA_OCDE:N', sort='-y', title='Curso'),
        y='quantidade:Q'
    )
    st.altair_chart(c04, use_container_width=True)

with tab05:
    st.markdown(f"Top 10 cursos com mais vagas autorizadas por UF (Na Região {st.session_state.regiao}).")

    regiaoDS = presencialDS[presencialDS['REGIAO'] == st.session_state.regiao]

    df_uf_vagas = regiaoDS.groupby(['UF', 'AREA_OCDE'])['QT_VAGAS_AUTORIZADAS'].sum().reset_index(name='quantidade').sort_values(by='quantidade', ascending=False)

    def get_top_10_cursos(uf_data):
        return uf_data.nlargest(10, 'quantidade')

    top_cursos = df_uf_vagas.groupby('UF').apply(get_top_10_cursos).reset_index(drop=True)

    # Top 10 Cursos com mais vagas por UF em uma dada região
    c05 = alt.Chart(top_cursos).mark_bar().encode(
        x=alt.X('UF:N', title='UF'),
        y=alt.Y('quantidade:Q', title='Quantidade de Vagas'),
        color='AREA_OCDE:N',
        tooltip=['AREA_OCDE', 'quantidade']
    ).properties(
        width=600,
        height=400
    ).configure_axis(
        labelAngle=0
    )
    st.altair_chart(c05, use_container_width=True)
    
menu_barra() # Render the dynamic menu!

