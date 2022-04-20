'''Faça um programa que leia ano de nascimento de um jovem e informa de acordo com a sua idade:
- se ele ainda vai se alistar no serviço militar
- se é a hora de se alistar
- se já passou do tempo do alistamento.
Seu programa também deve mostrar o tempo que falta ou que passou do prazo.'''

ano = int(input("Em que ano você nasceu? "))
ano1 = 2021 - ano
passou = ano1 - 18
falta = 18 - ano1

print("Você tem {} anos de idade.".format(ano1))
if ano1 > 18:
    print("O tempo do alistamenteo já passou faz {} anos.".format(passou))
elif ano1 < 18:
    print("Faltam {} anos para se alistar.".format(falta))
elif ano1 == 18:
    print("É hora de se alistar.")
