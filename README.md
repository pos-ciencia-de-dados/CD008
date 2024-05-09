## [TRABALHO FINAL] Dashboard: Distribuição de Cursos de Graduação no Brasil

Todos os cursos de graduação no Brasil, com informações sobre a modalidade de ensino, categoria administrativa das instituições, e a distribuição geográfica dos cursos.

Grupo
* Andre dos Santos Gianini
* Carlos Eduardo Rodrigues Felix
* Hermano Albuquerque Lira

---

### Objetivo do Trabalho

A educação superior no Brasil é um campo dinâmico e diversificado, abrangendo uma ampla gama de instituições, cursos e modalidades de ensino.
Com a expansão do acesso à educação superior nas últimas décadas, é crucial compreender a estrutura e a distribuição dos cursos oferecidos pelas
Instituições de Educação Superior (IES) para avaliar a eficácia das políticas educacionais e a adequação da oferta aos objetivos de
desenvolvimento nacional.
Este estudo emprega uma análise detalhada de um dataset compreensivo que inclui informações sobre cursos de graduação em todo o território
nacional, cobrindo aspectos como modalidade de ensino, categoria administrativa das instituições, e a distribuição geográfica dos cursos.

Utilizando a API Vega-Altair, uma ferramenta declarativa para visualização de dados em Python, este trabalho apresenta uma série de visualizações
que destacam tendências importantes e fornecem insights sobre a distribuição dos cursos de graduação.
As visualizações focam em diversas características, incluindo a natureza dos cursos (como Licenciatura, Bacharelado, entre outros), a modalidade
de ensino (presencial ou à distância), e a situação atual dos cursos (ativo ou inativo). 
Além disso, aspectos como a carga horária, vagas autorizadas, e a localização geográfica das IES são examinados para ilustrar como os recursos
educacionais estão alocados.

Este estudo não apenas visa elucidar o panorama atual da educação superior no Brasil, mas também busca contribuir para debates sobre 
políticas educacionais, ajudando a identificar áreas de atenção e oportunidades para intervenções estratégicas. Ao oferecer uma visão 
clara e detalhada do cenário educacional superior, esperamos apoiar os formuladores de políticas, educadores e stakeholders na 
implementação de melhorias significativas na educação brasileira.

### Instalação das dependências para execução local do Dashboard

```bash
pip install -r requirements.txt
```

### Comando para execução local do Dashboard

```bash
streamlit run dashboard_streamlit/app.py
```

### Última versão disponível em
https://trabalho-final.streamlit.app

### Referências

* [Distribuição dos cursos de graduação pelo Brasil](https://dadosabertos.mec.gov.br/indicadores-sobre-ensino-superior/item/183-cursos-de-graduacao-do-brasil)

* [Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/)

* [Streamlit API](https://docs.streamlit.io/develop/api-reference)