import pandas as pd

LINK_CSV = "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"

def load_data():
    """Carrega o dataset remoto."""
    df = pd.read_csv(LINK_CSV)
    return df

def filter_data(df, anos, senioridades, contratos, tamanhos):
    """Filtra o dataframe com base nas opções selecionadas."""
    return df[
        (df['ano'].isin(anos)) &
        (df['senioridade'].isin(senioridades)) &
        (df['contrato'].isin(contratos)) &
        (df['tamanho_empresa'].isin(tamanhos))
    ]
