'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
- EQUILÁTERO: todos os lados iguais
- ISÓCELES: dois lados iguals
- ESCALENO: todos os lados diferentes'''

print('-='*20)
print('Analisador de triângulo')
print('-='*20)
r1 = float(input("1° Linha: "))
r2= float(input("2° Linha: "))
r3 = float(input("3° Linha: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR triangulo.")
    if r1 == r2 and r1 == r3 and r2 == r3:
        print("Triângulo EQUILÁTERO.")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Triângulo ISÓCELES.")
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print("Triângulo ESCALENO.")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo.")