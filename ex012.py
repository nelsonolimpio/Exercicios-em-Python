'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto'''

valor = float(input('Digite o valor do produto:'))

print("Valor com desconto: {}".format((valor - ((5/100*valor)))))
