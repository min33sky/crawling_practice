import requests
from bs4 import BeautifulSoup
import pyautogui

header = {'User-agent': 'Mozilla/5.0'}

# keyword = input()
keyword = pyautogui.prompt('검색어를 입력하세요')
lastPage = pyautogui.prompt('검색할 페이지 수를 입력하세요')

pageNum = 1

for i in range(1, int(lastPage) * 10, 10):
    response = requests.get(
        f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&start={i}', headers=header)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    links = soup.select('.news_tit')

    print(f'페이지 {pageNum} ---------------------------------------')

    for idx, link in enumerate(links):
        news_link = link.attrs['href']
        print(f'{idx + 1}: {link.text.strip()} - {news_link}')

    pageNum += 1
