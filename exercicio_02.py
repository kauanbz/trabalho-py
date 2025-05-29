def soma_positivos (valores:list[float]) -> float:
    return sum(valor for valor in valores if valor > 0)

    from unittest.mock import patch
from unittest.mock import patch
import pytest
import importlib


@patch("builtins.print")
@patch("builtins.input")
@pytest.mark.parametrize(
    argnames=["argumento", "real"],
    argvalues=[
        ([1.0, 2.0, 3.0], 6.0),
        ([0.0, 0.0], 0.0),
        ([1.0], 1.0),
        ([-1.0], 0.0),
        ([], 0.0),  # lista vazia
        ([-1.0, -2.5, -3.7], 0.0),  # todos negativos
        ([1.5, -0.5, 2.5, 0.0], 4.0),  # mistura positivos, negativos e zero
        ([0.1, 0.2, 0.3, 0.4], 1.0),  # decimais que somam exatamente 1.0
    ],
)
def test_exercicio_02(input, print, argumento: list[float], real: float):
    exercicio_02 = importlib.reload(importlib.import_module("exercicio_02"))

    assert hasattr(exercicio_02, "soma_positivos"), (
        "Não definiu a função soma_positivos"
    )
    funcao = exercicio_02.soma_positivos
    nome_funcao = funcao.__name__
    aluno = funcao(argumento)

    assert not input.called, "A função input não deveria ser usada"
    assert not print.called, "A função print não deveria ser usada"
    assert aluno == real, (
        f"A função {nome_funcao}({argumento}) deveria retornar => {real}, mas retornou {aluno}"
    )
