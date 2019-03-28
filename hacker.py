from bs4 import BeautifulSoup
import requests


respose = requests.get("https://news.ycombinator.com/")

source = respose.content

soup = BeautifulSoup(source, "lxml")
table = soup.find_all("table", {"class":"itemlist"})
# tds = table.find_all("td", {"class": "title"})

for td in table:

	tds = td.find_all("td", {"class": "subtext"})
	for a in tds:
		all= a.find_all("a")
		print(all[-1])
	# if "comments" in tds:
		
	# for a in tds:
		# all_a = a.find_all("a")
		# print(all_a[2])
# print(len(all_a))