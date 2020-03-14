import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

headers = {
    'cookie': 'SOVASESSION_ID=6qg9lf2m1na0s958p6pqom51tu'
}

page = 'http://vk-sova.3w.kz/users'


def parser_sova(headers, page):
    session = requests.Session()
    request = session.get(page, headers=headers)
    if request.status_code == 200:
        #soup = BeautifulSoup(page, 'html.parser')
        soup = BeautifulSoup(request.content, 'html.parser')
        a = soup.select('title')
        print(a)
    else:
        print('error')


parser_sova(headers, page)
