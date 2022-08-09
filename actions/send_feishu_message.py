#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/12 10:36 上午
# @Author  : ppj
# @File    : send_feishu_message.py
# @Software: PyCharm

from feishu_toolkit.robot import CustomRobot
import json

# 测试的飞书机器人，可以发信息到对应的群组
SECRET = "gJamvilRaRB3qKfyNqFx9c"
URL = "https://open.feishu.cn/open-apis/bot/v2/hook/67c5bffd-def5-4edc-b0cb-4e2756f17212"

def send_feedback_message(msg):
    robot = CustomRobot(secret=SECRET, url=URL)
    # 发送简单的文本
    robot.send_msg(msg=msg, msg_type='text')

    return []

# # 发送请求
# url = f'https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type={receive_id_type}'
# headers = {
#     'Content-Type': "application/json; charset=utf-8",
#     'Authorization': 'Bearer ' + self.access_token
# }
# data = {
#     'receive_id': receive_id,
#     'content': json.dumps(msg),
#     'msg_type': msg_type,
# }
# res = requests.post(url=url, json=data, headers=headers).json()