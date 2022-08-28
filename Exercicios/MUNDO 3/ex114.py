import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.linkedin.com/in/caio-carv/')
except urllib.error.URLError:
    print('\033[1;92mO perfil do Caio no Linkedin está no ar\033[m')
else:
    print('\033[1;91mO perfil do Caio no Linkedin está fora do ar\033[m')
