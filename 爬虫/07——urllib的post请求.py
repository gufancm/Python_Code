import urllib.request
import json

url = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46"
}
data = {
    "kw": "spider"
}
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("UTF-8")
print(type(content))
print(content)
obj = json.loads(content)
print(obj)