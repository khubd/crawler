# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeituiItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    location = scrapy.Field()
    position = scrapy.Field()
    employment = scrapy.Field()
    mobile = scrapy.Field()
    targetJob = scrapy.Field()
    targetCity = scrapy.Field()
    age = scrapy.Field()
    title = scrapy.Field()
    workYear = scrapy.Field()
    content = scrapy.Field()
    detail = scrapy.Field()
    url = scrapy.Field()
