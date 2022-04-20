'''Crie um programa que leia um número inteiro e mostre na tela se ele é pra ou ímpar.'''

n = int(input("Digite um número inteiro: "))
resto =  n % 2
if resto == 0:
    print("Número par.")
else:
    print("Número impár.")