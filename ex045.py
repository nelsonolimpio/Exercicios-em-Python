'''Crie um programa que faça o computador jogar jokempô com você.'''
from random import choice

pedra = ("p")
papel = ("PA")
tesoura = ("T")

SuaEscolha = str(input("Você escolhe Pedra(P), Papel(PA) ou Tesoura(T)? ").upper())
print("Você escolheu: {}".format(SuaEscolha))
lista = [pedra, papel, tesoura]
escolhido = choice(lista)
print("Computador escolheu: {}".format(escolhido))

if SuaEscolha == escolhido:
    print("Empate.")
elif (SuaEscolha == "P" and escolhido == "PA") or (SuaEscolha == 'T' and escolhido == 'P') or (SuaEscolha == "PA" and escolhido == "T"):
    print("Você perdeu.")
elif (escolhido == "P" and SuaEscolha == 'PA') or (escolhido == 'T' and SuaEscolha == 'P') or (escolhido == 'PA' and SuaEscolha == 'T'):
    print ("Parabens! Você ganhou.")
