import requests
from bs4 import BeautifulSoup

base_url = "http://bruneiproperty.com.bn/directory/103/"
response = requests.get(base_url+"?page=5")

source = response.content
soup =BeautifulSoup(source, "lxml")
ul_tag = soup.find('ul',{'class':'directory-list'})
all_div = ul_tag.find_all('div',{'class':'text'})
faxs = []
for div in all_div:
	title = ""
	description = ""
	tel= ""
	fax = ""
	email = ""
	web = ""
	title = div.find('h2').text
	description = div.find_all('p')
	for p_tag in description:
		description = p_tag.text
	all_dd = div.dl.find_all('dd')
	try:
		addresses = all_dd[0].text
	except:
		pass
	try:
		tel = all_dd[1].text
	except:
		pass
	try:
		fax = all_dd[2].text
	except:
		pass
	faxs.append(fax)

print(faxs)
	# try:
	# 	email = all_dd[3].text
	# except:
	# 	continue
	# try:
	# 	web = all_dd[4].text
	# except:
	# 	continue

