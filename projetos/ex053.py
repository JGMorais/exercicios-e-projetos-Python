frase = str(input('Digite uma frase: ')).strip().upper()
pal = frase.split()
jun = ''.join(pal)
inv = ''
for letra in range (len(jun) -1, -1, -1):
    inv += jun[letra]
print('O inverso de {} é {}'.format(jun, inv))
if inv == jun:
    print('temos um palíndromo!')
else:
    print('NÃO temos um palíndromo!')