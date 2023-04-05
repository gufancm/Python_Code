import urllib.request
from lxml import etree
# https://sc.chinaz.com/tupian/qinglvtupian.html
# https://sc.chinaz.com/tupian/qinglvtupian_2.html
def creat_request(page):
    if page ==1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_'+str(page)+'.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }
    request = urllib.request.Request(url=url,headers=headers)
    return request
def get_response(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content):
    # urllib.request.urlretrieve('图片地址’，‘文件的名字’）
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="container"]//img/@alt')
    src_list = tree.xpath('//div[@class="container"]//img/@src2')
    for i in range(len(src_list)):
        src = src_list[i]
        name = name_list[i]
        url = 'https:' + src
        urllib.request.urlretrieve(url=url, filename='/' + name+'.jpg')

if __name__ == '__main__':
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入尾页页码："))
    for page in range(start_page, end_page+1):
        # 1.请求对象定制
        request = creat_request(page)
        # 2.获取网页源码
        content = get_response(request)
        # 3.下载
        down_load(content)