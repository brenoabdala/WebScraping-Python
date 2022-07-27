# Bibliotecas instalação
# pip install requests
# pip install bs4
# pip install pandas

# Importando biblioteca
import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')

# Verificando o código de requisição
# 200 - Funcional
# print(response.status_code)

content = response.content

# Conversão para HTML
site = BeautifulSoup(content, 'html.parser')

# HTML da noticia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

# print(noticia.prettify())

for noticia in noticias:
    # Titulo da Noticia
    titulo = noticia.find('a', attrs={'class', 'feed-post-link'})
    print(titulo.text)

    # Subtitulo da noticia
    subtitulo = noticia.find('a', attrs={'class', 'feed-post-body-resumo'})

    if (subtitulo):
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])

news.to_csv('noticias.csv', index=False)
