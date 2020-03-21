import requests
import json

from bs4 import BeautifulSoup
from textwrap import dedent

from cookie import headers
from urls import users_url


def parser_sova(headers, users_url):
    response = requests.get(users_url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
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
            print('')
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
    # pass
    parser_sova(headers, users_url)
    # json_add()
