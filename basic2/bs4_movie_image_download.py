import requests
from bs4 import BeautifulSoup

'''
2016 ~ 2020년도 영화 인기 1 ~ 5위 포스터 다운로드
'''

for year in range(2016, 2020 + 1):

    url = f'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={year}%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84'

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    movies = soup.select('img.thumb_img')

    for idx, movie in enumerate(movies):
        poster_url = movie['src']

        if poster_url.startswith('//'):
            poster_url += 'https:'

        # 이미지 주소에 http 요청
        res = requests.get(poster_url)
        res.raise_for_status()

        # 이미지를 파일에 저장하기 (이미지파일이므로 'wb')
        with open(f'basic2/poster_{year}_{idx + 1}.jpg', 'wb') as f:
            f.write(res.content)

        if idx == 4:  # 순위 5등까지만 다운로드
            break
