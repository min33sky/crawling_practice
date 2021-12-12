from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selenium4에서 크롬 드라이버 설정
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

'''
    셀레니움 무한 스크롤링
'''


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    return driver


#################################################################################

browser = set_chrome_driver()
browser.maximize_window()   # 브라우저 전체 화면

url = 'https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US'
browser.get(url)

# 화면 가장 아래로 스크롤 내리기
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 2초마다 스크롤을 내린다.
interval = 2

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 스크롤바가 멈출 때 까지 내리기
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 대기
    time.sleep(interval)

    # 현재 위치 가져오기
    curr_height = browser.execute_script('return document.body.scrollHeight')

    # 이전 위치와 현재 위치가 같다는 것은 문서 가장 아래이므로 반복 중지
    if prev_height == curr_height:
        break

    # 현재 위치를 이전 위치로 저장
    prev_height = curr_height

print('문서 가장 아래 위치로 이동')
browser.quit()
