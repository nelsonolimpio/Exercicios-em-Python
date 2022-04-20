'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre eles e qual foi a maior e os menores valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.'''

resp = 'S'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N] -> ")).upper().strip()[0]
media = soma / quant
print("Acabou")
print("Você digitou {} números e a média foi {}. ".format(quant, media))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))