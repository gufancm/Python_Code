import urllib.request
proxies_pool = [
    {'http': '113.121.42.98:3828'},
    {'http': '114.230.89.248:3828'},
]

import random

proxies = random.choice(proxies_pool)
print(proxies)

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}
request = urllib.request.Request(url=url, headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
with open('dailichi.html', 'w', encoding='utf-8')as df:
    df.write(content)
