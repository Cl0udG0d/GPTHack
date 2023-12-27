#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/26 10:47
# @Author  : Cl0udG0d
# @File    : test.py
# @Github: https://github.com/Cl0udG0d

import requests
import json
def get_format_data( prompt, parentMessageId):
    return {"prompt": prompt,
            "options": {
                "parentMessageId": parentMessageId
            },
            "systemMessage": "你是ChatGPT，一个由OpenAI训练的大型语言模型。尽可能详细而准确地回答我们提出的问题 谢谢\n"}
url = 'http://54.215.187.30:3003'
data = get_format_data("python读取文件",'chatcmpl-8aJrT2IqZKiraL2JwqXjZ32aVktgT')
session = requests.Session()
with session.post(f"{url}/api/chat-process", json=data, stream=True) as response:
    response.raise_for_status()

    for line in response.iter_lines():
        if line == b"<script>":
            raise RuntimeError("Solve challenge and pass cookies")

        if b"platform's risk control" in line:
            raise RuntimeError("Platform's Risk Control")
        if line:
            # 进行其他操作或处理逻辑
            last_line = line
    print(last_line)

data = get_format_data("文件名是test.txt",'chatcmpl-8aJrT2IqZKiraL2JwqXjZ32aVktgT')
with session.post(f"{url}/api/chat-process", json=data, stream=False) as response:
    response.raise_for_status()

    for line in response.iter_lines():
        if line == b"<script>":
            raise RuntimeError("Solve challenge and pass cookies")

        if b"platform's risk control" in line:
            raise RuntimeError("Platform's Risk Control")
        data = json.loads(line)
        print(data['text'])

import json

import requests

