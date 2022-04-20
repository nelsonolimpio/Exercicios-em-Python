'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses
abertos e fechados na ordem correta.'''

algebra = list()
expressao = str(input("Digite uma expressão algébrica com parênteses: "))
if "(" in expressao and ")" in expressao:
    algebra.append(expressao)
    print(f'A sua expressão {algebra} está correta!')
else:
    print(f'Sua expressão está incorreta, verifique os parênteses da álgebra.')