# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GjyzjsswzPipeline(object):
    def __init__(self):
         self.file = open("logistics_review_P.csv", "w")
         self.file.write('page_number,topic,review\n')
    def process_item(self, item, spider):
        info = dict(item)
        self.file.write(info["page_number"]+"#"+info["topic"]+"#"+info["review"].replace("\n","，").replace("\r","，")+"\n")
        return item

    def close_spider(self, spider):
        self.file.close()