# from core.chatgpt_web.chatgpt import ChatGpt
#
# url = 'http://192.3.231.28:8016'
# url2 = 'http://47.236.41.161:3002'
# url1 = 'http://54.215.187.30:3003'
# # ChatGpt.check_alive(url1)
# list1=['https://113.218.241.217:7788', 'http://192.3.231.28:8016', 'http://47.236.41.161:3002', 'http://64.110.91.208:3002', 'http://146.56.147.68:3000', 'http://155.138.214.176:3002', 'https://82.157.152.110:1503', 'http://112.74.47.122:3003', 'http://172.233.75.229:18000', 'http://43.129.184.225:3002', 'http://104.221.226.18:4002', 'http://183.14.24.234:2020', 'http://139.199.230.64:3002', 'http://119.108.48.60:3002', 'http://47.107.77.252:3000', 'http://168.138.199.119:3002', 'http://113.109.15.114:3002', 'http://107.173.153.125:3000', 'https://gpt.dftianyi.com', 'http://221.122.68.144:50001', 'http://60.179.75.156:3002', 'http://74.48.4.213:3002', 'https://27.189.127.151:8848', 'http://server2.shancn.com:3000', 'http://ai.shancn.com:3000', 'https://leilou.xyz:30003', 'http://43.153.56.158:2023', 'https://13.213.31.217:30003', 'https://api.1479284.xyz', 'http://149.88.70.95:3000', 'http://95.214.164.121:3002', 'https://page.raindropcover.xyz', 'http://113.251.87.151:9998', 'http://23.95.39.103:3636', 'http://218.20.221.124:9002', 'http://144.202.108.183:3000', 'http://117.45.123.244:3000', 'https://175.0.37.232:3002', 'https://114.216.50.170:3002', 'http://107.173.83.227:2086', 'https://chat.imgnest.xyz', 'https://nevermore.littleboomfish.xyz', 'http://nevermore.littleboomfish.xyz', 'http://81.68.107.147:3002', 'http://165.154.145.147:3002', 'http://175.178.126.228:3002', 'http://27.124.22.4:3000', 'https://aichat.ccbbee.xyz', 'http://aichat.ccbbee.xyz', 'http://222.90.12.5:3002','https://aichat.ccbbee.xyz', 'http://aichat.ccbbee.xyz', 'http://222.90.12.5:3002', 'https://gpt.cccoding.xyz', 'https://chat.ttuuvv.xyz', 'http://chat.tl2000.top', 'https://chat.tl2000.top', 'https://144.255.18.79:2087', 'https://192.9.147.73', 'https://chat.zhaoqian.me', 'https://192.9.147.102', 'http://123.249.21.26:3002', 'http://60.208.55.5:3000', 'http://www.garytb.xyz', 'http://kf.garytb.xyz', 'http://kefu.guotaijunanhye.xyz', 'http://43.153.58.72:3002', 'http://108.165.254.104:3002', 'https://149.88.68.43:8443', 'https://pay.beisu100.com', 'http://155.94.197.93:3002', 'https://chatweb.200311.xyz', 'https://ai.961114.xyz', 'http://ai.961114.xyz', 'http://205.234.157.197:3002', 'http://14.104.85.231:32768', 'http://104.168.154.44:3002', 'https://60.186.218.12:3000', 'http://113.227.140.68:3002', 'http://103.218.243.142', 'http://114.240.227.137:3002', 'http://kefu.gtjanweb.xyz', 'http://13.59.17.148:3000', 'http://ai.323985.xyz', 'https://198.44.179.243', 'http://113.89.232.145:3002', 'https://165.154.10.43', 'http://13.230.162.166:3002', 'http://106.52.253.46', 'https://www.ai516.top', 'https://ai516.top', 'https://149.88.70.8', 'http://106.55.250.52:3003', 'https://190.92.238.32', 'https://35.86.69.20', 'http://115.28.138.73:3002', 'http://107.150.103.174', 'http://115.219.237.170:3002', 'http://113.251.65.56:9998', 'http://175.178.46.53:8112','http://139.224.191.22:3002', 'http://43.200.171.101:3002', 'http://113.250.144.154:3003', 'http://113.251.230.171:3002', 'http://113.250.144.157:3003', 'http://159.75.81.167:3002', 'https://20.205.139.84', 'http://fq.815360296.xyz:8888', 'http://27.8.252.254:3002', 'https://assistant.51604550.xyz', 'http://114.219.149.3:3002', 'https://45.32.225.166', 'https://115.192.187.39:3000', 'http://122.243.86.59:3002', 'http://139.185.32.125:3002', 'http://149.129.86.229:3030', 'http://39.96.64.176:3002', 'http://115.218.121.54:49156', 'http://148.135.34.218:8080', 'http://20.232.22.130:8080', 'http://164.152.47.218:8080', 'https://103.116.246.153', 'http://39.98.113.41:8080', 'https://121.91.174.9', 'http://115.219.239.65:3002', 'https://chatgpt.ericsandbox.xyz:8443', 'http://xmz.125816.xyz:3002', 'https://ai.150527.xyz', 'http://155.248.214.46:3002', 'https://ai.jkhuang.xyz', 'http://hh.xqyhr.xyz:3002', 'http://chatgpdv1.hwflll.cn', 'https://117.50.183.51', 'http://115.231.218.100:3002', 'http://168.138.220.26:3002', 'http://58.212.41.77:3002', 'http://106.55.224.130:3002', 'http://183.45.76.60:3002', 'https://chatme.2345781.xyz', 'https://chattoai.05739527.xyz', 'https://chat.aier688.com', 'http://123.6.102.217:3002', 'http://www.aichatapp.top', 'https://www.aichatapp.top', 'https://54.183.21.72', 'https://www.aier688.com', 'https://ai2.chendeyun.xyz', 'https://ai.chendeyun.xyz', 'https://210.87.202.219', 'http://chatgpt.tsykx.top','http://www.hongbi.xyz:3002', 'http://153.3.80.215:3002', 'http://107.150.102.48', 'https://azai.wwg.xyz', 'http://54.82.202.177', 'http://116.16.198.120:3002', 'http://chat.zxp.xyz', 'http://23.105.220.10:3002', 'http://116.63.196.170', 'http://45.92.158.93:2082', 'http://54.248.73.124:3002', 'http://107.175.245.129', 'https://chat.weihanli.xyz', 'https://chat-a.weihanli.xyz', 'http://3.136.29.140', 'http://112.124.32.247', 'http://123.122.162.243:50003', 'http://47.251.44.93', 'http://43.153.47.115', 'http://38.47.226.51', 'http://www.chatgpt.test.hsgitlab.xyz', 'http://124.221.132.41', 'http://124.223.21.98', 'http://124.222.174.99', 'http://124.221.78.219', 'http://117.83.17.81:3002', 'http://47.108.148.194', 'http://120.24.205.6', 'http://ai.heiya.xyz', 'https://chat.heier.xyz', 'http://165.154.133.138:3002', 'https://api.deempay.com', 'http://api.deempay.com', 'https://3.9.29.59', 'http://1.92.69.52', 'http://43.153.171.167:3002', 'http://123.122.163.61:50003', 'http://116.62.143.15:8888', 'http://chat.aionlife.xyz', 'http://linode.aionlife.xyz', 'https://chat.aionlife.xyz', 'https://linode.aionlife.xyz', 'http://222.95.252.102:3002', 'https://openai.lefoster.cn', 'https://106.52.103.135', 'http://220.130.116.51', 'http://185.242.233.118:3002', 'http://34.105.17.95:7880', 'http://113.92.157.140:3002', 'https://149.88.82.70']
# for i in list1:
#     ChatGpt.check_alive(i)

# data = json.loads(line)
# result = data['delta'] if 'delta' in data else ""
# print(result)
# yield result
