import re
from bs4 import BeautifulSoup
import requests
from bs4 import SoupStrainer
import csv

def link_generator(area):
	link = 'https://www.zomato.com/kolkata/'
	words = area.split()
	ctr = 0
	for word in words:
		w = word.lower()
		if ctr == 0:
			link = link + w
		else:
			link = link + '-' + w
		ctr = ctr + 1
	link = link + '-restaurants?all=1&nearby=0&page='
	return link

def extract_link(url):
	"""
	Creates a BeautifulSoup object from the link
	:param url: the link
	:return: a BeautifulSoup object equivalent of the url
	"""
	headers = {"Host": "www.zomato.com",
	       "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0",
	       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	       "Accept-Language": "en-US,en;q=0.5",
	       "Accept-Encoding": "gzip, deflate, br",
	       "Referer": "https://www.zomato.com/",
	       "Connection": "keep-alive"}

	r = requests.get(url, headers=headers)
	if r.status_code == 404:
		return None
	page_source = r.text

	page_source = re.sub('<br>', '', page_source)
	page_source = re.sub('<br />', '', page_source)
	page_source = re.sub('<br/>', '', page_source)
	soup = BeautifulSoup(page_source, 'html.parser')

	return soup
	
def get_data(link,file_name):
	seen = set()
	for ctr in range(1,5000):
		ulink = link_generator(link)
		mylink = ulink + str(ctr)
		print(mylink)
		soup = extract_link(mylink)
		restaurant_cards_name = soup.find_all('div', class_=re.compile('card search-snippet-card'))
		restaurant_cards_id = soup.find_all('div', class_=re.compile('js-search-result-li even status 1'))
		spamWriter = csv.writer(open(file_name, 'a'))
		
		for rcname,rcid in zip(restaurant_cards_name,restaurant_cards_id):
			item = rcname.find('a', class_=re.compile('item'))
			rid = rcid.get('data-res_id')
			name = item.get('data-res-name')
			pair = (name,rid)
			print (pair)	
			if pair in seen:
				return
			spamWriter.writerow([name,rid,link])
			seen.add(pair)
	

#Sub-locations within each major locations


north_kolkata = ['Bara Bazar','Baranagar','Barrackpore','Belghoria','Bow Bazar','College Street','Girish Park','Hatibagan','Khardah','Machuabazar','Maniktala','Paikpara','Sealdah Area','Shobha Bazar','Shyam Bazar','Sinthi','Sodepur']

#removed Sarat Bose Road as no data for it on website
south_kolkata = ['Ajoy Nagar','Alipore','Baghajatin','Ballygunge','Bhawanipur','Desapriya Park','Dhakuria','Elgin','Garia','Gariahat','Golf Green','Golpark','Hazra','Hindustan Park','Jadavpur','Jodhpur Park','Kalighat','Kalikapur','Kasba','Lake Gardens','Lake Market Area','Naktala','Narendra Pur','New Alipore','Paddapukur','Picnic Garden','Prince Anwar Shah Road','Ruby Hospital Area','Santoshpur','Southern Avenue','Tollygunge']

east_kolkata = ['Baguihati','Bangur','Barasat','Beliaghata','Dum Dum','Kaikhali','Kalindi','Kankurgachi','Kestopur','Lake Town','Nagerbazar','Rajarhat','New Town','Science City Area','Sector 4 Salt Lake','Tangra','Topsia','Ultadanga']

west_kolkata = ['Behala','Falta','Joka','Kidderpore','Tara Tala','Thakur Pukur']

central_kolkata = ['Camac Street Area','Chandni Chowk','Chowringhee','Dalhousie BBD Bagh','Entally','Esplanade','Loudon Street Area','Minto Park','New Market Area','Park Circus Area','Park Street Area','Taltala','Theatre Road','Wellesley']


salt_lake = ['Sector 1 Salt Lake','Sector 2 Salt Lake','Sector 3 Salt Lake','Sector 5 Salt Lake']

rajarhat = ['Chinar Park','New Town']

howrah = ['Andul Road','Bally','Belur','Dobson Road','GT Road','Howrah Maidan Area','Howrah Station Area','Ichapur','Kadamtala','Kona Exp Way','Liluah','Salkia','Shalimar','Shibpur']


hooghly = ['Hindmotor','Konnagar','Rishra','Shrirampur','Uttarpara']

arr = [north_kolkata,south_kolkata,east_kolkata,central_kolkata,salt_lake,rajarhat,howrah,hooghly]

file_name = "location_data.csv"
for loc in arr:
	for sub_loc in loc:
		print(sub_loc)
		get_data(sub_loc,file_name)
		

