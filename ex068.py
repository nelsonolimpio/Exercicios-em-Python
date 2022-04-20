'''Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecultivas que ele conquistou
no final do jogo. '''

from random import randint
cont = 0
while True:
    n = int(input('Digite o seu número: '))
    a = ' '
    while a not in "PI":
        a = str(input("Escolha par ou ímpar [P/I]:")).strip().upper()
    c = randint(0, 10)
    if (n + c) % 2 == 0:
        if a == 'P':
            print(f'Venceu. Você escolheu {n}, o computador escolheu {c}. E a soma deu {n + c}.')
        else:
            print(f'Perdeu. Você escolheu {n}, o computador escolheu {c}. E a soma deu {n + c}.')
            break
    if (n +c) % 2 != 0:
        if a == 'I':
            print(f'Venceu. Você escolheu {n}, o computador escolheu {c}. E a soma deu {n + c}.')
        else:
            print(f'Perdeu. Você escolheu {n}, o computador escolheu {c}. E a soma deu {n + c}.')
            break
    cont += 1
print(f'Você venceu {cont} vezes')
print('FIM')
