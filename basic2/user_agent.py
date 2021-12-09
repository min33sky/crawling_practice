import requests

url = 'http://nadocoding.tistory.com'

# https://www.whatismybrowser.com/detect/what-is-my-user-agent
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

res = requests.get(url, headers=headers)
res.raise_for_status()

# 파일에 저장
with open('nadocoding.html', 'w', encoding='utf8') as f:
    f.write(res.text)
