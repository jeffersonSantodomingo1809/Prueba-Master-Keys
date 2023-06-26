import re
def Dominios(html_fragmentos):
    urls = re.findall(r'https?://(?:www\.)?([\w.-]+)', html_fragmentos)
    Dominios = set()
    for url in urls:
        Orden= url.split('.')
        if len(Orden) >= 2:
            Dominios.add('.'.join(Orden[-2:]))
    print(urls)
    sorted_domains = sorted(Dominios)
    return ' ; '.join(sorted_domains)
num = input("Ingrese link para identificar el nombre de dominio: ")
html_lineas = []
print(num)
for i in num:
    html_lineas.append(i)
html_fragmentos = ''.join(html_lineas)
Lista_Dominios = Dominios(html_fragmentos)
#https://youtu.be/ARWg160eaX4 https://youtu.abc.be/ARWg160eaX4 https://youtu.abcd.be/ARWg160eaX4?t=125
#https://admisiones.unimagdalena.edu.co/mEstudiantes/indexPrinc.jsp?0.8028655747247073=280.1217420417459 http://deletesql.com/viewtopic.php?f=5&t=10 https://www.debian.org/distrib/ftplist