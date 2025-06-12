def conta_ocorrencias(lista: list[int]) -> dict[int, int]:
    frequencias = {}
    for numero in lista:
        if numero in frequencias:
            frequencias[numero] += 1
        else:
            frequencias[numero] = 1
    return frequencias
