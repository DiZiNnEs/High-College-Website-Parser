import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from textwrap import dedent

headers = {
    'cookie': 'SOVASESSION_ID=aoqf02h693q3502fivesag6li1'
}

page = f'http://vk-sova.3w.kz/users/'


def parser_sova(headers, page):
    session = requests.Session()
    request = session.get(page, headers=headers)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        for users in soup.find_all('tr'):
            name = users.select_one(':nth-child(3) a')
            ip = users.select_one(':nth-child(4) span')
            ip2 = users.select_one(':nth-child(5) span')
            first_ip = ip['title'] if ip is not None else None
            second_ip = ip2['title'] if ip2 is not None else None
            print(dedent(f'''\
            --------------------------------------------------
                Full name : {name.contents}
                IP from the last entry point: {first_ip}
                IP from the place of registration: {second_ip}
            --------------------------------------------------
            '''))

    else:
        print('error')

print(page)
parser_sova(headers, page)
