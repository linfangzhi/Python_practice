import requests
import random
import time

def hex(ifhex=True,num=1):
    out = ''
    if ifhex is True:
        hexlist = list('123457890abcdef')
        for i in range(num):
            out += random.choice(hexlist)
        return out
    else:
        hexlist = list('123457890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        for i in range(num):
            out += random.choice(hexlist)
        return out



url = 'https://wxapi.szgalaxy.com/api/Community/PutPostReadQty?UserToken=Microt{}&oid=64cd00db-8f4c-4ad8-83d8-ef5a1087cd69'.format(hex(ifhex=False,num=22))
# proxy_url ='163.204.246.4:9999'
# UserToken = 'Microt{}'.format(hex(ifhex=False,num=22))
# proxies = {
#     'http': 'http://{proxy_url}'.format(proxy_url=proxy_url),
#     'https': 'https://{proxy_url}'.format(proxy_url=proxy_url),
# }
# header = {
#     'content-type':'application/x-www-form-urlencoded',
#     'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
#     'sec-fetch-site':'same-site',
#     'sec-fetch-mode':'cors',
#     'sec-fetch-dest':'empty',
#     'referer':'https://weixin2.szgalaxy.com/Community/Detail?Oid=64cd00db-8f4c-4ad8-83d8-ef5a1087cd69',
#     'origin': 'https://weixin2.szgalaxy.com',
#
# }
# url = 'https://wxapi.szgalaxy.com/api/Community/PutPostPraise?UserToken=Microt{}'.format(UserToken)
for i in range(26):
    a = requests.post(url=url,timeout=10)
    b = a.json()
    print(b['msg'])
    time.sleep(1)



