def classifica_notas(notas: list[float]) -> list[str]:
    classificacao = []
    for n in notas:
        if n >= 6.0:
            classificacao.append("Aprovado")
        elif n >= 4.0:
            classificacao.append("Recuperação")
        else:
            classificacao.append("Reprovado")
    return classificacao
