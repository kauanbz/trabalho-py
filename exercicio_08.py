import pandas as pd

def cria_resumo(df: pd.DataFrame, col: str) -> pd.DataFrame:
    if col not in df.columns:
        raise ValueError(f"Coluna '{col}' não encontrada.")

    if not pd.api.types.is_numeric_dtype(df[col]):
        raise TypeError(f"Coluna '{col}' não é numérica.")

    res = df[col].describe().to_frame()
    return res
