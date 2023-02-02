from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('/Users/yunkanghyun/Downloads/chromedriver')
driver.implicitly_wait(3)
# url에 접근한다.
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
# Login
driver.get('https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do?searchCondition=&searchKeyword=&column=&selUpjong=&selIndus=&pageUnit=2&pageIndex='+'1') # 네이버 로그인 URL로 이동하기
#driver.find_element_by_xpath('//*[@id="log.login"]').click() # 버튼클릭하기

html = driver.page_source # 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기

notices = soup.select('#frm > table > tbody > tr')

for n in notices:
    sangho = n.select_one("td:nth-child(2)").text.strip()
    driver.get('https://bizno.net/%EC%83%81%ED%98%B8%EB%AA%85%EC%9C%BC%EB%A1%9C%EC%82%AC%EC%97%85%EC%9E%90%EB%93%B1%EB%A1%9D%EB%B2%88%ED%98%B8%EC%A1%B0%ED%9A%8C/')
    driver.find_element_by_name('query').send_keys(sangho)
    driver.find_element_by_xpath('//*[@id="home"]/div[2]/div/div/form/div/div[3]/button').click()
    driver.execute_script("window.scrollTo(0, 700)")
    driver.find_element_by_xpath('/html/body/section[2]/div/div/div[1]/div[2]/div/div/div/a/h4').click()
    driver.execute_script("window.scrollTo(0, 700)")
    nb = soup.select('tr:nth-child(11) > th > span')
    print(sangho, nb)
