import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.ycombinator.com/")
src = response.text
soup = BeautifulSoup(src, "lxml")
table_tag = soup.find_all("table", {"class":"itemlist"})

for td in table_tag:
    tds = td.find_all("a", {"class":"storylink"})
    for a in tds:
        title = a.text
        links = a["href"]
        print(title, links)
        # print(t
