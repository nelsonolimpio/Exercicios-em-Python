'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto'''

sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
#A cima declaramos uma variável, que pede para o usuário informar o sexo dele (M ou F) ...
#Stripo = Elimina os espaços e pega somente a primeira letra da escrita // .upper() = Todas as letras ficam maiúsculas.
while sexo not in 'MF':
    #Enquanto sexo não for M ou F:
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo [M/F]:")).strip().upper()[0]
    #Sexo vai ser igual uma String digitada pelo usuário
print("Sexo {} registrado com sucesso".format(sexo))
#e quando o sexo for igual a M ou F, vai imprimir a frase a cima.