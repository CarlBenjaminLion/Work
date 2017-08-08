# coding=utf-8
from urllib.request import urlopen
# Retrive HTML string fron the URL
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
print(html.read())
# Sucess!
