# 패키지
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver as wd
from bs4 import BeautifulSoup
import time
import re


# 키워드에 따른 url 
def insta_searching(word):
    url = "https://www.instagram.com/explore/tags/" + word
    return url

# 첫번째 글 선택 
def select_first(driver):
    first = driver.find_element_by_css_selector("#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a > div.eLAPa > div._9AhH0")
    first.click()
    time.sleep(3)
    
# 본문 내용 수집
def get_content(driver):
    
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # 본문 내용 
    try:
        content = soup.select('div.C4VMK > span')[0].text
        print(content)
    except:
        content = ' '
        print(content)
    # 해시태그 
    try:
        tags = re.findall(r'#[^\s#,\\]+', content)
        print(tags)
    except:
        tags = ' '
        print(tags)
    # 작성일자 
    try:
        date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
        print(date)
    except:
        date = ' '
        print(date)
        
    data = [date, content, tags]
    return data

# 다음 페이지로 넘어가기
def move_next(driver):

    right = driver.find_element_by_css_selector ('a.coreSpriteRightPaginationArrow')
    right.click()
    
    WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.C4VMK > span'))
                )
    
    time.sleep(3)

# 데이터 크롤링
word = "밀키트" 
url = insta_searching(word)

driver.get(url)
time.sleep(10)

select_first(driver)

results = [ ]

# 추출할 게시글 수
target = 10
for i in range(target):
    print(i)
    try:
        data = get_content(driver)  
        results.append(data)
        move_next(driver)
    except:
        time.sleep(2)
        move_next(driver)


