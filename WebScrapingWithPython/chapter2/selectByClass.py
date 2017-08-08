# coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs_obj = BeautifulSoup(html, 'html.parser', from_encoding='urf-8')
nameList = bs_obj.findAll('span', {'class': 'green'})
# print(html)
for name in nameList:
    print(name.get_text())
# Done!
