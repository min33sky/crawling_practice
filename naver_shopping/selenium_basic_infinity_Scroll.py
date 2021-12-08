from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

# 브라우저 생성
browser = webdriver.Chrome('c:/chromedriver.exe')

# 웹사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10)  # 로딩이 끝날 때까지 10초까지는 기다린다.

# 쇼핑메뉴 열기
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)   # 검색창을 찾기위해 2초정도 대기

# 검색창 클릭
search = browser.find_element_by_css_selector('.co_srh_area > .co_srh_input')
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이 (자바스크립트 명령어 사용)
before_h = browser.execute_script('return window.scrollY')

# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    browser.find_element_by_css_selector('body').send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간 (1초)
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script('return window.scrollY')

    if after_h == before_h:  # 제일 아래 스크롤이 위치하므로 반복문 중지
        break

    before_h = after_h  # 스크롤 위치 업데이트


# 상품 정보 래퍼: basicList_info_area__17Xyo
# 상품 정보 div Tag
items = browser.find_elements_by_css_selector('.basicList_info_area__17Xyo')

for item in items:
    name = item.find_element_by_css_selector(
        '.basicList_title__3P9Q7 > a').text
    try:
        price = item.find_element_by_css_selector(
            '.price_num__2WUXn').text
    except:
        price = '판매중단'

    link = item.find_element_by_css_selector(
        '.basicList_title__3P9Q7 > a').get_attribute('href')

    print(f'{name}: {price} - {link}')
