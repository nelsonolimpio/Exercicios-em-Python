'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

l1 = [[], []]
for c in range(0, 7):
    l2 = int(input("Digite um valor numérico: "))
    if l2 % 2 == 0:
        l1[0].append(l2)
    else:
        l1[1].append(l2)
l1[0].sort()
l1[1].sort()
print('~='*30)
print('Lista unificada')
print(l1)
print('~='*30)
print(f'Números pares digitados em ordem crescente: {l1[0]}.')
print(f'Números ímpares digitados em ondem crescente: {l1[1]}.')
print('~='*30)