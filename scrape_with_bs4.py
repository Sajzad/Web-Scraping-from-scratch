import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.practicalecommerce.com/category/amazon-marketplaces')

source= response.content

soup = BeautifulSoup(source, 'lxml')

lists = soup.find_all("li", {"class":"postlist"})
for list in lists:
    print(list.find("h2").text)
    print(list.find("a").get("href"))
