# imersao-python-analise-dados

**Dashboard interativo em Streamlit desenvolvido a partir da imersão Python de análise de dados**

Este projeto tem como objetivo apresentar visualmente os dados salariais da área de tecnologia, utilizando técnicas de análise exploratória de dados e construção de dashboards com Streamlit e Plotly.


## Funcionalidades

- Filtros interativos (ano, senioridade, tipo de contrato, tamanho da empresa)
- KPIs principais (salário médio/máximo, cargo mais frequente, total de registros)
- Gráficos dinâmicos:
  - Distribuição de salários
  - Top 10 cargos por média salarial
  - Mapa de salários de Cientista de Dados por país
- Estrutura **multi-páginas** escalável


## Estrutura

- src/ → funções de carregamento de dados e geração de gráficos
- app.py → aplicação principal em Streamlit
- .streamlit/ → configuração de tema (dark)
requirements.txt


## Como executar

```bash
pip install -r requirements.txt
streamlit run app.py

Em seguida, acesse o dashboard no navegador pelo endereço exibido no terminal (geralmente http://localhost:8501)

##Fonte dos dados

Os dados utilizados no dashboard são públicos e foram disponibilizados na URL abaixo:

https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv
