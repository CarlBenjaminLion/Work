# coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
# print(datetime.datetime.now())
def get_links(articleURL):
    html = urlopen('http://en.wikipedia.org'+articleURL)
    bs_obj = BeautifulSoup(html,'html.parser', from_encoding='utf-8')
    return bs_obj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
links = get_links('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = get_links(newArticle)

    
