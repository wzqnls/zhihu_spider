#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-7 上午10:47
# @Author  : Lee
# @File    : for_cookies.py

import json

from ZhiHu.settings import COOKIES_PATH
from ZhiHu.common.login_zhihu import LoginZhihu


def get_cookies():
    user = LoginZhihu()
    user.login()
    with open(COOKIES_PATH, 'rt', encoding='utf8') as f:
        for line in f:
            cookies = json.loads(line)
            return cookies
