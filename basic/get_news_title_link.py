import requests
from bs4 import BeautifulSoup
import pyautogui

header = {'User-agent': 'Mozilla/5.0'}

# keyword = input()
keyword = pyautogui.prompt('검색어를 입력하세요')

for i in range(3):
    response = requests.get(
        f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=27&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={str(i * 10 + 1)}', headers=header)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    links = soup.select('.news_tit')
    for idx, link in enumerate(links):
        news_link = link.attrs['href']
        print(f'{i}{idx}: {link.text.strip()} - {news_link}')
