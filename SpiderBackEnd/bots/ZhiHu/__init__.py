#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-9 上午10:55
# @Author  : Lee
# @File    : __init__.py


def setup_django_env():
    import os, django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BackEnd.settings")
    django.setup()


def check_db_connection():
    from django.db import connection

    if connection.connection:
        if not connection.is_usable():
            connection.close()