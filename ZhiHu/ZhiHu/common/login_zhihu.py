#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 21:41
# @Author  : Lee
# @File    : login_zhihu.py
# @Software: PyCharm

import re
import os
import time
import json
import pickle
import requests
from requests import utils
from http import cookies
from http import cookiejar

from PIL import Image
from ZhiHu.settings import USER_AGENT, COOKIES
from ZhiHu.settings import DEFAULT_REQUEST_HEADERS


class LoginZhihu(object):
    def __init__(self):
        # self.phone_num = input("phone_num\n")
        # self.password = input("password\n")
        self.captcha = ""
        self._xsrf = ""
        self.url = "https://www.zhihu.com"

        self.session = requests.session()
        # self.session.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')
        # try:
        #     self.session.cookies.load(ignore_discard=True)
        # except:
        #     pass

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
        with open('captcha.jpg', 'wb') as f:
            f.write(r.content)
            f.close()
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except:
            print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
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
        # self.session.cookies.save("cookies.txt")
        with open('cookies.txt', 'w') as f:
            # pickle.dump(self.session.cookies.get_dict(), f)
            # f.write(json.dump(self.session.cookies.get_dict()))
            json.dump(self.session.cookies.get_dict(), f)
            COOKIES = json.dumps()
            print("获取并保存cookie成功！")

if __name__ == '__main__':
    login_instance = LoginZhihu()
    login_instance.login()

