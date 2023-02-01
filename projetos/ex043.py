peso = float(input('Qual é o seu peso?'))
altura = float(input('Qual é a sua altura?'))
imc = peso / (altura ** 2)
if imc < 17:
    print('Seu IMC é {:.2f} classificação "Muito abaixo do peso"!'.format(imc))
elif 17 <= imc <= 18.49:
    print('Seu IMC é {:.2f} classificação "Abaixo do peso"!'.format(imc))
elif 18.5 <= imc <= 24.99:
    print('Seu IMC é {:.2f} classificação "Peso normal!"'.format(imc))
elif 25 <= imc <= 29.99:
    print('Seu IMC é {:.2f} classificação "Acima do peso"!'.format(imc))
elif 30 <= imc <= 34.99:
    print('Seu IMC é {:.2f} classificação "Obesidade 1"!'.format(imc))
elif 35 <= imc <= 39.99:
    print('Seu IMC é {:.2f} classificação "Obesidade 2"!'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f} classificação "Obesidade 3"!'.format(imc))