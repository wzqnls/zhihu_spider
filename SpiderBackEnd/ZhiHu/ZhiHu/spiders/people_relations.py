# -*- coding: utf-8 -*-

import json

import scrapy

from ZhiHu.utils.for_cookies import get_available_cookies
from ZhiHu.utils.tools import get_num_from_str
from ZhiHu.items import PeopleInfoItem


class PeopleRelationsSpider(scrapy.Spider):
    name = "people_relations"
    allowed_domains = ["https://www.zhihu.com"]
    user_api = "https://www.zhihu.com/api/v4/members/{user}"
    user_url = "https://www.zhihu.com/people/{user}/activities"
    start_user = "li-shuo-1-31"
    follow_url = "https://www.zhihu.com/api/v4/members/{user}/followees?" \
                 "include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%" \
                 "2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D." \
                 ".topics&limit=20&offset=0"
    followed_url = "https://www.zhihu.com/api/v4/members/{user}/relations/mutuals?" \
                   "nclude=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2C" \
                   "follower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D" \
                   ".topics&offset=0&limit=20"

    cookies = get_available_cookies()

    def start_requests(self):
        yield scrapy.Request(url=self.user_url.format(user=self.start_user), meta={"user": self.start_user},
                             cookies=self.cookies, callback=self.parse_userinfo)
        yield scrapy.Request(url=self.follow_url.format(user=self.start_user),
                             cookies=self.cookies, callback=self.parse_followinfo)
        yield scrapy.Request(url=self.followed_url.format(user=self.start_user),
                             cookies=self.cookies, callback=self.parse_followinfo)

    def parse_userinfo(self, response):
        item = PeopleInfoItem()

        # 行业,职业,教育信息
        work_info = response.css(".ProfileHeader-info .ProfileHeader-infoItem::text").extract()
        try:
            item["industry"] = work_info[0]
        except IndexError:
            item["industry"] = ""
        try:
            item["job_history"] = work_info[1]
        except IndexError:
            item["job_history"] = ""
        try:
            item["education"] = work_info[2]
        except IndexError:
            item["education"] = ""

        # 回答、提问、文章、专栏、分享数值
        question_info = response.css(".Tabs-item .Tabs-link span::text").extract()
        item["answer_count"] = question_info[0]
        item["question_count"] = question_info[1]
        item["articles_count"] = question_info[2]
        item["special_column_count"] = question_info[3]
        item["share_count"] = question_info[4]

        # 赞同数
        approval_info = response.css(".Card .IconGraf::text").extract()
        item["approval_num"] = get_num_from_str(approval_info[-1])[0] if len(approval_info) else 0

        # 感谢和收藏数
        praise_info = response.css(".Card .Profile-sideColumnItemValue::text").extract()
        if len(praise_info):
            item["thanks_num"], item["collected_num"] = [i for i in get_num_from_str(praise_info[-1])]
        else:
            item["thanks_num"], item["collected_num"] = 0, 0

        # 关注与被关注
        follow_info = response.css(".FollowshipCard-counts .NumberBoard-value::text").extract()
        item["followed_count"] = follow_info[0]
        item["follower_count"] = follow_info[1]


        # 其他关注部分
        # 部分用户没有赞助live信息，故对匹配结果多加一层判断
        other_follow_info = response.css(".Profile-lightList .Profile-lightItemValue::text").extract()
        if len(other_follow_info) == 5:
            item["follow_live_num"] = other_follow_info[0]
            item["follow_topic_num"] = other_follow_info[1]
            item["follow_special_column_num"] = other_follow_info[2]
            item["follow_question_num"] = other_follow_info[3]
            item["follow_collection_num"] = other_follow_info[4]
        else:
            item["follow_topic_num"] = other_follow_info[0]
            item["follow_special_column_num"] = other_follow_info[1]
            item["follow_question_num"] = other_follow_info[2]
            item["follow_collection_num"] = other_follow_info[3]

        yield scrapy.Request(url=self.user_api.format(user=response.meta.get("user")),
                             cookies=self.cookies, meta={"item": item},
                             callback=self.parse_userapi, dont_filter=True)

    def parse_userapi(self, response):
        data = json.loads(response.text)
        item = response.meta.get("item")

        item["id"] = data["id"]
        item["name"] = data["name"]
        item["headline"] = data["headline"]
        item["gender"] = data["gender"]
        item["url_token"] = data["url_token"]
        item["url"] = data["url"]
        item["avatar_url_template"] = data["avatar_url_template"]

        yield scrapy.Request(url=self.follow_url.format(user=data["url_token"]),
                             cookies=self.cookies, callback=self.parse_followinfo)
        yield scrapy.Request(url=self.followed_url.format(user=data["url_token"]),
                             cookies=self.cookies, callback=self.parse_followinfo)

        yield item

    def parse_followinfo(self, response):
        result = json.loads(response.text)
        page_info = result["paging"]
        data = result["data"]

        users = [obj["url_token"] for obj in data]
        for user in users:
            yield scrapy.Request(url=self.user_url.format(user=user), meta={"user": user},
                                 cookies=self.cookies, callback=self.parse_userinfo, dont_filter=True)

        if not page_info["is_end"]:
            next_url = page_info["next"]
            yield scrapy.Request(url=next_url, callback=self.parse_followinfo, cookies=self.cookies, dont_filter=True)
