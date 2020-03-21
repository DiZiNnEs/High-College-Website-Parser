import requests
import json

from bs4 import BeautifulSoup
from textwrap import dedent

from cookie import headers

page = 'http://vk-sova.3w.kz/users/index?sort_key=lastlogin&t=d'


def parser_sova_pages(headers, page):
    page_storage = []
    response = requests.get(page, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    for pages in soup.find_all('ul', attrs={'class': 'pages'}):
        for every_page in pages.find_all('a'):
            every_page_output = every_page['href']
            page_storage.append('http://vk-sova.3w.kz' + every_page_output)
            ready_page_storage = page_storage[:-1]
            # return ready_page_storage
        return page_storage


def last_users():
    list_ = parser_sova_pages(headers, page)
    for walk in page and list_:
        response = requests.get(walk, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
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
                print('')
        else:
            print('')


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
    last_users()
    # json_add()
