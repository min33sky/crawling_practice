import requests
from bs4 import BeautifulSoup

# 크롤링 봇 감지를 피하기 위한 설정
header = {'User-agent': 'Mozilla/5.0'}

response = requests.get('https://news.naver.com/', headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
headlines = soup.select('.lnk_hdline_article')

for headline in headlines:
    print(headline.text.strip())
