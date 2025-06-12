def soma_positivos (valores:list[float]) -> float:
    return sum(valor for valor in valores if valor > 0)
