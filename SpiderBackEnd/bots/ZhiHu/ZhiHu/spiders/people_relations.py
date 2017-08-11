# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader

from bots.ZhiHu.ZhiHu.settings import DEFAULT_REQUEST_HEADERS
from bots.ZhiHu.ZhiHu.utils.for_cookies import get_cookies
from bots.ZhiHu.ZhiHu.items import PeopleRelationsItem


class PeopleRelationsSpider(scrapy.Spider):
    name = "people_relations"
    allowed_domains = ["https://www.zhihu.com"]
    start_urls = ['https://www.zhihu.com/']

    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com/people/li-shuo-1-31/following', cookies=get_cookies(), callback=self.parse_page)]

    def parse_page(self, response):
        pass


    def parse_page_info(self, reponse):
        pass