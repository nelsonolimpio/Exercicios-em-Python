'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas as letras minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Nome completo: {}".format(nome))
print('Nome em letras maiúscula: {}'.format(nome.upper()))
print('Nome em letras minúsculas: {}'.format(nome.lower()))
print('O nome digitado possui {} letras ao todo.'.format(len(nome)-nome.count(' ')))
print('O primeiro nome tem {} letras.'.format(nome.find(' ')))