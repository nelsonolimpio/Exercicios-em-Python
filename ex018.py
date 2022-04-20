import math
angulo = float(input("Digite um ângulo:"))
seno = math.sin(math.radians(angulo))
print('o angulo de {} ten o SENO de {:.2f}'.format(angulo, seno))
cos = math.cos(math.radians(angulo))
print('o angulo de {} tem o cosseno de {:.2f}'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('o angulo de {} tem a tangente de {:.2f}'.format(angulo, tan))