'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.'''

ano = int(input("Digite um ano: "))
resto = ano % 4
if resto == 0:
    print("Ano Bissexto.")
else:
    print("Ano não Bissexto.")