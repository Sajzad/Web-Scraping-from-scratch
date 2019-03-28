import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.ycombinator.com/news")
source = response.content

soup = BeautifulSoup(source, "lxml")

tds = soup.find_all("td", {"class":"title"})

for link in tds:
    a_tags = link.find_all("a", {"class":"storylink"})
    for span_tag in tds:
        span_tags = span_tag.find_all("span", {"class":"score"})
        print(span_tags)
    print(a_tags)

# print(len(link["href"]))
# print(len(link.text))
