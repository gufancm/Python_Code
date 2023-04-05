# re.findall()用法详解
# re.findall()：函数返回包含所有匹配项的列表。返回string中所有与pattern相匹配的全部字串，返回形式为数组。
# findall(pattern, string, flags=0)
import re
def count_word(text, word):
    words = re.findall(r'%s' % word, text, flags=re.IGNORECASE)
    return len(words)
text = "Python is a high-level,general-purpose programming language.Its design philosophy emphasizes code readability with the use of significant indentation . Python is dynamically typed and garbage-collected."
word = str(input("请输入要查询次数的字母："))
result = count_word(text, word)
print("单词'{}'出现的次数为：{}".format(word, result))

# “d”：0到9之间的数
str_s1 = "21Python is a h23igh-level,genera123l-purpose prog4ramming ！、、language."
ret1 = re.findall(r'\d', str_s1)
print(ret1)

# “D”：除了了0-9以外的所有内容
str_s2 = "21Python is a ！？‘【】language."
ret = re.findall(r'\D', str_s2)
print(ret)

# “w”:匹配从小写a到z,大写A到Z，数字0到9中的内容
str_s3 = "21Python is a ！？‘【】language."
ret3 = re.findall(r'\w', str_s3)
print(ret3)

# “W”在正则里面代表匹配除了字母与数字以外的特殊符号
str_s4 = "21Python is a ！？‘【】language."
ret4 = re.findall(r'\W', str_s4)
print(ret4)

# [ ] 匹配括号中的任何一个符合条件的字符
str_s5 = "Python is a h23igh-level,genera123l-purpose prog4ramming ！、、language."
ret5 = re.findall(r'[pn]', str_s5)
print(ret5)

# ^ 取非
str_s6 = "Python is a language."
ret6 = re.findall(r"[^Python]", str_s6)
print(ret6)
