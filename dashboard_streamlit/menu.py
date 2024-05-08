import streamlit as st

def set_regiao():
    # Callback function to save the role selection to Session State
    st.session_state.regiao = st.session_state._regiao

def menu_inicio():
    st.sidebar.page_link("app.py", label=":house: INÍCIO")
    st.sidebar.markdown("---")
    
    st.sidebar.page_link("pages/IES.py", label="Instituições de Ensino Superior")
    st.sidebar.page_link("pages/Linha.py", label="Cursos de Graduação")
    st.sidebar.page_link("pages/Ponto.py", label="Vagas Autorizadas")
    
    st.sidebar.markdown("---")
    st.sidebar.page_link("pages/Dataset.py", label="Sobre o Dataset")
    st.sidebar.page_link("pages/Sobre.py", label="Sobre esse Trabalho")

def menu_barra():
    st.session_state._regiao = st.session_state.regiao
    st.sidebar.selectbox(
        "Selecione um Região:",
        #[None,'AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO','ZZ'],
        ['TODAS', 'SUDESTE', 'NORDESTE', 'SUL', 'CENTRO-OESTE', 'NORTE'],
        key="_regiao",
        on_change=set_regiao
    )
    st.sidebar.toggle("Cursos Ativos", False)
    st.sidebar.multiselect("Selecione a Modalidade", ["Educação a Distância", "Educação Presencial"])

    st.sidebar.markdown("---")
    st.sidebar.page_link("pages/IES.py", label="Instituições de Ensino Superior")
    st.sidebar.page_link("pages/Linha.py", label="Cursos de Graduação")
    st.sidebar.page_link("pages/Ponto.py", label="Vagas Autorizadas")

    st.sidebar.markdown("---")
    st.sidebar.page_link("app.py", label="Voltar ao Início")