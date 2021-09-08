from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    # test_quando_adicionados_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance

    def setUp(self):
        self.carla = Usuario('Carla', 500.0)
        self.lance_do_carla = Lance(self.carla, 150.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        denys = Usuario('Denys', 500.0)
        lance_do_denys = Lance(denys, 100.0)

        self.leilao.propoe(lance_do_denys)
        self.leilao.propoe(self.lance_do_carla)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            denys = Usuario('Denys', 500.0)
            lance_do_denys = Lance(denys, 100.0)

            self.leilao.propoe(self.lance_do_carla)
            self.leilao.propoe(lance_do_denys)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_carla)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        denys = Usuario('Denys', 500.0)
        lance_do_denys = Lance(denys, 100.0)
        vini = Usuario('Vini', 500.0)

        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(lance_do_denys)
        self.leilao.propoe(self.lance_do_carla)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_carla)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        denys = Usuario('Denys', 500.0)
        lance_do_denys = Lance(denys, 200.0)

        self.leilao.propoe(self.lance_do_carla)
        self.leilao.propoe(lance_do_denys)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_carla200 = Lance(self.carla, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_carla)
            self.leilao.propoe(lance_do_carla200)
