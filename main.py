import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.jobstreet.co.id/id/job-search/laravel-developer-jobs-in-bogor/'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
}


res = requests.get(url, headers=headers)

def Get_Sallary():
    url = 'https://www.jobstreet.co.id/id/job-search/laravel-developer-jobs-in-bogor/'

    res = requests.get(url, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    soup = BeautifulSoup(res.text, 'html.parser')
    result = soup.find('div', 'sx2jih0 zcydq8n lmSnC_0')
    sallary = result.find_all('span', 'sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc3 _18qlyvc7')[1].text
    print(sallary)


if __name__ == '__main__':
    Get_Sallary()