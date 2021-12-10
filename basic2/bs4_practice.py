from bs4 import BeautifulSoup
import requests

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

# lxml 파서가 html.parser보다 빠르다. (설치 필요: pip install lxml)
soup = BeautifulSoup(res.text, 'lxml')

# print(soup.title)                   # title 태그 가져오기
# print(soup.title.get_text())        # title 태그의 text 노드 가져오기
# print(soup.a)                       # 가정 먼저 발견되는 a 태그값을 가져오기
# print(soup.a.attrs)                 # a 태그의 속성들을 가져오기
# print(soup.a['href'])               # a 태그의 href 속성값을 가져오기

# class명이 Nbtn_upload인 첫번째 a태그를 찾아라
# print(soup.find('a', attrs={'class': 'Nbtn_upload'}))
# class명이 Nbtn_upload인 첫번째 아무 태그나 찾아라
# print(soup.find(attrs={'class': 'Nbtn_upload'}))

rank01 = soup.find(attrs={'class': 'rank01'})
print(rank01.a.get_text())

# rank02 = rank01.find_next_sibling('li')
# print(rank02.a.get_text())

# rank03 = rank02.find_next_sibling('li')
# print(rank03.a.get_text())

ranks = rank01.find_next_siblings('li')
for rank in ranks:
    print(rank.a.get_text())

print('---------------------------------------')

# a태그 중에서 해당 text가 포함된 태그 검색학시
webtoon = soup.find('a', text='광마회귀')
print(webtoon.get_text())
