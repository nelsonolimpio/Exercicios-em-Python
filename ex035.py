'''Faça um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
print('-='*20)
print('Analisador de triângulo')
print('-='*20)
r1 = float(input("1° Linha: "))
r2= float(input("2° Linha: "))
r3 = float(input("3° Linha: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR triangulo.")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo.")
