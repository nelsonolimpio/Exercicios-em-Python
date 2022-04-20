'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados em ordem crescente.'''

numeros=[]

while True:
    numeros.append(int(input('Digite um número: ')))
    condicao = str(input('Deseja continuar? [S/N}? ')).upper()

    if condicao == 'N':
        numeros.sort()
        unicos = list(set(numeros))
        #O comando  list(set(lista))  faz com que os números repetidos digitados não se repitam.
        print(f'Os números digitados foram {unicos}')
        break

    elif condicao != 'S':
    # Como faço para fazer o usuário retornar a "condicao" SIM ou NÃO?
        print('Essa opção não existe. Tente de novo.')