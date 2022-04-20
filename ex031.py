'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
R$0,50 por km para viagens de até 200Km e R$0,45 para viagens mais longas.'''

DViagem = float(input("Qual a distância da viagem? "))
if DViagem <= 200:
    VViagem = DViagem * 0.50
    print("Valor da viagem: R${:.2f}".format(VViagem))
else:
    VViagem = DViagem * 0.45
    print("Valor da viagem: R${:.2f}".format(VViagem))
