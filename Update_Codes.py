import requests
from bs4 import BeautifulSoup

def update_bus_codes(url=''):
	
	#https://www.iett.istanbul/tr/main/duraklar/225632/YEN%C4%B0SAHRA-%C4%B0ETT-Duraktan-Ge%C3%A7en-Hatlar-Durak-Bilgileri-Hatt%C4%B1n-Duraktan-Ge%C3%A7i%C5%9F-Saatleri
	response = requests.get(url)
	html_content = response.content
	soup = BeautifulSoup(html_content, "html.parser")
	buses = soup.find_all('mark')
	station_name = str(soup.find('span',{'class':'station-name'}).text) + ' '+ str(soup.find('span',{'class':'station-name-suffix'}).text)

	bus_codes = []

	for i in buses:
		bus_codes.append(i.text)
	
	with open('bus_codes.txt', 'w+') as f:
		f.write(station_name + '\n')
		f.write(str(bus_codes))

	return True
