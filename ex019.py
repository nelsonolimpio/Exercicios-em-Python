from random import choice

n1 = str(input("primeiro aluno: "))
n2 = str(input("segundo aluno: "))
n3 = str(input("terceiro aluno: "))
n4 = str(input("quarto aluno: "))
lista = [n1, n2, n3, n4]  # python, lista fica entre colchetes.
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
