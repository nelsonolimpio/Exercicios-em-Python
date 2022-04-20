'''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número de 0 a 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.'''

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
while num != escolhido:
    lista = [n0, n1, n2, n3, n4, n5]
    escolhido = choice(lista)
    num = int(input("Digite um número de 0 até 5: "))
    print("O número escolhido pelo computador foi {}.".format(escolhido))
    if num == escolhido:
        print("Parabéns")
    else:
        print("Tente novamente")
print("--FIM--")
