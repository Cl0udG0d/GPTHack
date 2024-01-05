#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 18:02
# @Author  : Cl0udG0d
# @File    : background.py
# @Github: https://github.com/Cl0udG0d
from apscheduler.schedulers.background import BackgroundScheduler
import ping3

import config
from core.chatgpt_web.chatgpt import ChatGpt
from core.toolkit import get_file_line_count, sort_gpt_sitelist_from_list, set_new_gpt_site
import concurrent.futures
import threading

scheduler = BackgroundScheduler()

temp_site_list = list()
lock = threading.Lock()


def check_site_num():
    return get_file_line_count() > config.GPT_ALARM_NUM


def save_site2list(site):
    alive, execution_time = ChatGpt.check_alive(site)
    if alive:
        with lock:
            temp_site_list.append(f"{site}|{execution_time}\n")


def submit_thread_task(sitelist):
    with concurrent.futures.ThreadPoolExecutor(max_workers=config.THREADPOOL_NUM) as executor:
        futures = [executor.submit(save_site2list, site) for site in sitelist]
        concurrent.futures.wait(futures)


def is_connected(host=config.TEST_CONNECT_URL):
    return True if ping3.ping(host) else False


def check_gpt_alive():
    global temp_site_list
    urllist = list()
    with open(config.GPT_FILEPATH, "r") as file:
        lines = file.readlines()
        for line in lines:
            url = line.strip().split('|')[0]
            urllist.append(url)
    submit_thread_task(urllist)
    sort_gpt_sitelist_from_list(temp_site_list)
    temp_site_list = list()
    if config.DEBUG:
        print('检验存活结束')


def heartbeat():
    if config.DEBUG:
        print('定时任务正在执行...')
    if is_connected():
        check_gpt_alive()
        if not check_site_num():
            set_new_gpt_site()
    else:
        if config.DEBUG:
            print("网络不通")


scheduler.add_job(
    func=heartbeat,
    trigger='interval',
    seconds=config.HEARTBEAT_TIME
)

if __name__ == '__main__':
    print(is_connected())
