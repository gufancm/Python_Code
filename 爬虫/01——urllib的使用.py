import urllib.request
url = "https://www.baidu.com/"
respone = urllib.request.urlopen(url)
content = respone.read().decode('UTF-8')
print(content)