import requests
import json

from bs4 import BeautifulSoup
from textwrap import dedent

from cookie import headers

page = f'http://vk-sova.3w.kz/users/'


def parser_sova(headers, page):
    session = requests.Session()
    request = session.get(page, headers=headers)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        for users in soup.find_all('tr'):
            try:
                name = users.select_one(':nth-child(3) a')
                ip = users.select_one(':nth-child(4) span')
                date_time = users.select_one(':nth-child(4) span').text
                first_ip = ip['title'] if ip is not None else None
                print(dedent(f'''\
                --------------------------------------------------
                    Full name : {name.string}
                    IP from the last entry point: {first_ip}
                    Last login date: {date_time}
                --------------------------------------------------
                '''))
            except:
                pass
    else:
        print('Some mistake :3')


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
    parser_sova(headers, page)
    # json_add()
