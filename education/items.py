# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


class EducationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(
    	input_processor=MapCompose(remove_tags),
    	output_processor=TakeFirst()
    	)

    details = scrapy.Field(
    	input_processor=MapCompose(remove_tags),
    	output_processor=Join()
    	)
    pass
