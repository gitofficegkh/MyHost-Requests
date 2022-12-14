# encoding=utf8
import requests
import json
import re
def getextime(cookie_string):
    url1 = "https://www.yun316.net/host/panel/3342"
    my_headers1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42',
        'cookie': cookie_string,
    }
    response = requests.get(url1, headers=my_headers1, verify=False)
    obj = re.compile(r"<tr><td>到期时间</td><td>(?P<time>.*?)</td>")
    it = obj.finditer(response.text)
    res='未知'
    for i in it:
        res = i.group("time")
    return res
            
def connect(cookie_string):
    url2 = "https://www.yun316.net/data/host.php?act=renew&id=3342&planid=3342&m=1"
    my_headers2 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42',
        'cookie': cookie_string,
    }
    response = requests.get(url2, headers=my_headers2, verify=False)
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
    # message = f"{message}Status:{statu}\n"
    # message = f"{message}Reasons:{res}\n"
    if "ok" in resp["sta"]:
        statu = resp["msg"]
        res = getextime(cookie_string)
        message = f"{message}Status:{statu}\n"
        message = f"{message}Extime:{res}\n"
    else:
        message = f"{message}Status:{statu}\n"
        message = f"{message}Reasons:{res}\n"
    return checkin_code, message
