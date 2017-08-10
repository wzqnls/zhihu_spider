#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-7 上午10:47
# @Author  : Lee
# @File    : for_cookies.py

import json

from SpiderBackEnd.bots.ZhiHu import CAPTCHA_PATH
from SpiderBackEnd.bots.ZhiHu import LoginZhihu


def get_cookies():
    someone = LoginZhihu()
    someone.login()
    with open(CAPTCHA_PATH, 'rt', encoding='utf8') as f:
        for line in f:
            cookies = json.loads(line)
            return cookies
