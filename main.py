# encoding=utf8
import os
import re
import argparse

from checkin import checkin
from messageSender import MessageSender

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--cookie_string", type=str, required=True)

    args= parser.parse_args()
    cookie_string = args.cookie_string
    pushplus_token = os.environ.get("PUSHPLUS_TOKEN", None)
    serverChan_sendkey = os.environ.get("SERVERCHAN_SENDKEY", None)
    weCom_webhook = os.environ.get("WECOM_WEBHOOK", None)
    bark_deviceKey = os.environ.get("BARK_DEVICEKEY", None)

    message_tokens = {
        "pushplus_token": pushplus_token,
        "serverChan_token": serverChan_sendkey,
        "weCom_webhook": weCom_webhook,
        "bark_deviceKey": bark_deviceKey
    }

    message_sender = MessageSender()

    # message_all = str()
    # message_all = f"{message_all}访问结果\n"
    checkin_code, message = glados(cookie_string)
    # message_all = f"{message_all}{message}\n"

    if checkin_codes != 0:
        title = "灰狼云访问成功"
    else:
        title = "灰狼云访问失败"
    message_all = f"{title}\n{message}"
    message_all = re.sub("\n+","\n", message_all)
    if message_all.endswith("\n"): message_all = message_all[:-1]
    message_sender.send_all(message_tokens= message_tokens, title = title, content = message_all)
