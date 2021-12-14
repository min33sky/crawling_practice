import requests
from bs4 import BeautifulSoup
import re

# https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;

url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;'

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

expressions = soup.select('div.conv_in')


print('오늘의 영어 회화')
print('[영어 지문]')
english = expressions[1].get_text().strip().split('\n')
for expression in english:
    if len(expression) != 0:
        print(expression)

print('\n[한글 지문]')
korean = expressions[0].get_text().strip().split('\n')
print('\n'.join(expression for expression in korean if len(expression) != 0))
