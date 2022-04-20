'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela. '''

aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('~=' * 17)
print(f'Aluno: {aluno["nome"]}')
print(f'A Média de {aluno["nome"]} é {aluno["média"]}')

if aluno['média'] < 7:
    print("Aluno reprovado!")
else:
    print("Aluno aprovado!")

print("~="*17)