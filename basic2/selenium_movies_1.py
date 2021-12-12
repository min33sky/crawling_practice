import requests
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US'

# 헤더에 접속 정보 추가
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'Accept-Language': 'Ko-KR'
}


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select(
    'div.ImZGtf.mpg5gc')

# 아직 해당 태그가 존재하지 않아 길이가 0이 나온다.
print(len(movies))

# 파일을 저장해서 확인해보면 화면에 있는 영화는 존재하지 않는다. (미국에서 접속한 화면으로 뜨기때문에)
# 헤더에 정보를 추가해서 해결한다.
with open('movie.html', 'w', encoding='utf8') as f:
    f.write(soup.prettify())

for movie in movies:
    title = movie.select_one('div.WsMG1c.nnK0zc')
    print(title.get_text())
