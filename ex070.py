'''Crie um programa que leia o nome e o preço de vários produtos. O produto deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) QUantos produtos custam mais de R#1000
C) Qual é o nome do produto mais barato. '''

cont = 0
s = 0
c1000 = 0
menor = 0
nome = ' '
while True:
    cont +=1
    p = float(input("Preço: "))
    n = str(input("Nome do produto: ")).strip().capitalize()
    s += p
    if p > 1000:
        c1000 += 1
    if cont == 1 or p < menor:
        menor = p
        nome = n
    c = ' '
    while c not in "SN":
        c = str(input("Quer continuar [S/N}? ")).strip().upper()
    if c == "N":
        break

print(f'Total gasto: {s}')
print(f'{c1000} produtos custam mais de R$1000,00')
print(f'O nome do produto mais barato é: {nome}')


