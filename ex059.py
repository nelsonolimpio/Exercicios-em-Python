'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] Soma
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do Programa
seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
#Importante sleep da biblioteca time.
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
#Dando valor as variáveis n1 & n2.
opc = 0
#opc vai iniciar do 0.
while opc != 5:
#Enquanto opc for diferente de 5, o programa roda.
    print('''             ---------------------------
              ********* MENU **********
              [1] Soma
              [2] Multiplicar.
              [3] Qual o Maior número.
              [4] Novos número.
              [5] Sair do Programa.
             ---------------------------''')
    opc = int(input("QUal é a sua opção? "))
    #Atribuindo valor a variável opc, através do usuário.
    if opc == 1:
        soma = n1 + n2
        print("{} + {} = {}".format(n1, n2, soma))
        #Se opc for igual a 1, a variavel soma vai ser n1 + n2. E vamos imprimir a frase a cima.
    elif opc == 2:
        mult = n1 * n2
        print("{} * {} = {}".format(n1, n2, mult))
        #Se opc for igual a 2 multiplicação de n1 * n2.
    elif opc == 3:
        if n1 > n2:
            print("{} maior que {}.".format(n1, n2))
        else:
            print("{} maior que {}.".format(n2, n1))
        # Se opc for igual a 3, ele vai descobrir qual o número maior.
    elif opc == 4:
        print("Informe os números novamente.")
        n1 = int(input("Primeiro valor: "))
        n2 =  int(input("Segundo valor: "))
        #Se opção for igual a 4 ele vai pedir novamente os valores, para que possa ser modificados.
    elif opc == 5:
        print("Finalizando...")
        #Opção 5 finaliza o programa.
    else:
        print("Opção inválida. Tente novamente.")
    print("=-=" * 10)
    sleep(2)
    #Sleep (2), ele pede 2 segundo de espera antes de partir para a proxima linha.
print("Fim do programa! Volte sempre")

