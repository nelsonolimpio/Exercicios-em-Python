'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavra = (str(input("1 palavra: ")), str(input("2 palavra: ")), str(input("3 palavra: ")), str(input("4 palavra: ")), str(input("5 palavra: ")))

for c in palavra:
    print(f'Palavra {c.upper()}')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print(f'vogais: {palavra.count()}')
    print('\n')