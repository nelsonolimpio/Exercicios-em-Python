'''Escreva um programa que leia dois números inteiro e compare-os, mostrando la tela uma mensagem
- O primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais'''

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

if n1 > n2:
    print("O primeiro valor é maior.")
elif n2 > n1:
    print("Segundo valor é maior.")
else:
    print("Não exsite valor maior, os dois são iguais.")