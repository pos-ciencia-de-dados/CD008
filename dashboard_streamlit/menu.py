import streamlit as st

def set_regiao():
    # Callback function to save the role selection to Session State
    st.session_state.regiao = st.session_state._regiao

def menu_inicio():
    st.sidebar.page_link("app.py", label="INÍCIO")
    st.sidebar.markdown("---")
    
    st.sidebar.markdown("Gráficos:")
    st.sidebar.page_link("pages/Barra.py", label="Gráfico em Barra")
    st.sidebar.page_link("pages/Pizza.py", label="Gráfico de Pizza")
    st.sidebar.page_link("pages/Linha.py", label="Gráfico de Linha")
    st.sidebar.page_link("pages/Ponto.py", label="Gráfico de Ponto")
    
    st.sidebar.markdown("---")
    st.sidebar.page_link("pages/Dataset.py", label="Sobre o Dataset")

def menu_barra():
    # Retrieve the UF from Session State to initialize the widget
    st.session_state._regiao = st.session_state.regiao
    st.sidebar.selectbox(
        "Selecione um Região:",
        #[None,'AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO','ZZ'],
        ['SUDESTE', 'NORDESTE', 'SUL', 'CENTRO-OESTE', 'NORTE'],
        key="_regiao",
        on_change=set_regiao
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown("Gráficos:")
    st.sidebar.page_link("pages/Barra.py", label="Gráfico em Barra")
    st.sidebar.page_link("pages/Pizza.py", label="Gráfico de Pizza")
    st.sidebar.page_link("pages/Linha.py", label="Gráfico de Linha")
    st.sidebar.page_link("pages/Ponto.py", label="Gráfico de Ponto")

    st.sidebar.markdown("---")
    st.sidebar.page_link("app.py", label="Voltar ao Início")