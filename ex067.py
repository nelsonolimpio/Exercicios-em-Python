'''Faça um programa que mostre a tabuada de vários números, um de cada vez, paras cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

print(10*"~=")
print("      TABUADA     ")
print(10*"~=")
while True:
    t = int(input("Digite o número em que deseja a tabuada: "))
    if t < 0:
        break
    d = 1
    while d <= 10:
        print(f"{t} X {d} = {t*d}")
        d += 1
print(10*"~=")
print("        FIM     ")
print(10*"~=")

