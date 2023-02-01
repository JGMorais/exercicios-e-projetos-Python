import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com.br')
except urllib.error.URLError:
    print('O Site não está acessível no momento')
else:
    print('Consegui abrir o site com sucesso!')