'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida.
- Média abaixo de 5.0: reprovado.
- Média entre 5.0 e 6.9: recuperação.
- Média maior que 7.0: aprovado'''

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2)/2

print("Média: {}".format(media))

if media < 5.0:
    print("Aluno reprovado.")
elif media > 5.0 and media < 6.9:
    print("Aluno em recuperação.")
else:
    print("Aluno aprovado.")