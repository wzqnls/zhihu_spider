# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy_djangoitem import DjangoItem

from zhihu_backend.models import Customer


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PeopleInfoItemLoader(ItemLoader):
    # 自定义itemloader
    default_output_processor = TakeFirst()


class PeopleInfoItem(DjangoItem):
    django_model = Customer