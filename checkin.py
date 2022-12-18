# encoding=utf8
import requests
import json
import time
import re
import os
def getextime(cookie_string):
    base_url=os.environ.get("HOST", None)
    url1 = base_url+'/host/panel/3342'
    my_headers1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42',
        'cookie': cookie_string,
        'referer': base_url+'/host/manager',
    }
    response = requests.get(url1, headers=my_headers1, verify=False)
    obj = re.compile(r"<tr><td>到期时间</td><td>(?P<time>.*?)</td>")
    it = obj.finditer(response.text)
    res='未知'
    for i in it:
        res = i.group("time")
    return res
            
def connect(cookie_string):
    base_url=os.environ.get("HOST", None)
    url2 = base_url+'/data/host.php?act=renew&id=3342&planid=3342&m=1'
    my_headers2 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42',
        'cookie': cookie_string,
        'referer': base_url+'/host/panel/3342',
        'sec-ch-ua': "Not?A_Brand;v=8, Chromium;v=108, Microsoft Edge;v=108",
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
    }
    time.sleep(6)
    response = requests.post(url2, headers=my_headers2, proxies={'https':'60.169.96.72:8089'})
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
        res = getextime(cookie_string)
        message = f"{message}Status:{statu}\n"
        message = f"{message}Extime:{res}\n"
    else:
        message = f"{message}Status:{statu}\n"
        message = f"{message}Reasons:{res}\n"
    return checkin_code, message
