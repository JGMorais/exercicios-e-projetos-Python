p = str(input('Digite uma expressão: '))
pilha = []
for simb in p:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta VALIDA!')
else:
    print('Sua expressão esta ERRADA!')