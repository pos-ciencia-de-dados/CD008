import streamlit as st

def set_uf():
    # Callback function to save the role selection to Session State
    st.session_state.uf = st.session_state._uf

def menu_inicio():
    st.sidebar.page_link("app_tarefa03.py", label="INÍCIO")
    st.sidebar.page_link("pages/Barra.py", label="Gráfico em Barra")
    st.sidebar.page_link("pages/Dataset.py", label="Sobre o Dataset")

def menu_barra():
    # Retrieve the UF from Session State to initialize the widget
    st.session_state._uf = st.session_state.uf
    st.sidebar.selectbox(
        "Unidade Federativa:",
        [None,'AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO','ZZ'],
        key="_uf",
        on_change=set_uf
    )
    st.sidebar.page_link("app_tarefa03.py", label="Voltar ao Início")