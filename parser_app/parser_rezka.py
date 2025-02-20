import requests
from bs4 import BeautifulSoup

URL = 'https://rezka.ag/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

#1 make response
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

#2 get data
def get_data(html):
    bs = BeautifulSoup(html, features='html.parser')
    items = bs.find_all('div', class_='b-content__inline_item')
    rezka_list = []
    for item in items:
        title = item.find('div', class_='b-content__inline_item-link').get_text(strip=True)
        rezka_list.append({
            'title': title,
        })
    return rezka_list

# func parser
def parsing_rezka():
    response = get_html(URL)
    if response.status_code == 200:
        rezka_list2 = []
        for page in range(1,2):
            response = get_html("https://rezka.ag/films/", params={'page': page})
            rezka_list2.extend(get_data(response.text))
        return rezka_list2
    else:
        raise Exception('Error in parsing rezka')

#print(parsing_rezka())




