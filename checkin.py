# encoding=utf8
import requests
import json
def glados(cookie_string):
    # 灰狼云续费url
    url2 = "https://www.yun316.net/data/host.php?act=renew&id=3342&planid=3342&m=1"
    my_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42',
        'cookie': cookie_string,
}
    response = requests.post(url2, headers=my_headers)
    message = str()
    if response.status_code != 200: 
      checkin_code = -2
      message = f"{message}Status:error\n"
      message = f"{message}Checkin:Login fails, please check your cookie.\n"
      return checkin_code, message
    print(response.text)  # response.text和浏览器返回数据相同说明post数据成功
    checkin_code = 1
    resp = json.loads(response.text)
    message = f"{message}Status:{resp["sta"]}\n"
    message = f"{message}Checkin:{resp["msg"]}\n"
    return checkin_code, message
