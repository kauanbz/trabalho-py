def maximo_personalizado(valores: list[float]) -> float:

    maior = valores[0]
    for valor in valores[1:]:
        if valor > maior:
            maior = valor
    return maior
from unittest.mock import patch
import pytest
import importlib
@patch("builtins.print")
@patch("builtins.input")
@patch("builtins.max")
@pytest.mark.parametrize(
    argnames=["argumento", "real"],
    argvalues=[
        ([3.2, 7.8, 1.5, 7.9, 2.4], 7.9),  # maior no meio
        ([0.0], 0.0),  # único elemento
        ([-1.0, -5.5, -3.3], -1.0),  # todos negativos
        ([5.5, 5.5, 2.2], 5.5),  # valores repetidos
        ([100.0, 50.0, 1000.0], 1000.0),  # último é o maior
        ([1.1, 2.2, 3.3, 2.2, 3.3, 3.3], 3.3),  # máximo repetido várias vezes
    ],
)
def test_exercicio_03(max, input, print, argumento: list[float], real: float):
    exercicio_03 = importlib.reload(importlib.import_module("exercicio_03"))
    # Verifica existência da função
    assert hasattr(exercicio_03, "maximo_personalizado"), (
        "Não definiu a função maximo_personalizado"
    )
    funcao = exercicio_03.maximo_personalizado
    nome_funcao = funcao.__name__
    # Executa o código do aluno
    aluno = funcao(argumento)
    # Garante que não usou max(), input() ou print()
    assert not max.called, "A função max não deveria ser usada"
    assert not input.called, "A função input não deveria ser usada"
    assert not print.called, "A função print não deveria ser usada"
    # Verifica resultado
    assert aluno == real, (
        f"A função {nome_funcao}({argumento}) deveria retornar => {real}, mas retornou {aluno}"
    )
