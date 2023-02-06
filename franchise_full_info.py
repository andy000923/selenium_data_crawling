from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
f = open("franchise_full_info.csv", "w")
f.write("번호,상호,영업표지,대표자,등록번호,최초등록일,업종,공정거래위원회의 시정조치,민사소송 패소 및 민사상 화해,형의 선고,"
        "가입비(가맹비),교육비,보증금,기타비용,합계,단위면적(3.3㎡)당 인테리어 비용,기준점포면적(㎡),인테리어 비용")


driver = webdriver.Chrome('/Users/yunkanghyun/Downloads/chromedriver')
driver.implicitly_wait(3)
# url에 접근한다.
driver.get('https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do?searchCondition=&searchKeyword=&column=&selUpjong=&selIndus=&pageUnit=12300&pageIndex={0}'.format(1))
#driver.maximize_window()
html = driver.page_source # 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기
line = soup.select('#frm > table > tbody > tr')
i = 1
for n in line:
    bun = n.select_one("td:nth-child(1)").text.strip()
    sang = n.select_one("td:nth-child(2)").text.strip()
    young = n.select_one("td:nth-child(3)").text.strip()
    dae = n.select_one("td:nth-child(4)").text.strip()
    deung = n.select_one("td:nth-child(5)").text.strip()
    choi = n.select_one("td:nth-child(6)").text.strip()
    eop = n.select_one("td:nth-child(7)").text.strip()
    dae = dae.replace(",", " ")
    sang = sang.replace(",", " ")
    young = young.replace(",", " ")

    driver.find_element_by_css_selector("tr:nth-child({0}) > td:nth-child(2) > a".format(i)).click()
    i += 1
    html = driver.page_source #페이지의 elements모두 가져오기
    soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기

    law = soup.select('#frm > div:nth-child(14) > div > table > tbody > tr')

    for l in law:
        l1 = l.select_one("td.noborder").text.strip()
        l2 = l.select_one("td:nth-child(2)").text.strip()
        l3 = l.select_one("td:nth-child(3)").text.strip()

    contribution = soup.select('#frm > div:nth-child(15) > div > table:nth-child(2) > tbody > tr')

    for c in contribution:
        c1 = c.select_one("td.noborder").text.strip()
        c2 = c.select_one("td:nth-child(2)").text.strip()
        c3 = c.select_one("td:nth-child(3)").text.strip()
        c4 = c.select_one("td:nth-child(4)").text.strip()
        c5 = c.select_one("td:nth-child(5)").text.strip()

    price = soup.select('#frm > div:nth-child(15) > div > table:nth-child(4) > tbody > tr')

    for p in price:
        p1 = p.select_one("td.noborder").text.strip()
        p2 = p.select_one("td:nth-child(2)").text.strip()
        p3 = p.select_one("td:nth-child(3)").text.strip()

        l1 = l1.replace(",", "")
        l2 = l2.replace(",", "")
        l3 = l3.replace(",", "")

        c1 = c1.replace(",", "")
        c2 = c2.replace(",", "")
        c3 = c3.replace(",", "")
        c4 = c4.replace(",", "")
        c5 = c5.replace(",", "")

        p1 = p1.replace(",", "")
        p2 = p2.replace(",", "")
        p3 = p3.replace(",", "")

    print(bun,sang,young,dae,deung,choi,eop,l1,l2,l3,c1,c2,c3,c4,c5,p1,p2,p3)
    f.write("\n" + bun + "," + sang + "," + young + "," + dae + "," + deung + "," + choi + "," + eop + "," + l1 + "," + l2 + "," + l3 + "," + c1 + "," + c2 + "," + c3 + "," + c4 + "," + c5 + "," + p1 + "," + p2 + "," + p3)
    driver.get('https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do?searchCondition=&searchKeyword=&column=&selUpjong=&selIndus=&pageUnit=12300&pageIndex=1')
