'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início. pergunte ao usuário qual será o valor a ser sacado (número
inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10, R$1.'''

ced = 50
cedTotal = 0
print("Cédulas disponíveis R$50, R$20, R$10, R$1.")
sacar = int(input("Qual valor deseja sacar? R$"))

while True:
    if sacar >= ced:
        sacar -= ced
        cedTotal += 1
    else:
        if cedTotal != 0:
            print(f'Total de {cedTotal} de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cedTotal = 0
        if sacar == 0:
            break



