'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
- até 9 anos: Mirim
- até 14 anos: Infantil
- até 19 anos: Júnior
- até 20 anos: Sênior
- acima: Master.'''

nasc = int(input("Digite o ano de nascimento do aluno: "))
idade = 2021 - nasc

print("Idade do aluno: {}".format(idade))

if idade <= 9:
    print("Categoria: Mirim.")
elif idade > 9 and idade <= 14:
    print("Categoria: Infantil.")
elif idade > 14 and idade <= 19:
    print("Categoria: Júnior.")
elif idade == 20:
    print("Categoria: Sênior.")
else:
    print("Categoria: Master.")
