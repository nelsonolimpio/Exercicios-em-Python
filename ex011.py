'''Faça um programa que leia a largura e a altura de uma parede em metros. Calcule sua área e a quantidade
de tinta necessária para pintá-la. Sabendo que cada litro de tinta pinta uma área de 2m².'''

lar = float(input("Digite a largura:"))
alt = float(input("Digite a altura:"))

print("área: {}".format(lar*alt))
print("Será usada {} latas de tintas.".format((lar*alt)/2))
