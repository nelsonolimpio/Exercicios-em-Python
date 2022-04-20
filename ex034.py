'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

sal = float(input("Digite o salário: "))
if sal > 1250:
    aumento = (10/100) * sal
    print("Aumento de: R${:.2f}".format(aumento))
else:
    aumento = (15/100) * sal
    print ("Aumento de: R${:.2f}".format(aumento))