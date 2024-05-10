import streamlit as st
import pandas as pd
import altair as alt
from menu import menu_barra
from pages.Mapa import mostrar_mapa
from pages.MapaMunicipios import mostrar_mapa_municipios

if "regiao" not in st.session_state:
    st.session_state.regiao = "TODAS"

if "ativo" not in st.session_state:
    st.session_state.ativo = False

if "modalidade" not in st.session_state:
    st.session_state.modalidade = "Ambas"

if "grau" not in st.session_state:
    st.session_state.grau = []

st.title(f"Instituições de Ensino Superior ({st.session_state.regiao})")

if st.session_state.regiao == "TODAS":
    regiaoDF = st.session_state.dataset
else:
    regiaoDF = st.session_state.dataset[st.session_state.dataset['REGIAO'] == st.session_state.regiao]

if st.session_state.ativo == True:
    regiaoDF = regiaoDF[regiaoDF['SITUACAO_CURSO'] == 'Em atividade']

if len(st.session_state.grau) > 0:
    regiaoDF = regiaoDF.query('GRAU in ' + str(st.session_state.grau))
    
if st.session_state.modalidade != "Ambas":
    regiaoDF = regiaoDF[regiaoDF['MODALIDADE'] == st.session_state.modalidade]

tabUF, tabCat, tabMuni, tabCurso, tabMap, tabMapMunicipio = st.tabs(["Por Unidade Federativa", "Categorias Administrativas", "Top 10 Municípios", "Top 10 IES com mais cursos", "Mapa UF's", "Mapa Municípios"])

with tabUF:
    st.markdown(f"Total de Instituições de Ensino Superior por UF.")

    ufDF = regiaoDF.groupby(['REGIAO', 'UF'])['CODIGO_IES'].nunique().reset_index(name='quantidade').sort_values(by='quantidade', ascending=False)

    ufChart = alt.Chart(ufDF).mark_bar().encode(
        x=alt.X('UF:N', sort='-y'),
        y='quantidade:Q'
    )
    st.altair_chart(ufChart, use_container_width=True)

with tabCat:
    st.markdown(f"Total de Instituições de Ensino Superior por CATEGORIA ADMINISTRATIVA.")

    catDF = regiaoDF.groupby(['REGIAO', 'CATEGORIA_ADMINISTRATIVA'])['CODIGO_IES'].nunique().reset_index(name='quantidade').sort_values(by='quantidade', ascending=False)

    catChart = alt.Chart(catDF).mark_bar().encode(
        x=alt.X('CATEGORIA_ADMINISTRATIVA:N', sort='-y'),
        y='quantidade:Q',
        color='REGIAO',
        tooltip=['REGIAO', 'quantidade']
    )
    st.altair_chart(catChart, use_container_width=True)

with tabMuni:
    st.markdown(f"Top 10 Municípios com mais Instituições de Ensino Superior.")

    muniDF = regiaoDF.groupby(['REGIAO', 'MUNICIPIO'])['CODIGO_IES'].nunique().reset_index(name='quantidade').sort_values(by='quantidade', ascending=False)

    top10DF = muniDF.head(10)

    muniChart = alt.Chart(top10DF).mark_bar().encode(
        x=alt.X('MUNICIPIO:N', sort='-y'),
        y='quantidade:Q'
    )
    st.altair_chart(muniChart, use_container_width=True)


with tabCurso:
    st.markdown(f"Top 10 Instituições de Ensino Superior com mais cursos.")

    cursoDF = regiaoDF.groupby(['REGIAO', 'NOME_IES'])['CODIGO_CURSO'].nunique().reset_index(name='quantidade').sort_values(by='quantidade', ascending=False)

    top10IesDF = cursoDF.head(10)

    cursoChart = alt.Chart(top10IesDF).mark_bar().encode(
        x=alt.X('NOME_IES:N', sort='-y'),
        y='quantidade:Q'
    )
    st.altair_chart(cursoChart, use_container_width=True)

with tabMap:
    mostrar_mapa(regiaoDF)
    

with tabMapMunicipio:
    mostrar_mapa_municipios(regiaoDF)

menu_barra() # Render the dynamic menu!

