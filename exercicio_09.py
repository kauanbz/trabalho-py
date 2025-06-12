import pandas as pd

def filtra_df(df: pd.DataFrame, col: str, lim):
    if col not in df.columns:
        raise ValueError(f"Coluna '{col}' não encontrada.")

    if not pd.api.types.is_numeric_dtype(df[col]):
        raise TypeError(f"Coluna '{col}' não é numérica.")

    return df[df[col] >= lim]
