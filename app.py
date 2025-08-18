import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from src.data import load_data, filter_data
from src.plots import (
    kpi_metrics,
    grafico_distribuicao_salarios,
    grafico_top_cargos,
    grafico_paises
)

# ---------------- Configuração da página ----------------
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide"
)

# Estilos customizados (para card com fundo cinza)
st.markdown(
    """
    <style>
    .metric-card {
        background-color: #2e2e2e;
        padding: 15px;
        border-radius: 8px;
        color: #ffffff;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- Carregamento dos dados ----------------
df = load_data()

# ---------------- Sidebar: filtros ----------------
st.sidebar.header("Filtros")

anos = sorted(df['ano'].unique())
senioridades = sorted(df['senioridade'].unique())
contratos = sorted(df['contrato'].unique())
tamanhos = sorted(df['tamanho_empresa'].unique())

anos_sel = st.sidebar.multiselect("Ano", anos, default=anos)
sen_sel = st.sidebar.multiselect("Senioridade", senioridades, default=senioridades)
cont_sel = st.sidebar.multiselect("Tipo de Contrato", contratos, default=contratos)
tam_sel = st.sidebar.multiselect("Tamanho da Empresa", tamanhos, default=tamanhos)

df_filtrado = filter_data(df, anos_sel, sen_sel, cont_sel, tam_sel)

# ---------------- Seletor de páginas ----------------
pagina = st.sidebar.radio(
    "Selecione a Página",
    ["Visão Geral", "Cargos", "Países"]
)

# ---------------- Página: Visão Geral ----------------
if pagina == "Visão Geral":
    st.title("Visão Geral")

    if not df_filtrado.empty:
        salario_medio, salario_max, total_reg, cargo_freq = kpi_metrics(df_filtrado)

        # KPIs em 2 linhas
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"<div class='metric-card'><b>Salário médio (USD)</b><br>${salario_medio:,.0f}</div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='metric-card'><b>Salário máximo (USD)</b><br>${salario_max:,.0f}</div>", unsafe_allow_html=True)

        col3, col4 = st.columns(2)
        with col3:
            st.markdown(f"<div class='metric-card'><b>Total de registros</b><br>{total_reg:,}</div>", unsafe_allow_html=True)
        with col4:
            st.markdown(f"<div class='metric-card'><b>Cargo mais frequente</b><br>{cargo_freq}</div>", unsafe_allow_html=True)

        st.plotly_chart(
            grafico_distribuicao_salarios(df_filtrado),
            use_container_width=True
        )
    else:
        st.warning("Nenhum dado disponível com os filtros selecionados.")

# ---------------- Página: Cargos ----------------
elif pagina == "Cargos":
    st.title("Análise por Cargos")

    if not df_filtrado.empty:
        st.plotly_chart(
            grafico_top_cargos(df_filtrado),
            use_container_width=True
        )
        st.dataframe(df_filtrado)
    else:
        st.warning("Nenhum dado disponível com os filtros selecionados.")

# ---------------- Página: Países ----------------
else:
    st.title("Análise por Países")

    if not df_filtrado.empty:
        st.plotly_chart(
            grafico_paises(df_filtrado),
            use_container_width=True
        )
    else:
        st.warning("Nenhum dado disponível com os filtros selecionados.")
# ---------------- Rodapé ----------------
