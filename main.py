#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/26 10:52
# @Author  : Cl0udG0d
# @File    : main.py
# @Github: https://github.com/Cl0udG0d
import os



import config
from core.chatgpt_web.chatgpt import ChatGpt
from core.toolkit import get_file_line_count, sort_gpt_sitelist, set_new_gpt_site
from gui import run_gui

# 创建互斥锁







def init_config():
    config.ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    config.GPT_FILEPATH = os.path.join(config.ROOT_DIRECTORY, config.FILENAME)





def init():
    print("初始化中...")
    init_config()
    line_count = get_file_line_count()
    if line_count > 0:
        pass
    else:
        set_new_gpt_site()
    print("初始化结束")


def test_init():
    with open(config.GPT_FILEPATH, "r") as file:
        lines = file.readlines()
        for line in lines:
            url = line.strip().split('|')[0]
            print(url)

def test():
    init()
    test_init()

if __name__ == '__main__':
    init()
    run_gui(config.HOST, config.PORT, config.DEBUG)
    # test()
