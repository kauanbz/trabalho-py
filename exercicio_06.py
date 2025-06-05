def fatorial(n: int) -> int:
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
