import urllib.request
from lxml import etree
# xpath解析
# （1） 本地文件                                              etree.parse()
# （2） 服务器响应的数据 response.read().decode('utf-8)         etree.HTML()
tree = etree.parse('17——urllib xpth的基本使用.html')
# tree.xpath('xpath 路径')
# 1.路径查询     //:查找所有子孙节点，不考虑层级关系      （孙子）
#              /: 找直接结点                         （儿子）
# 2.谓词查询     //div[@id]
#              //div[@id='maincontent']
# 3.属性查询     //@class
# 4.模糊查询     //div[contains(@id, "he")]
#              //div[starts-with(@id, "he")]
# 5.内容查询     //div/h1/text()
# 6.逻辑运算     //div[@id="head" and @class="s_down"]
#               //title |  //price

# 查询ul下面的li
li_list1 = tree.xpath('//body/ul/li')
print(li_list1)
print(len(li_list1))
#  查询所有有id标签属性的li标签
li_list2 = tree.xpath('//body/ul/li[@id]/text()')
print(li_list2)
# 找到id为l1的标签
li_list3 = tree.xpath('//body/ul/li[@id="l1"]/text()')
print(li_list3)
# 找到id为l1的标签的class的属性值
li_list4 = tree.xpath('//ul/li[@id="l1"]/@class')
print(li_list4)
# 查询id中包含l的li标签
li_list5 = tree.xpath('//ul/li[contains(@id,"l")]/text()')
print(li_list5)
# 查询id中以l开头的li标签
li_list6 = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')
print(li_list6)
# 查询id为1和class为abc的li标签
li_list7 = tree.xpath('//ul/li[@id="l1" and @class= "abc"]/text()')
print(li_list7)