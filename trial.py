import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.farfetch.com/shopping/men/valentino-vltn-logo-polo-shirt-item-15200072.aspx?storeid=11560')

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦

soup = BeautifulSoup(data.text, 'html.parser')

price_tag = soup.select_one('#slice-pdp > div > div._6c4acd > div._5225f2 > div._c40757 > div._81fc25 > div > span')
print(price_tag.text)



#slice-pdp > div > div._6c4acd > div._5225f2 > div._c40757 > div._81fc25 > div > span
#slice-pdp > div > div._6c4acd > div._5225f2 > div._c40757 > div._81fc25 > div > span
#slice-pdp > div > div._6c4acd > div._5225f2 > div._c40757 > div._81fc25 > div > span

#wrap > div > div > div.pdp__mobile--new.pdp__redesign > div > div.pdp-mobile > div > div > div.s-row.pdp-header__right > div > div > div > div > div > div > div > div > h1

#wrap > div > div > div.pdp__mobile--new.pdp__redesign > div > div.pdp-mobile > div > div > div.s-row.pdp-header__right > div > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div > h1
