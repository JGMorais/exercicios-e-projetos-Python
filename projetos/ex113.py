def leiaint(msg):
   while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um numero inteiro valido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar o numero!\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
   while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um numero real valido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar o numero!\033[m')
            return 0
        else:
            return n


num = leiaint('Digite um numero inteiro: ')
n = leiafloat('Digite um numero real: ')
print(f'Voce digitou o numero {num} e {n}')
