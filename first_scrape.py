import requests
from bs4 import BeautifulSoup


response = requests.get('https://news.ycombinator.com/news')
src = response.content

soup = BeautifulSoup(src, 'lxml')


trs = soup.find_all("tr")

for tr in trs:
	tds = tr.find_all( "td", {"class":"title"})
	if tds:
		for td in tds:
			
			if td.find("a"):
				print(td.find("a").text, td.find("a").attrs.get("href"))
	td = tr.find("td", {"class":"subtext"})
	if td:
		if td.find("span"):
			print(td.find("span").text.replace(" points", ""))		