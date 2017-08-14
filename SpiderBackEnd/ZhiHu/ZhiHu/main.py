#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 21:36
# @Author  : Lee
# @File    : main.py
# @Software: PyCharm

from scrapy import cmdline

# from ZhiHu.common.login_zhihu import LoginZhihu


cmdline.execute("scrapy crawl people_relations".split())