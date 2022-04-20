'''Melhore o desafio 061, preguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.'''

print("GERADOR DE PA")
print("*-" * 10)
primeiro = int(input("Primeiro termo: "))
razão = int (input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo), end='')
        termo = termo + razão
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você mostrar a mais? "))

print("Progressão finalizada com {} termos mostrados.".format(total))