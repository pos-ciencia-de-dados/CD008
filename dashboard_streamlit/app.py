import streamlit as st
import altair as alt
import pandas as pd
from menu import menu_inicio
import wget
from zipfile import ZipFile # importing the zipfile module 

st.set_page_config(layout="wide")

title = st.title("Baixando dataset...")

try:
    with open("PDA_Dados_Cursos_Graduacao_Brasil.zip", 'r') as f:
        pass
except FileNotFoundError:    
    link = "https://github.com/pos-ciencia-de-dados/CD008/raw/principal/dataset/PDA_Dados_Cursos_Graduacao_Brasil.zip"
    wget.download(link, "PDA_Dados_Cursos_Graduacao_Brasil.zip")
    
    # loading the .zip and creating a zip object 
    with ZipFile("PDA_Dados_Cursos_Graduacao_Brasil.zip", 'r') as zObject: 
        # Extracting all the members of the zip 
        # into a specific location. 
        zObject.extractall(path=".") 

if "dataset" not in st.session_state:
    title.title("Baixando dataset... COMPLETO!")
    with st.spinner('Carregando dataset...'):
        st.session_state.dataset = pd.read_csv("PDA_Dados_Cursos_Graduacao_Brasil.csv")
        st.session_state.dataset = st.session_state.dataset[st.session_state.dataset['UF'] != 'ZZ']
    
title.title("Distribuição de Cursos de Graduação no Brasil")

st.write("Todos os cursos de graduação no Brasil, com informações sobre a modalidade de ensino, categoria administrativa das instituições, e a distribuição geográfica dos cursos.")

"---"

col1, col2, col3, col4 = st.columns([1, 1, 1, 2])

with col1:
    st.metric("Total de Registros", '{0:,}'.format(st.session_state.dataset.shape[0]).replace(',', '.'))

with col2:
    st.metric("Total de IES", '{0:,}'.format(st.session_state.dataset['CODIGO_IES'].nunique()).replace(',', '.'))

with col3:
    st.metric("Total de Cursos", '{0:,}'.format(st.session_state.dataset['CODIGO_CURSO'].nunique()).replace(',', '.'))
    
with col4:
    listaCursos = st.session_state.dataset.drop(columns=['CODIGO_MUNICIPIO', 'MUNICIPIO', 'UF', 'REGIAO']).drop_duplicates()
    st.metric("Total de Vagas Autorizadas", '{0:,}'.format(listaCursos['QT_VAGAS_AUTORIZADAS'].sum()).replace(',', '.'))

"---"

st.markdown("### Cursos agrupados por:")

col21, col22 = st.columns([1, 1])

with col21:
    catAdm = st.session_state.dataset.groupby(['CATEGORIA_ADMINISTRATIVA'])['CODIGO_CURSO'].nunique().reset_index(name='QTD_CURSOS')
    c1 = alt.Chart(catAdm).mark_arc().encode(
        theta="QTD_CURSOS:Q",
        color="CATEGORIA_ADMINISTRATIVA:N"
    ).properties(width=230, height=230, title="Categoria Administrativa").configure_legend(disable=True)
    st.altair_chart(c1)

    orgAcad = st.session_state.dataset.groupby(['ORGANIZACAO_ACADEMICA'])['CODIGO_CURSO'].nunique().reset_index(name='QTD_CURSOS')
    c2 = alt.Chart(orgAcad).mark_arc().encode(
        theta="QTD_CURSOS:Q",
        color="ORGANIZACAO_ACADEMICA:N"
    ).properties(width=230, height=230, title="Organização Acadêmica").configure_legend(disable=True)
    st.altair_chart(c2)

    grau = st.session_state.dataset.groupby(['GRAU'])['CODIGO_CURSO'].nunique().reset_index(name='QTD_CURSOS')
    c3 = alt.Chart(grau).mark_arc().encode(
        theta="QTD_CURSOS:Q",
        color="GRAU:N"
    ).properties(width=230, height=230, title="Grau").configure_legend(disable=True)
    st.altair_chart(c3)

with col22:
    areaOcde = st.session_state.dataset.groupby(['AREA_OCDE'])['CODIGO_CURSO'].nunique().reset_index(name='QTD_CURSOS')
    c4 = alt.Chart(areaOcde).mark_arc().encode(
        theta="QTD_CURSOS:Q",
        color="AREA_OCDE:N"
    ).properties(width=230, height=230, title="Área (OCDE)").configure_legend(disable=True)
    st.altair_chart(c4)

    #MODALIDADE
    modalidade = st.session_state.dataset.groupby(['MODALIDADE'])['CODIGO_CURSO'].nunique().reset_index(name='QTD_CURSOS')
    c5 = alt.Chart(modalidade).mark_arc().encode(
        theta="QTD_CURSOS:Q",
        color="MODALIDADE:N"
    ).properties(width=230, height=230, title="Modalidade").configure_legend(disable=True)
    st.altair_chart(c5)

    #SITUACAO_CURSO
    situacao = st.session_state.dataset.groupby(['SITUACAO_CURSO'])['CODIGO_CURSO'].nunique().reset_index(name='QTD_CURSOS')
    c6 = alt.Chart(situacao).mark_arc().encode(
        theta="QTD_CURSOS:Q",
        color="SITUACAO_CURSO:N"
    ).properties(width=230, height=230, title="Situação").configure_legend(disable=True)
    st.altair_chart(c6)

menu_inicio() # Render the dynamic menu!