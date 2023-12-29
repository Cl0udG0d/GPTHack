#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/28 17:49
# @Author  : Cl0udG0d
# @File    : init.py
# @Github: https://github.com/Cl0udG0d
import os
import sys
import config

if getattr(sys, 'frozen', False):
    config.ROOT_DIRECTORY = os.path.dirname(sys.executable)
    config.GPT_FILEPATH = os.path.join(config.ROOT_DIRECTORY, config.FILENAME)
    config.TEMPLATE_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)) , "templates")
    config.STATIC_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
else:
    config.ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    config.GPT_FILEPATH = os.path.join(config.ROOT_DIRECTORY, config.FILENAME)
    config.TEMPLATE_FOLDER_PATH = os.path.join(config.ROOT_DIRECTORY, "gui/client/html")
    config.STATIC_FOLDER_PATH = os.path.join(config.ROOT_DIRECTORY, "gui/client")
# print("config.ROOT_DIRECTORY "+config.ROOT_DIRECTORY)
# print("config.GPT_FILEPATH " + config.GPT_FILEPATH)
# print("config.TEMPLATE_FOLDER_PATH " + config.TEMPLATE_FOLDER_PATH)
# print("config.STATIC_FOLDER_PATH " + config.STATIC_FOLDER_PATH)