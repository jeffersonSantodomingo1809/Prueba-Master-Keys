from urllib.parse import urlparse
def extraer_dominio(url):
    parsed_url = urlparse(url)
    dominio = parsed_url.netloc
    return dominio
import re
def eliminar_www(url):
    patron = r'(https?://)?(www\.)?(.*)'
    dominio = re.sub(patron, r'\3', url)     
    # Utilizamos la función re.sub para reemplazar el patrón encontrado por el primer grupo y el tercer grupo
    # El tercer grupo (\3) corresponde al resto de la URL sin el prefijo "www"
    return dominio
# Lista de URLs
dato= input("Ingrese link para identificar el nombre de dominio: ")
urls= []
for i in dato:
    urls.append(i)
url = ''.join(urls)
dominio = extraer_dominio(url)
Dominios = eliminar_www(dominio)
print(Dominios)
#https://admisiones.unimagdalena.edu.co/mEstudiantes/indexPrinc.jsp?0.8028655747247073=280.1217420417459 http://deletesql.com/viewtopic.php?f=5&t=10 https://www.debian.org/distrib/ftplist
