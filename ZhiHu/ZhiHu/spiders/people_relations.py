# -*- coding: utf-8 -*-
import os
import pickle
import json
import scrapy
from ZhiHu.settings import COOKIES, DEFAULT_REQUEST_HEADERS
from http.cookies import SimpleCookie
from ZhiHu.settings import PROJECT_DIR

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
        cookies_path = PROJECT_DIR + "/common/cookies.txt"
        with open(cookies_path, 'r', encoding='utf8') as f:
            print(f.read())
            # cookies = pickle.load(f)
            # cc = SimpleCookie(f)
            # cc = {i.key: i.value for i in cc.values()}
            cc = json.load(f)
            # print(cc)
            return [scrapy.Request('https://www.zhihu.com/question/60673524', headers=DEFAULT_REQUEST_HEADERS,cookies=cc, callback=self.check)]

    def check(self, response):
        print(response.text)
        pass
