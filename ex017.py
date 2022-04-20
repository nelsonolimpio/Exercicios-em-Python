import math
co = float(input("Digite o cateto oposto:"))
ca = float(input("Digite o catato adjacente:"))
hip = math.hypot(co, ca)
print("Hipotenusa ={:.2f}".format(hip))

''' Fórmula para a questão é 
hipotenusa = (cateto adjacente ** 2 + cateto oposto ** 2) ** (1/2)'''

#:.2f dentro da chave quer dizer que vamos trará apenas dois números após a virgula no resultado.


