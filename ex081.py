'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenadas de forma decrescente.
C) Se o valor 5 foi digitado e está ou não está na lista.'''

valores = list()
while True:
    valores.append(int(input("Digite um valor: ")))
    cond = str(input("Deseja Continuar [S/N]? ")).upper()

    if cond == "N":
        valores.sort(reverse=True)
        print(f"Foram digitados {len(valores)} valores.")
        print(f"Lista de valores ordenadas de forma descrescente: {valores}")
        if 5 in valores:
            print("O valor 5 foi digitado e está na lista.")
        else:
            print("O valor 5 não foi digitado e não está na lista")
        break



