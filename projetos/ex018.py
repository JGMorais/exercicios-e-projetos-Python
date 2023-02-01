import math
an = float(input('Digite o angulo: '))
se = math.sin(math.radians(an))
print('O angulo de {} tem o seno de {:.2f}'.format(an, se))
co = math.cos(math.radians(an))
print('O angulo de {} tem o cosseno de {:.2f}'.format(an, co))
ta = math.tan(math.radians(an))
print('O angulo de {} tem a tangente de {:.2f}'.format(an, ta))
