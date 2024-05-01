import streamlit as st
from menu_tarefa03 import menu_inicio

st.title("TAREFA 03 - DASHBOARD STREAMLIT")
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