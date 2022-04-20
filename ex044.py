'''Elabore um programa que calcue o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- A vista dinheiro/cheque: 10% de desconto.
- A vista no cartão: 5% de desconto.
- Em até 2X no cartão: preço normal.
- 3X ou mais no cartão: 20% de juros.'''

vprod = float(input("Valor do produto: R$"))
fpag = str(input("Forma de pagamento (C = cartão /CH = cheque/D = Dinheiro): ").upper())

if fpag == ("C"):
    parcela = int(input("Em quantas vezes? "))
    if parcela == 2:
        print("Valor a pagar = R${}".format(vprod))
    elif parcela >= 3:
        juros = (20 / 100) * vprod
        vpag = vprod + juros
        print("Juros = R${}".format(juros))
        print("Total a pagar = R${}".format(vpag))
    elif parcela == 1:
        desc = (5 / 100) * vprod
        vpag = vprod - desc
        print("Desconto = R${}".format(desc))
        print("Valor a pagar = R${}".format(vpag))
elif fpag == ("D") or fpag == ("CH"):
    desc = (10 / 100) * vprod
    vpag = vprod - desc
    print("Desconto = R${}".format(desc))
    print("Valor a pagar = R${}".format(vpag))

## Abaixo -- Forma mais simplificada de fazer o exercício.
'''if fpag == ("A vista no dinheiro"):
    desc = (10/100)*vprod
    vpag = vprod - desc
    print("Desconto = R${}".format(desc))
    print("Valor a pagar = R${}".format(vpag))
elif fpag == ("A vista no cartão"):
    desc = (5/100)*vprod
    vpag = vprod - desc
    print("Desconto = R${}".format(desc))
    print("Valor a pagar = R${}".format(vpag))
elif fpag == ("2x no cartão"):
    print("Valor a pagar = R${}".format(vprod))
else:
    juros = (20/100)*vprod
    vpag = vprod + juros
    print("Juros = R${}".format(juros))
    print("Total a pagar = R${}".format(vpag))'''