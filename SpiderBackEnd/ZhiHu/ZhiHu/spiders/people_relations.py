# -*- coding: utf-8 -*-

from urllib import parse

import scrapy
from ZhiHu.utils.for_cookies import get_cookies
from scrapy.http import Request

from ZhiHu.items import PeopleInfoItem, PeopleInfoItemLoader


class PeopleRelationsSpider(scrapy.Spider):
    name = "people_relations"
    allowed_domains = ["https://www.zhihu.com"]
    start_urls = ['https://www.zhihu.com/']

    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com/people/li-shuo-1-31/following', cookies=get_cookies(), callback=self.parse)]

    def parse(self, response):
        single_page_urls = response.css('#Profile-following .List-item .ContentItem-head a[class=UserLink-link]::attr(href)').extract()

        for rest_url in single_page_urls:
            # 拼接关注页面url
            rest_url += '/following'
            url = parse.urljoin(response.url, rest_url)
            yield Request(url=url, callback=self.parse_info)
            yield Request(url=url, callback=self.parse)

        page_nums_list = response.css('.Pagination button::text').extract()
        if '下一页' in page_nums_list:
            nums = int(page_nums_list[-2])
            for num in range(2, nums+1):
                # 构造下页url
                next_url = response.url + "?page={}".format(num)
                yield Request(url=next_url, callback=self.parse)

    def parse_info(self, response):
        item_loader = PeopleInfoItemLoader(item=PeopleInfoItem(), response=response)
        item_loader.add_css("name", ".ProfileHeader-name::text")
        item_loader.add_css("signature", ".ProfileHeader-headline::text")
        item_loader.add_css("gender", ".Icon--male")
        item_loader.add_css("pic_url", ".ProfileHeader-avatar .Avatar--large::attr(src)")
        item_loader.add_value("url", response.url)
        item_loader.add_value("id", response.url.split('/')[-2])
        item_loader.add_value("follows", self.get_follow_nums(response.url))
        item_loader.add_value("followers", self.get_follow_nums(response.url[:-3] + "ers"))

    @staticmethod
    def get_follow_nums(url):
        pass
