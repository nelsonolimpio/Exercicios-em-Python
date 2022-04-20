'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na
posição correta de inserção (sem usar o sort). No final, mostre a lista ordenada na tela.'''

valores = list()
for cont in range (0, 5):
    valores.append(int(input("Digite um valor: ")))
print("=~"*25)
print(f"Lista na posição de inserção: {valores}")
print("=~"*25)
valores.sort()
print(f"Lista na ordem crescente: {valores}")
print("=~"*25)