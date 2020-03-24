import requests
import json
import csv

from bs4 import BeautifulSoup
from textwrap import dedent

from cookie import headers
from urls import users_url


def parser_sova(headers, users_url):
    for all_page_parser in users_url:
        all_page = all_page_parser
        response = requests.get(all_page, headers=headers)
        response.raise_for_status(),
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
            print('Next page ------------------------------------------------------------------------- Next page')


if __name__ == '__main__':
    parser_sova(headers, users_url)
