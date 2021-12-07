import requests
from bs4 import BeautifulSoup

header = {'User-agent': 'Mozilla/5.0'}

response = requests.get('https://news.naver.com/', headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
headline = soup.select_one('.lnk_hdline_article')
print(headline.text.strip())
