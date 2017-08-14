#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 21:41
# @Author  : Lee
# @File    : login_zhihu.py
# @Software: PyCharm

import json
import os
import re
import time

import requests
from PIL import Image

from ZhiHu.settings import CAPTCHA_PATH, COOKIES_PATH
from ZhiHu.settings import DEFAULT_REQUEST_HEADERS


class LoginZhihu(object):
    def __init__(self):
        # self.phone_num = input("phone_num\n")
        # self.password = input("password\n")
        self.phone_num = os.getenv('phone_num')
        self.password = os.getenv('password')
        self.captcha = ""
        self._xsrf = ""
        self.url = "https://www.zhihu.com"

        self.session = requests.session()

    def get_xsrf(self, url):
        index_page = self.session.get(url, headers=DEFAULT_REQUEST_HEADERS)
        html = index_page.text
        pattern = r'name="_xsrf" value="(.*?)"'
        _xsrf = re.findall(pattern, html)
        return _xsrf[0]

    def get_captcha(self):
        t = str(int(time.time() * 1000))
        captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
        r = self.session.get(captcha_url, headers=DEFAULT_REQUEST_HEADERS)
        with open(CAPTCHA_PATH, 'wb') as f:
            f.write(r.content)
            f.close()

        im = Image.open(CAPTCHA_PATH)
        im.show()
        im.close()

        captcha = input("please input the captcha\n>")
        return captcha

    def login(self):
        post_url = 'https://www.zhihu.com/login/phone_num'
        postdata = {
            '_xsrf': self.get_xsrf(self.url),
            'password': self.password,
            'remember_me': 'true',
            'phone_num': self.phone_num,
            "captcha": self.get_captcha()
        }
        login_page = self.session.post(post_url, data=postdata, headers=DEFAULT_REQUEST_HEADERS)

        with open(COOKIES_PATH, 'w') as f:

            # f.write(json.dump(self.session.cookies.get_dict()))
            json.dump(self.session.cookies.get_dict(), f)
            print("获取并保存cookie成功！")


