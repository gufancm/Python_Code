# 请求对象定制
# 获取对象请求
# 下载到本地
import urllib.request
import urllib.parse

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=20&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=40&limit=20
def creat_request(page):
    base_url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&"
    data = {
        'start': (page-1)*20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)
    url =base_url + data
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open('douban_'+str(page)+'.json', 'w', encoding='utf-8') as fd:
        fd.write(content)



if __name__ == '__main__':
    start_page = int(input("请输入起始页："))
    end_page = int(input("请输入最后一页："))
    for page in range(start_page, end_page+1):
        request = creat_request(page)
        content = get_content(request)
        down_load(page,content)