'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos
durante o campeonato.'''

jogador = dict()
partidas = list()
jogador['nome'] = str(input("Nome do jogador: "))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
print('~='*30)
for c in range(1, tot+1):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
print('~='*30)
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print(f'Nome do jogador: {jogador["nome"]}')
print(f'{jogador["nome"]} jogou {c} partidas, e fez um total de {jogador["total"]} gols.')
print('~='*30)



