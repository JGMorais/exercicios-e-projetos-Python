n = c = s = 0
while True:
    n = int(input('Digite um numero ou [999] para parar: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Voce digitou {c} numeros e a soma entre eles foi {s}.')