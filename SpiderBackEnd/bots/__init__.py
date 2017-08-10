#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-10 下午2:22
# @Author  : Lee
# @File    : __init__.py.py


def setup_django_env():
    import os, django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SpiderBckEnd.settings")
    django.setup()


def check_db_connection():
    from django.db import connection

    if connection.connection:
        #NOTE: (zacky, 2016.MAR.21st) IF CONNECTION IS CLOSED BY BACKEND, CLOSE IT AT DJANGO, WHICH WILL BE SETUP AFTERWARDS.
        if not connection.is_usable():
            connection.close()