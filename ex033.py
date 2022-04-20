'''Faça um programa que leia três números e moste qual é o maior e qual é o menor número.'''

a = int(input("1° número:"))
b = int(input("2° número:"))
c = int(input("3° número:"))
#Verificando quem é o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print("O menor valor executado foi {}".format(menor))
print("O maior valor executado foi {}".format(maior))


