'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados
respectivamentes. Ao final, mostre o conteúdo das três listas geradas.'''

valor = list()
pares = list()
impares = list()
while True:
    valor.append(int(input("Digite um valor: ")))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Continuar [S/N]? ")).upper()
    if continuar in 'N':
        break
print("=~"*25)
print(f'Lista completa: {valor}.')
for num in valor:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("=~" * 25)
print(f'Lista de pares: {pares}.')
print("=~"*25)
print(f'Lista de impares: {impares}')
print("=~"*25)