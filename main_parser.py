import requests
import json

from bs4 import BeautifulSoup

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

                for to_json in name, date_time, first_ip:
                    persons = {
                        "user": {
                            "name:": to_json.string,
                            "IP from the last entry point": first_ip,
                            "Last login date": date_time
                        }
                    }

                    with open('users.json', 'a') as json_file:
                        json.dump(persons, json_file, indent=5, ensure_ascii=False, sort_keys=True)

            except:
                print('')
        else:
            print('Next page ------------------------------------------------------------------------- Next page')


if __name__ == '__main__':
    parser_sova(headers, users_url)
