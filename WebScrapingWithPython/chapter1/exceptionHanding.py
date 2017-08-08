# coding=utf-8
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs_obj = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        title  = bs_obj.body.h1
    except AttributeError as e:
        return None
    return title

title = get_title("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print('Title could not be found')
else:
    print(title)

# Done!
