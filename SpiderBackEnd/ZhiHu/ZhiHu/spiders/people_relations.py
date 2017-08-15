# -*- coding: utf-8 -*-

import json
from urllib import parse

import scrapy
from scrapy.http import Request

from ZhiHu.utils.for_cookies import get_cookies
from ZhiHu.utils.tools import get_num_from_str
from ZhiHu.items import PeopleInfoItem



class PeopleRelationsSpider(scrapy.Spider):
    name = "people_relations"
    allowed_domains = ["https://www.zhihu.com"]
    api_url = "https://www.zhihu.com/api/v4/members/{user}/followees?" \
              "include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%" \
              "2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&" \
              "offset={offset}&limit={limit}"
    user_url = "https://www.zhihu.com/people/li-shuo-1-31/activities"

    def start_requests(self):
        yield scrapy.Request(self.user_url, cookies=get_cookies(), callback=self.parse_userinfo)
        # return scrapy.Request(self.api_url.format(user="li-shuo-1-31", offset=0, limit=20), cookies=get_cookies(), callback=self.parse)

    def parse_userinfo(self, response):
        item = PeopleInfoItem()
        info_part1 = response.css("industry", ".ProfileHeader-info .ProfileHeader-infoItem::text").extract()

        # 行业,职业,教育信息
        try:
            item["industry"] = info_part1[0]
        except IndexError:
            item["industry"] = ""
        try:
            item["job_history"] = info_part1[1]
        except IndexError:
            item["job_history"] = ""
        try:
            item["education"] = info_part1[2]
        except IndexError:
            item["education"] = ""

        # 回答、提问、文章、专栏、分享数值
        info_part2 = response.css(".Tabs-item .Tabs-link span::text").extract()
        item["answer_count"] = info_part2[0]
        item["question_count"] = info_part2[1]
        item["articles_count"] = info_part2[2]
        item["special_column_count"] = info_part2[3]
        item["share_count"] = info_part2[4]

        # 赞同数
        approval_info = response.css(".Card .IconGraf::text").extract()
        item["approval_num"] = int(get_num_from_str(approval_info))










    # def parse(self, response):
    #     single_page_urls = response.css('#Profile-following .List-item .ContentItem-head a[class=UserLink-link]::attr(href)').extract()
    #
    #     for rest_url in single_page_urls:
    #         # 拼接关注页面url
    #         rest_url += '/following'
    #         url = parse.urljoin(response.url, rest_url)
    #         yield Request(url=url, callback=self.parse_info)
    #         yield Request(url=url, callback=self.parse)
    #
    #     page_nums_list = response.css('.Pagination button::text').extract()
    #     if '下一页' in page_nums_list:
    #         nums = int(page_nums_list[-2])
    #         for num in range(2, nums+1):
    #             # 构造下页url
    #             next_url = response.url + "?page={}".format(num)
    #             yield Request(url=next_url, callback=self.parse)
    #
    # def parse_info(self, response):
    #     item_loader = PeopleInfoItemLoader(item=PeopleInfoItem(), response=response)
    #     item_loader.add_css("name", ".ProfileHeader-name::text")
    #     item_loader.add_css("signature", ".ProfileHeader-headline::text")
    #     item_loader.add_css("gender", ".Icon--male")
    #     item_loader.add_css("pic_url", ".ProfileHeader-avatar .Avatar--large::attr(src)")
    #     item_loader.add_value("url", response.url)
    #     item_loader.add_value("id", response.url.split('/')[-2])
    #     item_loader.add_value("follows", self.get_follow_nums(response.url))
    #     item_loader.add_value("followers", self.get_follow_nums(response.url[:-3] + "ers"))

