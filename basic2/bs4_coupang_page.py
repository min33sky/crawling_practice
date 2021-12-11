import requests
import re
from bs4 import BeautifulSoup
import pyautogui


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

keyword = pyautogui.prompt('검색어를 입력하세요: ')

# 5페이지까지 검색하기
for page_num in range(1, 5 + 1):

    url = f'https://www.coupang.com/np/search?component=&q={keyword}&channel=user&page={page_num}'

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    # 정규표현식을 사용해서 속성을 검색할 수 있다.
    items = soup.find_all('li', attrs={'class': re.compile('^search-product')})

    # print(f'-------------- {page_num} 페이지 결과 :')

    for item in items:

        # 광고 제품 제외
        ad_badge = item.find('span', attrs={'class': 'ad-badge-text'})
        if ad_badge:
            # print(' < 광고 제품이므로 쳐내겠습니다. >')
            continue

        name = item.find('div', attrs={'class': 'name'}).get_text()

        if 'Apple' in name:
            # print(' < Apple MacBook Out!!! >')
            continue

        price = item.find('strong', attrs={'class': 'price-value'}).get_text()

        # 평점이 없는 상품일 경우의 예외 처리
        try:
            rate = item.find('em', attrs={'class': 'rating'}).get_text()
            rate_count = item.find(
                'span', attrs={'class': 'rating-total-count'}).get_text()[1:-1]
        except:
            # print(' < 평점 없는 제품은 쳐냅니다. >')
            continue

        link = item.a['href']

        if float(rate) >= 4.5 and int(rate_count) >= 500:
            print(f'{name}: {price} - 평점: {rate}, {rate_count}')
            print(f'이름: {name}')
            print(f'가격: {price}')
            print(f'평점: {rate} - ({rate_count})')
            print(f'링크: https://www.coupang.com{link}')
            print('-'*100)

print('검색 끝 :)')
