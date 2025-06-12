def filtra_maiores_que(valores: list[float], limiar: float) -> list[float]:
    return [v for v in valores if v > limiar]
