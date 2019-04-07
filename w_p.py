import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


# csv_file = open('real_scarper_result.csv', 'w', encoding='utf-8')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow([""])
base_url = "http://bruneiproperty.com.bn/directory/103/"
output_file = "real_scarper_result.csv"
data = []

i=0
n=0
while i<=5:
	if i==0:
		response = requests.get(base_url)
	else:
		n+=1
		response = requests.get(base_url+"?page={}".format(n))
	i+=1

	source = response.text
	soup =BeautifulSoup(source, "lxml")
	ul_tag = soup.find("ul",{"class":"directory-list"})
	all_div = ul_tag.find_all('div',{'class':'text'})
	for div in all_div:

		company_name = ""
		addresses = ""
		descriptions = ""
		tel= ""
		fax = ""
		mail = ""
		web = ""

		company_name = div.find('h2').text
		description = div.find_all('p')
		for p_tag in description:
			descriptions = p_tag.text
		all_dd = div.dl.find_all('dd')
		all_dt = div.dl.find_all('dt')
		try:
			if all_dt[0].text=='Address':
				addresses = all_dd[0].text

		except:
			pass
		try:
			if all_dt[0].text=='Tel': 
				tel = all_dd[0].text
			elif all_dt[1].text=='Tel':
				tel = all_dd[1].text
		except:
			pass
		try:
			if all_dt[0].text == 'Fax':
				fax = all_dt[0].text
			elif all_dt[1].text =='Fax':
				fax = all_dd[1].text
			elif all_dt[2].text == 'Fax':
				fax = all_dd[2].text
		except:
			pass
		try:
			if all_dt[0].text == 'Email':
				mail = all_dd[0].a.text
			elif all_dt[1].text =='Email':
				mail = all_dd[1].a.text
			elif all_dt[2].text == 'Email':
				mail = all_dd[2].a.text
			elif all_dt[3].text == 'Email':
				mail = all_dd[3].a.text
		except:
			pass
		try:			
			if all_dt[0].text == 'Website':
				web = all_dd[0].a["href"]
			elif all_dt[1].text =='Website':
				web = all_dd[1].a["href"]
			elif all_dt[2].text == 'Website':
				web = all_dd[2].a["href"]
			elif all_dt[3].text == 'Website':
				web = all_dd[3].a["href"]
			elif all_dt[4].text == 'Website':
				web = all_dd[4].a["href"]
		except:
			pass
	
		data_dict = {

			"Company_name":company_name,
			"Descriptions": descriptions,
			"Address": addresses,
			"Tel": tel,
			"Fax": fax,
			"Email_Address" : mail,
			"Web": web
	
		}
		data.append(data_dict)
# print(data)

if data:
	df = pd.DataFrame(columns= ["Company_name", "Descriptions", "Address", "Tel", "Fax", "Email_Address", "Web"])
	df = df.append(data, ignore_index = True)
	df.to_csv(output_file, index= False)