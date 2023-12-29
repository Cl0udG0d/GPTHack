#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/26 10:55
# @Author  : Cl0udG0d
# @File    : config.py
# @Github: https://github.com/Cl0udG0d

# 定时任务检测时间 心跳时间 默认三十分钟检测一次
HEARTBEAT_TIME = 60*30

# 初始爬取数量
INIT_SEARCH_NUM = 100

# FOFA搜索关键字
FOFA_SEARCH_KEY = 'title=="ChatGPT Web"'

# 版本号
VERSION = '0.0.1'

# POST传输超时时间
POST_TIMEOUT = 6

# 线程池数量
THREADPOOL_NUM = 10

# 可用GPT存储文本名称
FILENAME = "gpthack.txt"

# 项目根路径
ROOT_DIRECTORY = ""
# 可用GPT存储文本路径
GPT_FILEPATH = ""

# 测试连通性域名
TEST_CONNECT_URL = "www.baidu.com"

GPT_ALARM_NUM = 2

#=======================================================================================================================
# FLASK 配置相关
HOST = ""
PORT = 8080
DEBUG = False

TEMPLATE_FOLDER_PATH = ""
STATIC_FOLDER_PATH = ""