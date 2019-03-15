# -*- coding: utf-8 -*-
import scrapy
from gjyzjsswz.items import GjyzjsswzItem
from scrapy.loader import ItemLoader
from scrapy import FormRequest
from scrapy.loader.processors import MapCompose, Join

class LogisticsSpider(scrapy.Spider):
    name = 'logistics'
    allowed_domains = ['sswz.spb.gov.cn']
    start_urls = ['http://sswz.spb.gov.cn/praiseList.do']
    url = 'http://sswz.spb.gov.cn/praiseList.do'
    page = 1


    def parse(self, response):
        item = GjyzjsswzItem()
        for i in range(0,4):
            item['topic'] = response.xpath('//a[@class="name"]/text()').extract()[i].strip()
            item['review'] = response.xpath('//span[@class="body"]/text()').extract()[i].strip()
            item['page_number'] = str(self.page)
            yield item
            i = i+1

            # l = ItemLoader(item = GjyzjsswzItem(), response = response)
            # l.add_xpath('page_number','//li[@class="disabled"][2]//a[@href="#"]/text()')
            # l.add_xpath('topic', '//a[@class="name"]/text()')
            # l.add_xpath('review', '//span[@class="body"]/text()')
        # return l.load_item()

        if self.page < 1987:
            self.page += 1
            yield scrapy.FormRequest(
                url = self.url,
                #method = 'POST',
                formdata = {"basePageNo": str(self.page)},
                callback = self.parse)