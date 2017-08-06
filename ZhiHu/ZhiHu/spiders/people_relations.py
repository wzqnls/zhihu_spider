# -*- coding: utf-8 -*-
import scrapy
from ZhiHu.settings import COOKIES, DEFAULT_REQUEST_HEADERS
from http.cookies import SimpleCookie

class PeopleRelationsSpider(scrapy.Spider):
    name = "people_relations"
    allowed_domains = ["https://www.zhihu.com"]
    start_urls = ['https://www.zhihu.com/']


    # custom_settings = {
    #     "DEFAULT_REQUEST_HEADERRS":{
    #
    #     }
    # }

    def parse(self, response):
        pass

    def start_requests(self):
        cc = SimpleCookie(COOKIES)
        cc = {i.key: i.value for i in cc.values()}
        print(cc)
        return [scrapy.Request('https://www.zhihu.com/question/60673524', headers=DEFAULT_REQUEST_HEADERS,cookies=cc, callback=self.check)]

    def check(self, response):
        print(response.text)
        pass
