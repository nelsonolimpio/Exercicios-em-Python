'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o 1° e o ultimo nome separadamente.
ex: Ana MAria de Souza
1° = Ana
ultimo = Souza '''

n = str(input("Digite um nome: ")).strip()
nome = n.split()
print("Seu primeiro nome é {}.".format(nome[0]))
print("Seu ultimo nome é {}.".format(nome[len(nome)-1]))

