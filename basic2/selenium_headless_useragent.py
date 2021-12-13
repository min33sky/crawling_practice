from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selenium4에서 크롬 드라이버 설정
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


'''
    Headless Chrome을 사용할 때 user-agent에 HeadlessChrome이 적혀있다.
    - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/96.0.4664.93 Safari/537.36
    특정 사이트의 경우에서 크롤러를 차단하므로 user-agent를 사람인것처럼 위장해야한다.
'''


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True  # Headless Chrome
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36')

    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    return driver


#################################################################################

browser = set_chrome_driver()
browser.maximize_window()   # 브라우저 전체 화면

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36
user_agent = browser.find_element(By.CSS_SELECTOR, '#detected_value').text
print(user_agent)
