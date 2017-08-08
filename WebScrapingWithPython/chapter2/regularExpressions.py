# coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs_obj = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
images = bs_obj.findAll('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])


