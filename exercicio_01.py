def eh_par (numero: int) -> bool:
   return numero % 2 == 0
from unittest.mock import patch
import importlib
import pytest
@patch("builtins.print")
@patch("builtins.input")
@pytest.mark.parametrize(
    argnames=["argumento", "real"],
    argvalues=[(0, True), (1, False), (2, True), (3, False), (4, True), (-1, False)],
)
def test_exercicio_01(input, print, argumento: int, real: bool):
    exercicio_01 = importlib.reload(importlib.import_module("exercicio_01"))
    assert exercicio_01.eh_par, "Não definiu a função eh_par"
    funcao = exercicio_01.eh_par
    nome_funcao = funcao.__name__
    aluno = funcao(argumento)
    assert not input.called, "A função input não deveria ser usada"
    assert not print.called, "A função print não deveria ser usada"
    assert aluno == real, (
        f"A função {nome_funcao}({argumento}) deveria retornar => {real}, mas retornou {aluno}"
    )
