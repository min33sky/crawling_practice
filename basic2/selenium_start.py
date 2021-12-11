from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Selenium4에서 크롬 드라이버 설정
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

'''
https://velog.io/@sangyeon217/deprecation-warning-executablepath-has-been-deprecated
'''

# browser = webdriver.Chrome('c:/chromedriver.exe')


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    return driver


browser = set_chrome_driver()

# 네이버 이동
browser.get('https://www.naver.com')

# 로그인 버튼 클릭
elem = browser.find_element(By.CSS_SELECTOR, 'a.link_login')
elem.click()

# ID, PW 입력
browser.find_element(By.CSS_SELECTOR, 'input#id').send_keys('my_id')
browser.find_element(By.CSS_SELECTOR, 'input#pw').send_keys('my_password')
time.sleep(1)

# 로그인 버튼 클릭
browser.find_element(By.CSS_SELECTOR, 'button.btn_login').click()

time.sleep(3)

# ID를 새로 입력
browser.find_element(By.CSS_SELECTOR, 'input#id').clear()
browser.find_element(By.CSS_SELECTOR, 'input#id').send_keys('new_id')

# HTML 정보 출력
print(browser.page_source)

# 브라우저 종료
# browser.close()  # 현재 탭만 종료
browser.quit()  # 전체 브라우저 종료
