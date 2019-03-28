import requests
from bs4 import BeautifulSoup
import csv


response = requests.get('https://news.ycombinator.com/news')

source = response.content
csv_file = open('hn_link.csv', 'w')
csv_wirter = csv.writer(csv_file)
soup = BeautifulSoup(source, 'lxml')
csv_wirter.writerow(["hn_link"])

tds= soup.find_all('td', {'class':'subtext'})
for a_tag in tds:
	links= a_tag.find_all('a')
	for link in links:
		if "comments" in link.text:
			hn_links = link
			print(hn_links)
		
	csv_wirter.writerow([hn_links])
	break

csv_file.close()
