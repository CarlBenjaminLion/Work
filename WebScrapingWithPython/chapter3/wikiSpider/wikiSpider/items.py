# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class WikispiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Article(Item):
    # define the fields for your item hrer like
    # name = scrapy.Field()
    title = Field()
# Scrapy 的每一个Item对象，表示网站的一个页面，当然你可以根据需要定义不同的条目
#
