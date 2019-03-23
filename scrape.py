from bs4 import BeautifulSoup
import requests


r=requests.get('https://www.whitehouse.gov/presidential-actions/')
# print(r.status_code)
# print(r.headers)
src=r.content
# print(src)
s=BeautifulSoup(src, 'lxml')
# link = s.find_all('a')
# print(link)
# print('/n')
# urls=[]
# for h2 in s.find_all('h2'):
#     a=h2.find("a")
#     a=a.attrs['href']
#     urls.append(a)
#
# print(urls)
# urls=[]

s= BeautifulSoup(src, 'lxml')
urls=[]

for list in s.find_all('li'):
    print(list.a.attrs['href'])
