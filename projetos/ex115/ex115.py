from lib.arquivo import *
from lib.interface import *
from time import sleep

arq = 'cursoemvideo.txt'



while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteudo do arquivo!
        cabecalho('1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até Logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção Válida!\033[m')
        sleep(2)