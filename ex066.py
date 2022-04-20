'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999. Que é a condição de parada. No final mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag).'''

n = s = q = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
    q += 1
print(f"Soma vale {s}")
print(f"foram digitados {q} números.")


