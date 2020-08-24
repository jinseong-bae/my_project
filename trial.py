import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.matchesfashion.com/kr/products/Gucci-%EC%98%A4%ED%94%84-%EB%8D%94-%EA%B7%B8%EB%A6%AC%EB%93%9C-%EB%A1%9C%EA%B3%A0-%ED%8C%A8%EC%B9%98-GG-%EC%BA%94%EB%B2%84%EC%8A%A4-%EC%B9%B4%EB%93%9C%ED%99%80%EB%8D%94-1356241')

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦

soup = BeautifulSoup(data.text, 'html.parser')

price_tag = soup.select_one('#pdpMainWrapper > div.pdp__description-wrapper > div.pdp__header.hidden-mobile > p')
print(price_tag)



#slice-pdp > div > div._6c4acd > div._5225f2 > div._c40757 > div._81fc25 > div > span
#slice-pdp > div > div._6c4acd > div._5225f2 > div._c40757 > div._81fc25 > div > span
#slice-pdp > div > div._6c4acd > div._5225f2 > div._c40757 > div._81fc25 > div > span

#wrap > div > div > div.pdp__mobile--new.pdp__redesign > div > div.pdp-mobile > div > div > div.s-row.pdp-header__right > div > div > div > div > div > div > div > div > h1

#wrap > div > div > div.pdp__mobile--new.pdp__redesign > div > div.pdp-mobile > div > div > div.s-row.pdp-header__right > div > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div > h1
