import schedule
import time
from datetime import datetime
import slack_sdk
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def job():
    global recentSubject
    #슬랙
    token_slack = "여기에 섹시코만도 토큰 입력. 깃허브엔 토큰값 올리면 안됨."
    client = slack_sdk.WebClient(token=token_slack)

    # 옵션 생성
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")

    # driver 실행
    driver = webdriver.Chrome('/Users/yunkanghyun/Downloads/chromedriver', options=options)
    driver.implicitly_wait(3)
    driver.get('https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do?searchCondition=&searchKeyword=&column=&selUpjong=&selIndus=&pageUnit=10&pageIndex=1')

    index1 = driver.find_element(By.XPATH, '//*[@id="frm"]/table/tbody/tr[1]/td[1]').text
    index2 = driver.find_element(By.XPATH, '//*[@id="frm"]/table/tbody/tr[1]/td[2]').text
    index3 = driver.find_element(By.XPATH, '//*[@id="frm"]/table/tbody/tr[1]/td[3]').text
    index4 = driver.find_element(By.XPATH, '//*[@id="frm"]/table/tbody/tr[1]/td[4]').text
    index5 = driver.find_element(By.XPATH, '//*[@id="frm"]/table/tbody/tr[1]/td[5]').text
    index6 = driver.find_element(By.XPATH, '//*[@id="frm"]/table/tbody/tr[1]/td[6]').text
    index7 = driver.find_element(By.XPATH, '//*[@id="frm"]/table/tbody/tr[1]/td[7]').text
    link = driver.find_element(By.XPATH, '//*[@id="frm"]/table/tbody/tr[1]/td[2]/a').get_attribute('onclick')

    url = 'https://franchise.ftc.go.kr'
    new_link = re.search(r'\(\'(.*?)\'\)', link).group(1)

    if recentSubject != index1:
        targetMsg1 = "[정보공개서] " + index1 + ", " + index2 + ", " + index3 + ', ' + index4 + ", " + index5 \
                    + ", " + index6 + ', ' + index7 + '\n' + url + new_link
        # 슬랙에 메세지 보내기
        client.chat_postMessage(channel='#9_notice_product_group', text=targetMsg1)
        recentSubject = index1

    else:
        print(datetime.now(), '정보공개서 변경사항 없음')

    driver.quit()

recentSubject = ""
# 1분 마다 실행
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
