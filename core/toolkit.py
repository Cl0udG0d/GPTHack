#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/28 11:39
# @Author  : Cl0udG0d
# @File    : toolkit.py
# @Github: https://github.com/Cl0udG0d
import os

from fofa_hack import fofa
import concurrent.futures
import config
from core.chatgpt_web.chatgpt import ChatGpt
import threading

lock = threading.Lock()


def get_file_line_count():
    if not os.path.exists(config.GPT_FILEPATH):
        return 0
    with open(config.GPT_FILEPATH, "r") as file:
        line_count = sum(1 for line in file)
    return line_count


def sort_gpt_sitelist():
    with open(config.FILENAME, "r+") as file:
        lines = file.readlines()

        # 将每行的数据拆分成元组 (line, number)，并按照数字进行排序
        sorted_lines = sorted(lines, key=lambda x: float(x.split("|")[1]))

        # 清空文件内容
        file.seek(0)
        file.truncate()

        # 写入排序结果到文件
        for line in sorted_lines:
            file.write(f"{line}")


def sort_gpt_sitelist_from_list(urllist):
    with open(config.FILENAME, "r+") as file:
        # 将每行的数据拆分成元组 (line, number)，并按照数字进行排序
        sorted_lines = sorted(urllist, key=lambda x: float(x.split("|")[1]))

        # 清空文件内容
        file.seek(0)
        file.truncate()

        # 写入排序结果到文件
        for line in sorted_lines:
            file.write(f"{line}")


def save_site(site):
    alive, execution_time = ChatGpt.check_alive(site)
    if alive:
        if ChatGpt.check_gpt_version(site):
            with lock:
                with open(config.FILENAME, "a") as file:
                    file.write(f"{site}|{execution_time}\n")


def submit_thread_task(sitelist):
    with concurrent.futures.ThreadPoolExecutor(max_workers=config.THREADPOOL_NUM) as executor:
        futures = [executor.submit(save_site, site) for site in sitelist]
        concurrent.futures.wait(futures)


def get_gpt_site():
    return fofa.api(config.FOFA_SEARCH_KEY, endcount=config.INIT_SEARCH_NUM)


# 重置gpt地址
def set_new_gpt_site():
    print('GPT地址重置')
    for sitelist in get_gpt_site():
        submit_thread_task(sitelist)
    sort_gpt_sitelist()
