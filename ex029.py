'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi
multado. A multa vai custar R$7,00 por cada km acima do limite.'''

vel = float(input("Velocidade do carro (km/h):"))
ValorMulta = (vel-80)*7
if vel > 80:
    print("Você foi multado!")
    print("Valor total da multa é de R${:.2f}".format(ValorMulta))
else:
    print("Ok, você estava de acordo com a velocidade!")