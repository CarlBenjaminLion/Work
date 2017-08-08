# coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs_obj = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
all_text = bs_obj.findAll(id='text')
print(all_text)
print(all_text[0])
print(all_text[0].get_text())
