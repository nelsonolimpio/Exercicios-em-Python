'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre seu status, de acordo com a tabela abaixo.
- menos de 18.5: Abaixo do peso.
- entre 18.5 e 25: Peso ideal.
- de 25 até 30: SobrePeso.
- de 30 até 40: Obesidade.
- mais de 40: Obesidade Mórbida.'''

alt = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
imc = peso/(alt**2)

print("IMC = {}".format(imc))

if imc < 18.5:
    print("Abaixo do peso.")
elif imc > 18.5 and imc < 25:
    print("Peso ideal.")
elif imc > 25 and imc < 30:
    print("Sobrepeso.")
elif imc > 30 and imc < 40:
    print ("Obesidade.")
else:
    print("Obesidade mórbida.")