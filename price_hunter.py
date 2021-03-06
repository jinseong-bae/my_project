from curses.ascii import US

import requests
from bs4 import BeautifulSoup
from flask import jsonify
from pymongo import MongoClient
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


client = MongoClient('mongodb://sparta:sparta123!@localhost', 27017)
db = client.dbjinseong


def send_email(you):
    me = "wlstjd7056@gmail.com"
    my_password = "aeadzyrrgsnbremx"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "[PRICE HUNTER] 선택하신 상품이 목표가격에 도달하였습니다!!"
    msg['From'] = me
    msg['To'] = you

    html = '<html>' \
           '<body>' \
           '<p><img src="https://img1.daumcdn.net/thumb/R720x0/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fliveboard%2Fanimalpeople%2F539cc950b2e3467eb7cd8b010e562257.JPG"/> <br> 축하합니다!<br> 선택하신 상품이 목표가격에 도달했습니다! <br> 지금 바로 상품을 확인하세요! </p>' \
           '</body></html>'
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    s = smtplib.SMTP_SSL('smtp.gmail.com')
    s.login(me, my_password)
    s.sendmail(me, you, msg.as_string())
    s.quit()

def price_hunting():
    order_infos = list(db.infos.find({'flag': 0}, {'_id': False}))

    for info in order_infos:
        order_URL = info['model']
        price = info['price']
        mail_address = info['mail_address']

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(order_URL)
        soup = BeautifulSoup(data.text, 'html.parser')

        if order_URL.startswith("https://www.yoox"):
            price_tag = soup.select_one('#item-price > span.font-bold > span')
            print('yoox 탐색중!', price_tag.text[4:9], price)
            if price_tag.text[4:9] <= price:
                send_email(mail_address)
                db.infos.update_one({'model': order_URL}, {'$set': {'flag': 1}})
            else:
                db.infos.update_one({'model': order_URL}, {'$set': {'current_price': price_tag.text[2:9]}})

        elif order_URL.startswith("https://www.fwrd"):
            price_tag = soup.select_one(
                '#page-content > div.fwd_pdp > div.pdp > div.pdp__col.pdp__col--fixed-width > div > div > div > span')
            print('fwrd 탐색중!', price_tag.text.lstrip('$'), price)
            if price_tag.text.lstrip('$') <= price:
                send_email(mail_address)
                db.infos.update_one({'model': order_URL}, {'$set': {'flag': 1}})
            else:
                db.infos.update_one({'model': order_URL}, {'$set': {'current_price': price_tag.text}})

        elif order_URL.startswith("https://www.balaan"):
            price_tag = soup.select_one(
                '#price')
            print('balaan 탐색중!', price_tag.text.strip().lstrip('￦'), price)
            if price_tag.text.strip().lstrip('￦') <= price:
                send_email(mail_address)
                db.infos.update_one({'model': order_URL}, {'$set': {'flag': 1}})
            else:
                db.infos.update_one({'model': order_URL}, {'$set': {'current_price': price_tag.text.strip()}})






def run():
    schedule.every(10).seconds.do(price_hunting) # 10초마다 job 함수를 실행
    while True:
        schedule.run_pending()

if __name__ == "__main__":
    run()
