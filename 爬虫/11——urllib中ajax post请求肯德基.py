# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname: 泰安
# pid:
# pageIndex: 1
# pageSize: 10
import urllib.request
import urllib.parse
def crease_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '泰安',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    data = urllib.parse.urlencode(data)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=base_url, data=data, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page, content):
    with open('kfc'+str(page)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入尾页页码：'))
    for page in range(start_page, end_page+1):
        request = crease_request(page)
        content = get_content(request)
        down_load(page, content)