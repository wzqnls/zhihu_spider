#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 21:36
# @Author  : Lee
# @File    : main.py
# @Software: PyCharm

from scrapy import cmdline


cmdline.execute("scrapy crawl people_relations".split())