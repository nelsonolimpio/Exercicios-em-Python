'''Crie um programa que tenha uma tubpla totalmente preenchida com contagem por extensão, de zero até vinte.
  Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. '''
contagem = ("zero",'um','dois','três','quatro','cinco','seis','sete','oito','nova','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n = int(input("Digite um número de 0 até 20: "))
if n > 20 or n < 0:
    print("Tente novamente!")
print(contagem[n])