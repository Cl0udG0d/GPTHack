#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 18:02
# @Author  : Cl0udG0d
# @File    : background.py
# @Github: https://github.com/Cl0udG0d
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

def job_function():
    print("定时任务执行了！")

# 创建定时任务，每隔5秒钟执行一次
scheduler = BackgroundScheduler()
scheduler.add_job(func=job_function, trigger="interval", seconds=5)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
