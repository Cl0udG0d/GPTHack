#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/26 17:27
# @Author  : Cl0udG0d
# @File    : chatgpt.py
# @Github: https://github.com/Cl0udG0d
import json
import time

import requests
from typing import Union

import config
from core.chatgpt_web.type import CreateResult, Messages
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ChatGpt():
    session_data = {}

    @classmethod
    def get_empty_data(cls, prompt):
        return {"prompt": prompt, "options": {},
                "systemMessage": "你是ChatGPT，一个由OpenAI训练的大型语言模型。尽可能详细而准确地回答我们提出的问题 谢谢\n"}

    @classmethod
    def get_format_data(cls, prompt, parentMessageId):
        return {"prompt": prompt,
                "options": {
                    "parentMessageId": parentMessageId
                },
                "systemMessage": "你是ChatGPT，一个由OpenAI训练的大型语言模型。尽可能详细而准确地回答我们提出的问题 谢谢\n"}

    @classmethod
    def get_response(cls, url):
        try:
            response = requests.post(f"{url}/api/chat-process", json=cls.get_empty_data("hi"),
                                     timeout=config.POST_TIMEOUT, verify=False)
            response.raise_for_status()
            last_line = None
            for line in response.iter_lines():

                if line:
                    # 进行其他操作或处理逻辑
                    last_line = line
            return last_line
        except Exception as e:
            print(e)
            return None

    @classmethod
    def get_parentMessageId(cls,
                            conversation_id: str):
        if cls.session_data.get(conversation_id):
            return cls.session_data.get(conversation_id)
        return ""

    @classmethod
    def get_new_gpt_site(cls):
        # print(config.ROOT_DIRECTORY)
        # print(config.GPT_FILEPATH)
        with open(config.GPT_FILEPATH, "r") as file:
            first_line = file.readline()

        if first_line:
            return first_line.split('|')[0]
        return ""

    @classmethod
    def create_completion(
            cls,
            conversation_id: str,
            messages: Messages,
            stream: bool,
            **kwargs
    ) -> CreateResult:
        # url = cls.get_new_gpt_site()
        url = "http://139.199.230.64:3002"
        prompt = messages[-1]["content"]
        parentMessageId = cls.get_parentMessageId(conversation_id)
        data = cls.get_format_data(prompt, parentMessageId)
        print(data)
        session = requests.Session()
        last_line = None
        with session.post(f"{url}/api/chat-process", json=data, stream=stream) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line == b"<script>":
                    raise RuntimeError("Solve challenge and pass cookies")

                if b"platform's risk control" in line:
                    raise RuntimeError("Platform's Risk Control")

                if line:
                    # 进行其他操作或处理逻辑
                    last_line = line
                data = json.loads(line)
                result = data['delta'] if 'delta' in data else ""
                yield result
        line = json.loads(last_line)
        cls.session_data[conversation_id] = line['id']

    @classmethod
    def create(cls,
               conversation_id: str,
               messages: Messages,
               stream: bool,
               **kwargs) -> Union[CreateResult, str]:
        result = cls.create_completion(
            conversation_id=conversation_id,
            messages=messages,
            stream=True
        )
        return result if stream else ''.join(result)

    @classmethod
    def check_alive(cls,
                    url):
        prompt = "hi"
        data = {"prompt": prompt, "options": {},
                "systemMessage": "你是ChatGPT，一个由OpenAI训练的大型语言模型。尽可能详细而准确地回答我们提出的问题 谢谢\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-12-26"}
        session = requests.Session()
        start_time = time.time()  # 记录开始时间
        try:
            with session.post(f"{url}/api/chat-process", json=data, stream=True, verify=False,
                              timeout=config.POST_TIMEOUT) as response:
                response.raise_for_status()

                for line in response.iter_lines():
                    last_line = None

                    if line:
                        # 进行其他操作或处理逻辑
                        last_line = line

                # 在循环结束后处理最后的流数据
                end_time = time.time()
                execution_time = end_time - start_time  # 计算执行时间
                if last_line is not None:
                    data = json.loads(last_line)
                    # print(data)
                    if 'text' in data and data['text'] != "" and (
                            data['text'].startswith("H") or data['text'].startswith("h")):
                        return True, execution_time
                    else:
                        return False, config.POST_TIMEOUT
        except Exception as e:
            print(e)
            return False, config.POST_TIMEOUT


if __name__ == '__main__':
    data = ChatGpt.get_response("http://54.215.187.30:3003")
    print(json.loads(data))
