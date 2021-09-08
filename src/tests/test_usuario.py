from src.leilao.dominio import Usuario, Leilao

import pytest

from src.leilao.excecoes import LanceInvalido


class Vini:
    pass


@pytest.fixture
def artur():
    return Usuario(Artur, 100.0)


@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(artur, leilao):
    artur.propoe_lance(leilao, 50.0)

    assert artur.carteira == 50.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(artur, leilao):
    artur.propoe_lance(leilao, 1.0)

    assert vini.carteira == 99.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(artur, leilao):
    artur.propoe_lance(leilao, 100.0)

    assert artur.carteira == 0.0


def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(artur, leilao):
    with pytest.raises(LanceInvalido):

        vini.propoe_lance(leilao, 200.0)
