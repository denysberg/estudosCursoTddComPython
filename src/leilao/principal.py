from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

carla = Usuario('Carla')
denys = Usuario('Denys')

lance_do_denys = Lance(denys, 100.0)
lance_do_carla = Lance(carla, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_denys)
leilao.lances.append(lance_do_carla)

for lance in leilao.lances:
    print('O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {leilao.menor_lance} e o maior lance foi de {leilao.maior_lance}')
