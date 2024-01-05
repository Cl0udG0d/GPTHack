import sys

from core.chatgpt_web.chatgpt import ChatGpt

site = "http://117.30.72.160:8005"
version_flag = ChatGpt.check_gpt_version(site)
print(version_flag)
