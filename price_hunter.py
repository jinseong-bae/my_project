from curses.ascii import US

import requests
from bs4 import BeautifulSoup
from flask import jsonify
from pymongo import MongoClient
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


client = MongoClient('localhost', 27017)
db = client.dbjinseong

order_infos = list(db.infos.find({}, {'_id': False}))

# for info in order_infos:

order_URL = order_infos[0]['model']
price = order_infos[0]['price']
mail_address = order_infos[0]['mail_address']


def send_email():
    me = "wlstjd7056@gmail.com"
    my_password = "aeadzyrrgsnbremx"
    you = mail_address

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "가격추적완료!!"
    msg['From'] = me
    msg['To'] = you

    html = '<html><body><p>축하합니다! 해당 제품의 가격이 희망가격의 이하로 설정되었습니다! <br>지금 바로 상품을 확인하세요! </p></body></html>'
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    s = smtplib.SMTP_SSL('smtp.gmail.com')
    s.login(me, my_password)
    s.sendmail(me, you, msg.as_string())
    s.quit()


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(order_URL)

soup = BeautifulSoup(data.text, 'html.parser')
targets = soup.select('#item-price')


for target in targets:
  price_tag = target.select_one('span.font-bold > span')
if price_tag.text[4:9] <= price:
 send_email()



# def run():
#     schedule.every(10).seconds.do(price_hunting()) # 10초마다 job 함수를 실행
#     while True:
#         schedule.run_pending()
#
# if __name__ == "__main__":
#     run()


# 10초에 한번씩 실행
# schedule.every(10).second.do(price_hunting)




