import requests
from bs4 import BeautifulSoup

codes = ['005930', '036570', '293490', '225570', '194480']

for code in codes:
    response = requests.get(
        f'https://finance.naver.com/item/sise.naver?code={code}')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one('#_nowVal')

    print(price.text)
