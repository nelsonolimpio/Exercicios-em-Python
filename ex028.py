'''Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
  O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import choice
n0 = int(0)
n1 = int(1)
n2 = int(2)
n3 = int(3)
n4 = int(4)
n5 = int(5)
lista = [n0, n1, n2, n3, n4, n5]
escolhido = choice(lista)
num = int(input("Digite um número de 0 até 5: "))
print("O número escolhido pelo computador foi {}.".format(escolhido))
if num == escolhido:
    print("Parabéns, você acertou!")
else:
    print("Infelizmente, você perdeu! Tente outra vez.")
print("--FIM--")
