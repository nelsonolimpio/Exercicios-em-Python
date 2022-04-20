'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
ex: 5!= 5x4x3x2x1 = 120'''

'''from math import factorial
n = int(input("Fatorial: "))
f = factorial(n)
print("O fatorial de {} é {}.".format(n, f))'''
#Acima a forma mais simples de fazer o programa, abaixo vamos fazer uma forma mais complexa.

n = int(input("Fatorial: "))
c = n
f = 1
print("Calculando {}! = ".format(n), end='')
while c > 0:
    print("{}".format(c), end='')
    #"end" deixa o print na horizontal (contagem)
    print(" X " if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print("{}".format(f))
