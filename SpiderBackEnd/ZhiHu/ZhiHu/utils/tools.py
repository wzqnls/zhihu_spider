#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-15 下午7:12
# @Author  : Lee
# @File    : tools.py

import re


def get_num_from_str(string):
    pattern = re.compile("\d+")
    return [int(i) for i in re.findall(pattern, string)]
