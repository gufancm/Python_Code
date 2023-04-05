import urllib.request
url = "http://www.baidu.com"
respone = urllib.request.urlopen(url)
# 一个类型  HTTPResponse类型
print(type(respone))
# content = respone.read().decode('UTF-8')   # 一个字节一个字节读
# content = respone.read(5).decode('UTF-8')  # 读五个字节
# content = respone.readline()  # 读取一行
# content = respone.readlines()
# content = respone.getcode()  # 返回状态码
# content = respone.geturl()  # 返回url地址
content = respone.getheaders()   # 返回状态信息
print(content)