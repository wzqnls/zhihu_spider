# -*- coding: utf-8 -*-

import json

import scrapy

from ZhiHu.settings import DEFAULT_REQUEST_HEADERS
from ZhiHu.utils.for_cookies import get_cookies


class PeopleRelationsSpider(scrapy.Spider):
    name = "people_relations"
    allowed_domains = ["https://www.zhihu.com"]
    start_urls = ['https://www.zhihu.com/']

    def parse(self, response):
        pass

    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com/question/60673524', headers=DEFAULT_REQUEST_HEADERS, cookies=get_cookies(), callback=self.parse)]

