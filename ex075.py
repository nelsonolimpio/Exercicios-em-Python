'''Desenvolva um programa que leia quatro valores pelo teclado e guarda-os em uma tubpla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''


val = (int(input("1 valor: ")), int(input("1 valor: ")), int(input("1 valor: ")), int(input("1 valor: ")))
print('*'*25)
print(f"O valor 9 apareceu {val.count(9)} vezes.")
if 3 in val:
    print('*'*25)
    print(f'O valor 3 aparece pela primeira vez na posição {val.index(3)}.')
    print('*'*25)
else:
    print('*'*25)
    print("O valor 3 não foi digitado.")
    print('*'*25)
for i in val:
    if i % 2 == 0:
        print(f'Os números pares foram {i}')
print('*'*25)
