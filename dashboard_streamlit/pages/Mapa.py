import streamlit as st
import pandas as pd
import altair as alt

# Obtendo o GeoJson de UFs do Brasil
geom = alt.Data(
            url="https://raw.githubusercontent.com/fititnt/gis-dataset-brasil/master/uf/geojson/uf.json",
            format=alt.DataFormat(property='features')
)

def mostrar_mapa(regiaoDF):
    st.markdown(f"Mapa de Instituições de Ensino Superior por UF.")

    ufDF = regiaoDF.groupby(['REGIAO', 'UF'])['CODIGO_IES'].nunique().reset_index(name='quantidade').sort_values(by='quantidade', ascending=False)
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