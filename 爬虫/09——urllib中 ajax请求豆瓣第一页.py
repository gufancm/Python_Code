import urllib.request
import urllib.parse
url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46'
}
# 定制请求对象
request = urllib.request.Request(url=url, headers=headers)
# 获取响应数据
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
# 保存文件到本地
with open('douban.json', 'w', encoding='utf-8') as fp:
    fp.write(content)