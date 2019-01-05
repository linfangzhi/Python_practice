import requests
import random
import time



for c in range(100):
    b = ''
    for i in range(1,21,):
        if i ==20:
            b = b + str(i) + '$' + str(random.randint(3, 5))
        else:
            b = b+str(i)+'$'+str(random.randint(3,5))+'}'
    #print(b)
    if time.localtime().tm_min<3:
        min = 0
    else:
        min = time.localtime().tm_min

    url = 'https://www.wjx.cn/joinnew/processjq.ashx?curid=31490788&starttime=2019%2F1%2F4%20{hour}%3A{min}%3A55&source=directphone&submittype=1&ktimes=310&hlv=1&rn=3737239896.38025742&t=1546603523765&jqnonce=1333f9c9-bb09-4a52-999c-f76a95338363&jqsign=0222g8b8%2Ccc18%2C5%6043%2C888b%2Cg67%6084229272'.format(hour = time.localtime().tm_hour,min = min)

    a = requests.post(url,data={'submitdata':b})
    print(a.headers['Date'])
    print(time.localtime().tm_hour)
    time.sleep(random.randint(100,200))
    print(c)
