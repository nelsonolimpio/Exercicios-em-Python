'''Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de 3 e que se encontram no intervalo de 1 até 100'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print("A soma de todos os {} valores solicitados são {}.".format(cont, soma))

