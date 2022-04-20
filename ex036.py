'''Escreva um programa para aprovar empréstimo bancário para a compra de uma casa. O progama vai perguntar
o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação
mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

vcasa = float(input("Qual o valor da casa?"))
sal = float(input("Qual o seu salário?"))
pag = int(input("Quantos anos pretende pagar?"))
excesso =  (30/100)*sal
PAnual = vcasa/pag
PMensal = PAnual/12


print("Prestação anual: R${}".format(PAnual))
print("Prestação mensal: R${}".format(PMensal))

if PMensal > excesso:
    print("O empréstimo foi negado. A prestação mensal excede 30% do salário.")

else:
    print("Parabéns, o seu empréstimo foi aprovado.")

