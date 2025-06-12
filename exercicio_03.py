def maximo_personalizado(valores: list[float]) -> float:

    mv = valores[0]
    for v in valores[1:]:
        if v > mv:
            mv = v
    return mv
