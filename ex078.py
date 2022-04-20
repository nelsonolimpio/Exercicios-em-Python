'''Faça um programa que leia 5 valores numéricos e guarda-os em uma lista. No final mostre qual foi o maior e o menor valor digitado
e as respectivas posições da lista.'''

valores = list()
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
valores.sort()
print('=~'*30)
print('Valores digitados listados e crescentemente ordenados')
print(valores)
print('=~'*30)
print(f"o menor número da lista é: {valores[0]}")
print('**'*30)
print(f"o maior número digitado é: {valores[4]}")
print('**'*30)

