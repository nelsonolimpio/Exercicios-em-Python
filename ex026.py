'''Faça um programa que leia uma frase pelo teclado e mostre:
- quantas vezes aparece a letra "A".
- Em que posição ela aprece pela 1° vez.
- Em que posição ela aparece pela ultima vez'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase.'.format(frase.count("A")))
print('A letra "A" aparece pela primeira vez na posição {}, e pela ultima vez na posição {}.'.format(frase.find('A')+1, frase.rfind('A')+1))
