import streamlit as st
import pandas as pd
import altair as alt
from menu import menu_barra

# Obtendo o GeoJson de UFs do Brasil
geom = alt.Data(
            url="https://raw.githubusercontent.com/fititnt/gis-dataset-brasil/master/uf/geojson/uf.json",
            format=alt.DataFormat(property='features')
)


if "regiao" not in st.session_state:
    st.session_state.regiao = "TODAS"

if "ativo" not in st.session_state:
    st.session_state.ativo = False

if "modalidade" not in st.session_state:
    st.session_state.modalidade = "Ambas"

if "grau" not in st.session_state:
    st.session_state.grau = []

st.title(f"Vagas autorizadas pelo MEC (Região: {st.session_state.regiao})")

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

st.markdown(f"Mapa de Instituições de Ensino Superior por UF.")

ufDF = regiaoDF.groupby(['REGIAO', 'UF'])['QT_VAGAS_AUTORIZADAS'].sum().reset_index(name='quantidade').sort_values(by='quantidade', ascending=False)
ufDF = ufDF.rename(columns={'UF':'UF_05'})

ufMapa = alt.Chart(geom).mark_geoshape(
    stroke='black',
    strokeWidth=0.1
).project(
    type='mercator'
).encode(
    color = alt.Color('quantidade:Q',
                #type='quantitative',
                scale=alt.Scale(type='linear', scheme='goldgreen')),
    tooltip=[
        alt.Tooltip('properties.UF_05:N', title='UF '),
        alt.Tooltip('quantidade:Q', title='Quantidade', format=",.0f")
    ]
).transform_lookup(
    lookup='properties.UF_05',
    from_=alt.LookupData(ufDF, 'UF_05', ['quantidade'])
).properties(
    width=800,
    height=600
).interactive()

# Exibindo o mapa
(ufMapa).configure_view(strokeWidth=0)

#c01 = mapa_altair

st.altair_chart(ufMapa, use_container_width=True)
    
menu_barra() # Render the dynamic menu!

