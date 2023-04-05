import urllib.request
import urllib.parse
base_url = "http://www.baidu.com/s?"
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}
headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46"
}
new_data = urllib.parse.urlencode(data)
url = base_url + new_data
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request()
content = response.read().decode("UFT-8")
print(content)