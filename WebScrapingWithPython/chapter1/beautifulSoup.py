# coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bs_obj = BeautifulSoup(html.read(),'html.parser', from_encoding='utf-8')
print(bs_obj)
