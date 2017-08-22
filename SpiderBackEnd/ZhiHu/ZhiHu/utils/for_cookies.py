#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-7 上午10:47
# @Author  : Lee
# @File    : for_cookies.py

import os
import json
import requests
from functools import wraps

from ZhiHu.settings import COOKIES_PATH, DEFAULT_REQUEST_HEADERS
from ZhiHu.common.login_zhihu import LoginZhihu


def read_cookies():
    with open(COOKIES_PATH, 'rt', encoding='utf8') as f:
        for line in f:
            cookies = json.loads(line)
            return cookies


def check_cookies(func):

    @wraps(func)
    def wrapper():
        cookies = func()
        result = requests.get(url="https://www.zhihu.com/inbox", headers=DEFAULT_REQUEST_HEADERS,
                              cookies=cookies, allow_redirects=False)

        if result.status_code == 200:
            return cookies
        else:
            os.remove(COOKIES_PATH)
            LoginZhihu().login()
            if result.status_code == 200:
                return cookies
            else:
                return
    return wrapper


@check_cookies
def get_available_cookies():
    if os.path.exists(COOKIES_PATH):
        return read_cookies()
    else:
        LoginZhihu().login()
        return read_cookies()
