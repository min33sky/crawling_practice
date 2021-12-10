import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# 정규표현식을 사용해서 속성을 검색할 수 있다.
items = soup.find_all('li', attrs={'class': re.compile('^search-product')})

for item in items:
    name = item.find('div', attrs={'class': 'name'}).get_text()
    price = item.find('strong', attrs={'class': 'price-value'}).get_text()

    # 평점이 없는 상품일 경우의 예외 처리
    try:
        rate = item.find('em', attrs={'class': 'rating'}).get_text()
        rate_count = item.find(
            'span', attrs={'class': 'rating-total-count'}).get_text()
    except:
        rate = '평점 없음'
        rate_count = '(0)'

    print(f'{name}: {price} - 평점: {rate}, {rate_count}')
