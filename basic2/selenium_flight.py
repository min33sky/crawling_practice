from os import truncate
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
네이버 항공권 예약
'''


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    return driver


#################################################################################

start_date = '2022.01.14'
end_date = '2022.03.22'
start_date_check = False
flag = False

browser = set_chrome_driver()
browser.maximize_window()   # 브라우저 전체 화면

url = 'https://flight.naver.com/'

browser.get(url)

# browser.find_element(
#     By.CSS_SELECTOR, 'button.tabContent_option__2y4c6').click()

# 예약 캘린더 버튼 클릭
browser.find_element(
    By.XPATH, r'//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

time.sleep(1)

# 날짜 선택하기
months = browser.find_elements(By.CSS_SELECTOR, 'div.month')
# print(months)

time.sleep(1)

for month in months:
    # 달 출력
    text = month.find_element(By.CSS_SELECTOR, '.sc-iqAclL').text

    # 출발, 도착과 관련 없는 달은 제외한다.
    if text != start_date[0:8] and text != end_date[0:8]:
        continue

    print(text)

    # 일 출력
    days = month.find_elements(By.CSS_SELECTOR, 'td.day')

    for day in days:
        if start_date_check == False and day.text == start_date[-2:]:
            day.click()
            time.sleep(1)
            start_date_check = True
            break

        if start_date_check == True and day.text == end_date[-2:]:
            day.click()
            flag = True
            break

    # 예약 날짜 선택이 끝났으므로 반복 종료
    if flag == True:
        break

# TODO: 도착 장소 정하기
browser.find_element(
    By.XPATH, r'//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.autocomplete_input__1vVkF')))

    print(elem)

    elem.click()
    elem.send_keys('하네다국제공항')

    time.sleep(1)

    browser.find_element(
        By.CSS_SELECTOR, 'a.autocomplete_search_item__2WRSw').click()

    time.sleep(1)

    browser.find_element(
        By.CSS_SELECTOR, 'button.searchBox_search__2KFn3').click()

    # div.result
    result = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.result')))

    print(result.text)


finally:
    # browser.close()
    # browser.quit()
    print()
