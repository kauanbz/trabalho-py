def filtra_maiores_que(valores: list[float], limiar: float) -> list[float]:
    return [v for v in valores if v > limiar]
from unittest.mock import patch
import pytest
import importlib


@patch("builtins.print")
@patch("builtins.input")
@pytest.mark.parametrize(
    argnames=["valores", "limiar", "real"],
    argvalues=[
        ([], 5.0, []),  # lista vazia
        ([1.0, 2.0, 3.0], 2.0, [3.0]),  # apenas > 2.0
        ([5.0, 5.0, 5.0], 5.0, []),  # estritamente > 5.0
        ([0.5, 1.5, 2.5], 1.0, [1.5, 2.5]),  # mistura de floats
        ([-1.0, 0.0, 1.0], 0.0, [1.0]),  # inclui zero, negativos
        ([2.2, 3.3, 2.2, 4.4], 2.2, [3.3, 4.4]),  # repetidos e > limiar
    ],
)
def test_exercicio_05(
    input, print, valores: list[float], limiar: float, real: list[float]
):
    # Recarrega o módulo após aplicar o patch
    exercicio_05 = importlib.reload(importlib.import_module("exercicio_05"))

    # Verifica existência da função
    assert hasattr(exercicio_05, "filtra_maiores_que"), (
        "Não definiu a função filtra_maiores_que"
    )
    funcao = exercicio_05.filtra_maiores_que
    nome_funcao = funcao.__name__

    # Executa o código do aluno
    resultado = funcao(valores, limiar)

    # Garante que não usou input() ou print()
    assert not input.called, "A função input não deveria ser usada"
    assert not print.called, "A função print não deveria ser usada"

    # Verifica tipo e valor
    assert isinstance(resultado, list), (
        f"{nome_funcao} deve retornar uma list, mas retornou {type(resultado).__name__}"
    )
    assert resultado == real, (
        f"A função {nome_funcao}({valores}, {limiar}) deveria retornar => {real}, mas retornou {resultado}"
    )
