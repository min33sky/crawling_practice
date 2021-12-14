from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import time


# Selenium4에서 크롬 드라이버 설정


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    return driver


browser = set_chrome_driver()
browser.maximize_window()   # 브라우저 전체 화면
weather_url = 'https://search.naver.com/search.naver?where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&ie=utf8&sm=tab_she&qdt=0'

#################################################################################


'''
[조건]
1. 네이버에서 오늘 서울의 날씨 정보를 가져온다.
2. 헤드라인 뉴스 3건을 가져온다
3. IT 뉴스 3건을 가져온다.
4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다.
'''


def scrape_weather():

    soup = create_soup(weather_url)

    # 날씨 요약
    temperature = soup.select_one('p.summary').get_text().split()
    description = ' '.join(temperature[:-1])

    # 현재 온도
    current_temperature = soup.find(
        'span', attrs={'class': 'blind'}, text='현재 온도').next_sibling

    # 최저 온도, 최고 온도
    lowest = str(soup.select_one('span.lowest')).split(r'</span>')[-2]
    highest = str(soup.select_one('span.highest')).split(r'</span>')[-2]

    # 오전 강수확률
    morning_rainfall = soup.find(
        'strong', attrs={'class': 'time'}, text='오전').find_next_sibling(
        'span', attrs={'class': 'rainfall'}).get_text()

    # 오후 강수확률
    afternoon_rainfall = soup.find(
        'strong', attrs={'class': 'time'}, text='오후').find_next_sibling(
        'span', attrs={'class': 'rainfall'}).get_text()

    print('[오늘의 날씨]')
    print(f'{temperature[-1]}, {description}')
    print(f'현재 {current_temperature}℃  (최저 {lowest} / 최고 {highest})')
    print(f'오전 강수확률 {morning_rainfall} / 오후 강수확률 {afternoon_rainfall}')

    # 미세먼지 데이터 호출
    getFineDust()


def getFineDust():

    browser.get(weather_url)

    try:
        browser.find_element(
            By.CSS_SELECTOR, 'li.item_today.level2 > a').click()
        time.sleep(2)

        # 먼지 수치 찾기
        results = browser.find_elements(
            By.CSS_SELECTOR, 'div.grade.level1._level')[:2]

        fine_dust = results[0].text
        ultra_fine_dust = results[1].text

        print(f'미세먼지 {fine_dust}')
        print(f'초미세먼지 {ultra_fine_dust}')

    except:
        print('미세먼지 데이터가 없습니다.')


def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


if __name__ == '__main__':
    scrape_weather()
    browser.quit()
