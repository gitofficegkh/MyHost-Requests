# encoding=utf8
import requests
import json
import re
def connect(cookie_string):
    url1 = "https://www.yun316.net/host/panel/3342"
    url2 = "https://www.yun316.net/data/host.php?act=renew&id=3342&planid=3342&m=1"
    my_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42',
        'cookie': cookie_string,
    }
    response = requests.post(url2, headers=my_headers)
    message = str()
    if response.status_code != 200: 
      checkin_code = 0
      message = f"{message}Status:error\n"
      message = f"{message}Reasons:Login fails, please check your cookie.\n"
      return checkin_code, message
    checkin_code = 1
    resp = json.loads(response.text)
    statu = resp["sta"]
    res = resp["msg"]
    if "ok" in resp["sta"]:
        statu = resp["msg"]
        response = requests.get(url1, headers=my_headers)
        obj = re.compile(r"<tr><td>到期时间</td><td>(?P<time>.*?)</td>")
        it = obj.finditer(response.text)
        for i in it:
            res = i.group("time")
        message = f"{message}Status:{statu}\n"
        message = f"{message}Extime:{res}\n"
    else:
        message = f"{message}Status:{statu}\n"
        message = f"{message}Reasons:{res}\n"
    return checkin_code, message
