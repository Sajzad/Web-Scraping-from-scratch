import requests
from bs4 import BeautifulSoup

s=requests.get("https://www.dreamcatcherit.com/")

src=s.content

# print(src)

p= BeautifulSoup(src, 'lxml')

a=p.find_all('li')

for link in a:
    h=link.find('a')
    print(h.attrs['href'])

# urls=[]
#
# for link in a:
#     l=link.find('a').attrs['href']
#     urls.append(l)
# print(urls)
