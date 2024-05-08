import streamlit as st
from menu import menu_inicio

st.title("Dataset")
st.markdown(f"""Dados dos cursos de graduação autorizados de todas as universidades do Brasil, por estado e município.

Fonte: [Distribuição dos cursos de graduação pelo Brasil](https://dadosabertos.mec.gov.br/indicadores-sobre-ensino-superior/item/183-cursos-de-graduacao-do-brasil)

**Colunas**
* `CODIGO_IES`: código da Instituição de Educação Superior (IES);
* `NOME_IES`: nome da IES;
* `CATEGORIA_ADMINISTRATIVA`: categoria da IES;
* `ORGANIZACAO_ACADEMICA`: organização acadêmica;
* `CODIGO_CURSO`: código do curso;
* `NOME_CURSO`: nome do curso;
* `GRAU`: grau;
* `AREA_OCDE`: área OCDE;
* `MODALIDADE`: modalidade de ensino (presencial ou EaD);
* `SITUACAO_CURSO`: situação do curso (ativo ou inativo);
* `QT_VAGAS_AUTORIZADAS`: vagas autorizadas;
* `CARGA_HORARIA`: carga horária;
* `CODIGO_AREA_OCDE_CINE`: segmentadas por código do município (IBGE);
* `AREA_OCDE_CINE`:
* `CODIGO_MUNICIPIO`: Nome do Município;
* `MUNICIPIO`:
* `UF`: Unidade Federativa;
* `REGIAO`: Região

**Estatísticas básicas dos dados**
* Número de atributos: 18
* Quantidade de registros: 902.676""")

st.dataframe(st.session_state.dataset.head())

menu_inicio() # Render the dynamic menu!