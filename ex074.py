'''Crie um programa que vai gerar cinco números aleatórios e colcoar em uma tupla.
Depois disso mostre a listagem de números gerados e também indiquem o menor e o maior valor que estão na tupla. '''

from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteados foram:{num}')
print('=-' * 20)
print(f'O maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
print('=-' * 20)

