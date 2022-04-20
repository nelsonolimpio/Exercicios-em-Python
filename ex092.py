'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a
CTPS foi diferentes de ZERO, o dicionário receberá o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.'''

from datetime import date

aposentadoria = {}
ano_atual = date.today().year
aposentadoria['Nome'] = str(input('Nome: '))
aposentadoria['Nascimento'] = int(input("ano de nascimento: "))
aposentadoria['Carteira de trabalho'] = int(input("Carteira de trabalho: "))
aposentadoria['Ano de contratação'] = int(input("Ano de contratação: "))
aposentadoria['Salário'] = float(input("Salário: "))
AnoDeAposentadoria = aposentadoria['Ano de contratação'] + 35
ano = ano_atual - aposentadoria['Nascimento']

if aposentadoria["Carteira de trabalho"] > 0:
    print('~='*30)
    print(f'Nome: {aposentadoria["Nome"]}')
    print(f'Idade: {ano}')
    print(f'Aposenta com {AnoDeAposentadoria} anos de idade.')
    print('~='*30)
else:
    print('~='*30)
    print("Não tem carteira de trabalho.")
    print('~='*30)
