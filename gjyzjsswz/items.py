# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GjyzjsswzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page_number = scrapy.Field()
    topic = scrapy.Field()
    review = scrapy.Field()
