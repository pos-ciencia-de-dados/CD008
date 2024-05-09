import streamlit as st

def set_regiao():
    st.session_state.regiao = st.session_state._regiao

def set_ativo():
    st.session_state.ativo = st.session_state._ativo

def set_grau():
    st.session_state.grau = st.session_state._grau

def set_modalidade():
    st.session_state.modalidade = st.session_state._modalidade

def menu_inicio():
    st.sidebar.page_link("app.py", label=":house: INÍCIO")
    st.sidebar.markdown("---")
    
    st.sidebar.page_link("pages/IES.py", label="Instituições de Ensino Superior")
#    st.sidebar.page_link("pages/Vagas_Autorizadas.py", label="Vagas Autorizadas pelo MEC")
#    st.sidebar.page_link("pages/Linha.py", label="[DEPRECATED] Cursos de Graduação")
#    st.sidebar.page_link("pages/Ponto.py", label="[DEPRECATED] Vagas Autorizadas")
    
    st.sidebar.markdown("---")
    st.sidebar.page_link("pages/Dataset.py", label="Sobre o Dataset")
    st.sidebar.page_link("pages/Sobre.py", label="Sobre esse Trabalho")

def menu_barra():
    st.session_state._regiao = st.session_state.regiao
    st.sidebar.selectbox(
        "Selecione uma Região:",
        ['TODAS', 'SUDESTE', 'NORDESTE', 'SUL', 'CENTRO-OESTE', 'NORTE'],
        key="_regiao",
        on_change=set_regiao
    )

    st.sidebar.toggle(
        "Remover cursos extintos e em extinção",
        False,
        key="_ativo",
        on_change=set_ativo
    )

    st.sidebar.multiselect(
        "Selecione o Grau do Curso",
        ["Área Básica de Ingresso (ABI)","Bacharelado","Licenciatura","Sequencial","Tecnológico"], 
        key="_grau",
        on_change=set_grau
    )

    st.sidebar.selectbox(
        "Selecione a Modalidade",
        ["Ambas", "Educação a Distância", "Educação Presencial"],
        key="_modalidade",
        on_change=set_modalidade
    )
    
    st.sidebar.markdown("---")
    st.sidebar.page_link("pages/IES.py", label="Instituições de Ensino Superior")
#    st.sidebar.page_link("pages/Vagas_Autorizadas.py", label="Vagas Autorizadas pelo MEC")
#    st.sidebar.page_link("pages/Linha.py", label="[DEPRECATED] Cursos de Graduação")
#    st.sidebar.page_link("pages/Ponto.py", label="[DEPRECATED] Vagas Autorizadas")

    st.sidebar.markdown("---")
    st.sidebar.page_link("app.py", label="Voltar ao Início")