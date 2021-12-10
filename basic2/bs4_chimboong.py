import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=103759'

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# 웹툰 제목 추출
cartoon_title = soup.find(
    'div', attrs={'class': 'detail'}).h2.get_text().split()[0]

# 웹툰 회차 검색
cartoons = soup.find_all('td', attrs={'class': 'title'})

score_sum = 0

print(f'------------------------{cartoon_title}-----------------------------')

for cartoon in cartoons:
    title = cartoon.a.get_text()
    url = cartoon.a['href']
    score = cartoon.find_next_sibling('td').strong.get_text()
    print(f'[{title}] 평점: {score} -  https://comic.naver.com{url}')
    score_sum += float(score)

average = score_sum / len(cartoons)
print(f'평점 평균: {average}')
