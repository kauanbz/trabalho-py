def conta_ocorrencias(lista: list[int]) -> dict[int, int]:
    frequencias = {}
    for numero in lista:
        if numero in frequencias:
            frequencias[numero] += 1
        else:
            frequencias[numero] = 1
    return frequencias
from unittest.mock import patch
import pytest
import importlib
@patch("builtins.print")
@patch("builtins.input")
@pytest.mark.parametrize(
    argnames=["argumento", "real"],
    argvalues=[
        ([], {}),  # lista vazia
        ([1], {1: 1}),  # único elemento
        ([1, 2, 1, 3, 2, 1], {1: 3, 2: 2, 3: 1}),  # múltiplos valores
        ([0, 0, 0], {0: 3}),  # zeros repetidos
        ([-1, -1, 2, 2, 2], {-1: 2, 2: 3}),  # negativos e positivos
        ([5, 5, 5, 5, 5], {5: 5}),  # todos iguais
    ],
)
def test_exercicio_04(input, print, argumento: list[int], real: dict[int, int]):
    exercicio_04 = importlib.reload(importlib.import_module("exercicio_04"))
    # Verifica existência da função
    assert hasattr(exercicio_04, "conta_ocorrencias"), (
        "Não definiu a função conta_ocorrencias"
    )
    funcao = exercicio_04.conta_ocorrencias
    nome_funcao = funcao.__name__
    # Executa o código do aluno
    aluno = funcao(argumento)
    # Garante que não usou input() ou print()
    assert not input.called, "A função input não deveria ser usada"
    assert not print.called, "A função print não deveria ser usada"
    # Verifica resultado
    assert isinstance(aluno, dict), (
        f"{nome_funcao} deve retornar um dict, mas retornou {type(aluno).__name__}"
    )
    assert aluno == real, (
        f"A função {nome_funcao}({argumento}) deveria retornar => {real}, mas retornou {aluno}"
    )
