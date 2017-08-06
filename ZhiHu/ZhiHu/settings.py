# -*- coding: utf-8 -*-

# Scrapy settings for ZhiHu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os
import sys


BOT_NAME = 'ZhiHu'

SPIDER_MODULES = ['ZhiHu.spiders']
NEWSPIDER_MODULE = 'ZhiHu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
COOKIES = 'q_c1=2235fd1d6abb446d8b1c7c2a284ad931|1501254555000|1501254555000; _zap=51d9efc5-ffaa-4511-8b0e-bb23e7a82dca; q_c1=f47f231ea2d34c3fab30ccd2cebbc7f5|1501254555000|1501254555000; aliyungf_tc=AQAAAJBdz3d6WAcAeCDAc8BnUqMMVJdk; _xsrf=4a4eeb52d21b38d8141cd9b55b7d164c; r_cap_id="NDk2MzAxYWU4MzQxNDBkNThiMTMzYThkMzk3NjQ5NGU=|1501679872|9cfe557c5963747f589ef374ca9a364463f0847b"; cap_id="Y2EwYTk4Yjc1ODBmNGFhZWJmYWRkNDkzZGMxZjM3OTg=|1501679872|dceae1e524e938652891018749dc5e78d5843a18"; d_c0="AFBCUMnZKAyPTh4TRH2LtMBJQ5Ax8SisCKk=|1501679876"; l_n_c=1; z_c0=Mi4wQUFDQWFjQXRBQUFBVUVKUXlka29EQmNBQUFCaEFsVk5ERjZwV1FEb3FSVXFDdDd0ZnhaZkZqVFdhUUdHRVBrcFBn|1501679884|94c8ddfd60c07106cf1fac50ea7a01c92c8bac38; __utma=155987696.224393165.1501680284.1501680284.1501680284.1; __utmc=155987696; __utmz=155987696.1501680284.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _xsrf=4a4eeb52d21b38d8141cd9b55b7d164c'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
  'Accept-Encoding': 'gzip, deflate, br',
  'Connection': 'keep-alive',
  'HOST': "www.zhihu.com",
  'Referer': "https://www.zhihu.com",
  'User-Agent': USER_AGENT
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ZhiHu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ZhiHu.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'ZhiHu.pipelines.ZhihuPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 项目路径
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)
sys.path.insert(0, os.path.join(BASE_DIR))