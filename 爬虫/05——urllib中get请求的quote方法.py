import urllib.request
url = "https://www.baidu.com/s?wd="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46"
}

# quote方法
name = urllib.parse.quote("西安特产")
url = url + name
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("UTF-8")
print(content)