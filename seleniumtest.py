from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

f = open("franchise_info.csv", "w")
# 헤더 추가하기
f.write("번호,상호,영업표지,대표자,등록번호,최초등록일,업종")

driver = webdriver.Chrome('/Users/yunkanghyun/Downloads/chromedriver')
driver.implicitly_wait(3)
# url에 접근한다.
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
# Login
driver.get('https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do?searchCondition=&searchKeyword=&column=&selUpjong=&selIndus=&pageUnit=12300&pageIndex='+'1') # 네이버 로그인 URL로 이동하기
#driver.find_element_by_xpath('//*[@id="log.login"]').click() # 버튼클릭하기

html = driver.page_source # 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기

notices = soup.select('#frm > table > tbody > tr')

for n in notices:
    bun = n.select_one("td:nth-child(1)").text.strip()
    sang = n.select_one("td:nth-child(2)").text.strip()
    young = n.select_one("td:nth-child(3)").text.strip()
    dae = n.select_one("td:nth-child(4)").text.strip()
    deung = n.select_one("td:nth-child(5)").text.strip()
    choi = n.select_one("td:nth-child(6)").text.strip()
    eop = n.select_one("td:nth-child(7)").text.strip()

    print(bun,sang,young,dae,deung,choi,eop)

    f.write("\n" + bun + "," + sang + "," + young + "," + dae + "," + deung + "," + choi + "," + eop)

# 작업이 끝난 파일을 닫습니다.
# 반복문 밖에서 닫아줍니다.
f.close()