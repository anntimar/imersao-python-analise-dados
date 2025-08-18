import plotly.express as px

# Paleta neutra
PALETA = ["#4c6a8a", "#6b7d8c", "#8898a1", "#a4adb5"]

def _apply_layout(fig, title: str = ""):
    fig.update_layout(
        title=title,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        title_x=0.0  # alinhado à esquerda
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    return fig

def kpi_metrics(df):
    salario_medio = df['usd'].mean()
    salario_maximo = df['usd'].max()
    total_registros = df.shape[0]
    cargo_mais_frequente = df["cargo"].mode()[0]
    return salario_medio, salario_maximo, total_registros, cargo_mais_frequente

def grafico_distribuicao_salarios(df):
    fig = px.histogram(
        df,
        x='usd',
        nbins=30,
        color_discrete_sequence=PALETA,
        labels={'usd': 'Faixa salarial (USD)'}
    )
    return _apply_layout(fig, title="Distribuição de salários anuais")

def grafico_top_cargos(df):
    top_cargos = (
        df.groupby('cargo')['usd']
          .mean()
          .nlargest(10)
          .sort_values(ascending=True)
          .reset_index()
    )
    fig = px.bar(
        top_cargos,
        x="usd",
        y="cargo",
        orientation="h",
        color_discrete_sequence=PALETA,
        labels={'usd': 'Média salarial anual (USD)', 'cargo': ''}
    )
    return _apply_layout(fig, title="Top 10 cargos por salário médio")

def grafico_paises(df):
    df_ds = df[df['cargo'] == 'Data Scientist']
    media_ds_pais = (
        df_ds.groupby('residencia_iso3')['usd']
             .mean()
             .reset_index()
    )
    fig = px.choropleth(
        media_ds_pais,
        locations='residencia_iso3',
        color='usd',
        color_continuous_scale="Blues",
        labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'},
    )
    fig.update_layout(title="Salário médio de Cientista de Dados por país", title_x=0.0)
    return fig
