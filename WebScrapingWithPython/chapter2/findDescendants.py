# coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs_obj = BeautifulSoup(html,'html.parser', from_encoding='utf-8')

for child in bs_obj.find('table', {'id':'giftList'}).children:
    print(child)
