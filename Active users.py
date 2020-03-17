import requests
import json

from bs4 import BeautifulSoup
from textwrap import dedent

from cookie import headers


page = 'http://vk-sova.3w.kz/users/index?sort_key=lastlogin&t=d'

def parser_sova_pages(headers, page):
    session = requests.Session()
    request = session.get(page, headers=headers)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        for pages in soup.find_all('ul', attrs={'class': 'pages'}):
            for a in pages.find_all('a'):
                b = a['href']
                print(dedent(f'''\
                Number page: {a.string}, link = {b}
                '''))

def parser_sova(headers, page):
    #session = requests.Session()
    request = requests.get(page, headers=headers)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        for users in soup.find_all('tr'):
            try:
                date_time = users.select_one(':nth-child(4) span').text
                name = users.select_one(':nth-child(3) a')
                ip = users.select_one(':nth-child(4) span')
                first_ip = ip['title'] if ip is not None else None
                print(dedent(f'''\
                --------------------------------------------------
                    Full name : {name.string}
                    Date / Time entry: {date_time}
                    IP from the last entry point: {first_ip}
                --------------------------------------------------
                '''))
            except:
                print('Some mistake :3')
    else:
        print('error')


# def json_add():
#     name = parser_sova(headers, page)
#     first_ip = parser_sova(headers, page)
#     a = [name, first_ip]
#     persons = {"Full name": name,
#                "IP from the last entry point": first_ip,
#                }
#     with open('users.json', 'w') as file:
#         json.dump(persons, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    parser_sova_pages(headers, page)
    parser_sova(headers, page)
    # json_add()
