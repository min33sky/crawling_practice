import csv
import requests
from bs4 import BeautifulSoup

'''
코스피 시가총액 순위 csv 파일에 저장하기
'''

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='

table_columns = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split(
    '\t')

filename = '시가총액1-200.csv'

# 한글이 깨질 때 인코딩 방식 변경 : utf-8-sig
# 줄바꿈 형식 : newline=''
f = open(filename, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

writer.writerow(table_columns)

for page_num in range(1, 2 + 1):

    res = requests.get(url, str(page_num))
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    rows = soup.select('table.type_2 > tbody > tr')

    for row in rows:
        columns = row.select('td')

        # 의미없는 줄바꿈칸은 넘어간다.
        if(len(columns) == 1):
            continue

        # print([column.get_text().strip() for column in columns])

        data = [column.get_text().strip() for column in columns]

        writer.writerow(data)
