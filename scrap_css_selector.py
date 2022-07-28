from bs4 import BeautifulSoup
import requests

URL = "https://www.jobstreet.co.id/id/job-search/laravel-jobs-in-bandung/"
  
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
  
webpage = requests.get(URL, headers=HEADERS)
# BeautifulSoup
soup = BeautifulSoup(webpage.content, 'html.parser')

# Find all by selector
els = soup.select('#jobList > div.sx2jih0.z0qC4_0 > div:nth-child(2) > div ')

el_list= str(els[0])#.text.split("/")

soup2 = BeautifulSoup(el_list,'html.parser')
elements = soup2.find_all("span")

list_baru = []

for element in elements:
    print(element.text)
    list_baru.append(element.text)