'''Refaça o desafion 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

tabuada = int(input("Tabuada do número:"))

for count in range(10):
    print("{} X {} = {}".format(tabuada, count+1, tabuada * (count+1)))