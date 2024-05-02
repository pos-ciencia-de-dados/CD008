import streamlit as st
import pandas as pd
from menu_tarefa03 import menu_inicio
import wget
from zipfile import ZipFile # importing the zipfile module 


title = st.title("Carregando dataset...")

# Initialize st.session_state.dataset to None
if "dataset" not in st.session_state:
    #st.session_state.dataset = None
    link = "https://github.com/pos-ciencia-de-dados/CD008/raw/principal/dataset/PDA_Dados_Cursos_Graduacao_Brasil.zip"
    wget.download(link, "PDA_Dados_Cursos_Graduacao_Brasil.zip")

    # loading the .zip and creating a zip object 
    with ZipFile("PDA_Dados_Cursos_Graduacao_Brasil.zip", 'r') as zObject: 
	    # Extracting all the members of the zip 
	    # into a specific location. 
	    zObject.extractall(path=".") 

st.session_state.dataset = pd.read_csv("PDA_Dados_Cursos_Graduacao_Brasil.csv")

title.title("TAREFA 03 - DASHBOARD STREAMLIT")
st.markdown(f"""
### Objetivo do Trabalho

Em aula vimos vários exemplos de dashboards criadas usando Streamlit.
Para esta tarefa pedimos que criem um novo exemplo usando Streamlit que mostre:

1. Os gráficos gerados na [tarefa Altair](https://colab.research.google.com/drive/1r1AZdntNBJZ-zhuhXUU8w9--lpJVOEA5#scrollTo=mPTB30Z3vY91);

2. Use sidebar e tabs; e

3. Coloque botões que permitam configurar os mapas para mudarem as informações mostradas nos gráficos.

---
Professor: joão Comba
                              
Grupo
* Andre dos Santos Gianini
* Carlos Eduardo Rodrigues Felix
* Hermano Albuquerque Lira            
""")

menu_inicio() # Render the dynamic menu!