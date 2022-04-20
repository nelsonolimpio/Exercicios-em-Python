'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com santo.'''

cidade = str(input("Digite uma cidade: ")).strip()
#print('Santo' in cidade)
print(cidade[:5].upper() == 'SANTO')