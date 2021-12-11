# Crawling Basic

## Install Modules

```bash
# Http request
pip install requests
# HTML Parsing
pip install beautifulsoup4
# lxml (bs4의 html parser)
pip install lxml
# Excel
pip install openpyxl
# selenium
pip install selenium
# pyautogui
pip install pyautogui
```

## Error

- pyautogui는 wsl에서 작동하지 않는다.

## Coding Note

1. requests

`http` 요청 라이브러리

2. beautifulsoup

웹페이지에서 정보를 스크래핑할 수 있는 라이브러리

- HTML을 파싱할 수 있는 라이브러리가 여러개 있다

```py
response = requests.get(url)

html = response.text

# 기본 제공하는 파서
soup = BeautifulSoup(html, 'html.parser')

# lxml 모듈을 설치해야 사용가능 (추천)
soup = BeautifulSoup(html, 'lxml')
```

- `select`와 `find`로 원하는 정보를 찾을 수 있다.
  - select가 더 사용이 편하고 속도도 빠르다고 한다.

3. Selenium

- Selenium4에서 바뀐 코드
  - chromeDriver를 직접 다운 받을 필요없이 설정이 변경되었다.
  - find_element() 메서드로 통합

```py
from selenium.webdriver.common.by import By

# Selenium4에서 크롬 드라이버 설정
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    return driver


browser = set_chrome_driver()


# 로그인 버튼 클릭
elem = browser.find_element(By.CSS_SELECTOR, 'a.link_login')

```
