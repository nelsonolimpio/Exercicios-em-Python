'''Crie um programa que leie nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média. '''

dados = {}
mulheres = []
lista = []
soma = 0
while True:
    dados['nome'] = str(input("Nome: "))
    dados['idade'] = int(input("Idade: "))
    while True:
        dados['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Opção inválida, tente novamente desta vez com M ou F.')

    lista.append(dados.copy())
    soma += dados['idade']

    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])

    while True:
        op = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
        if op in 'SN':
            break
    if op == "N":
        break
print('~='* 40)
print('                   R E L A T Ó R I O          ')
print('~='* 40)
print(f'Total de pessoas cadastradas: {len(lista)}')
print(f'Média de idade: {soma/len(lista):.2f}')
print(f'Mulheres cadastradas: {mulheres}')
for a in lista:
    if a['idade'] >= soma/len(lista):
        print(f'Pessoas com idade a cima da média: {a["nome"]} com {a["idade"]} anos.')

print('~='* 40)

