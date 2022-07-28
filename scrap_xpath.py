
from bs4 import BeautifulSoup
from lxml import etree
import requests
  
  
URL = "https://www.jobstreet.co.id/id/job-search/laravel-jobs-in-bandung/"
  
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
  
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "html.parser")
dom = etree.HTML(str(soup))
print(dom.xpath('//*[@id="jobList"]/div[2]/div[2]/div/div[1]/div/div/article/div/div/div[1]/div[1]/div[2]/span')[0].text)