import requests

'''
    raise_for_status()
    : 요청한 URL의 응답코드가 200이 아니라면 예외를 발생시키는 메서드
'''

res = requests.get('https://www.naver.com')
res.raise_for_status()

res = requests.get('http://hahahoho.com/qwe')
res.raise_for_status()
