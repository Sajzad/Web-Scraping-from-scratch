import requests
from bs4 import BeautifulSoup
import csv


response = requests.get("https://news.ycombinator.com/news")
src = response.content
csv_file = open("ycombinator.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["title", "links", "scores", "hn_links"])
soup = BeautifulSoup(src, "lxml")

tr_tags = soup.find_all("tr")
titles = ""
links = ""
scores = ""
hn_links = ""

for tr in tr_tags:

	tds = tr.find_all("td", {"class", "title"})
	if tds:
		for td in tds:
			if td.find("a", {"class":"storylink"}):
				titles = td.find("a", {"class":"storylink"}).text
				links = td.find("a", {"class":"storylink"})["href"]
				print(titles, links)

	td = tr.find("td",{"class", "subtext"})
	# HN links
	if td:
		hn_links= td.find_all("a")[-1]["href"]
		print(hn_links)
		print("https://news.ycombinator.com/",hn_links)
		if td:
			if td.find("span"):
				scores= td.find("span").text.replace("points","")
				print(scores)


	csv_writer.writerow([titles, links, scores, hn_links])
print(len(titles))
csv_file.close()
