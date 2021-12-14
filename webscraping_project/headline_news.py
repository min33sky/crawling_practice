import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}


def scrape_headline():
    url = 'https://news.naver.com/'
    soup = create_soup(url)

    # 헤드라인 뉴스 5개중 3개만 추출
    news_list = soup.select(
        'ul.hdline_article_list div.hdline_article_tit', limit=3)

    for news in news_list:
        link = news.a.attrs['href']
        print(f'{news.get_text().strip()}, https://news.naver.com/{link}')


def create_soup(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


if __name__ == '__main__':
    scrape_headline()
