# -*- coding: utf-8 -*-
import re
import urllib.request

# pattern = re.compile(r'abc')  # r'xxx'：保留原生字符串
# pattern = re.compile(r'abc', re.IGNORECASE)
pattern = re.compile(r'(abc)[\s\S]+(xyz)', re.IGNORECASE)
# pattern = re.compile(r'^(?P<near>abc)[\s\S]+(?P=near)$', re.IGNORECASE)

s = 'aBcdeXyZabC'
match = pattern.match(s)
# print(match.string)
# print(match.re)

print(match)  # Match object
print(match.group())  # 获得分组信息
# print(match.groups())
# print(match.span())  # 返回(start(group), end(group))
# print(match.expand(r'\2 \1'))


# search(pattern, string, flags=0)：在一个字符串中查找匹配
s = 'aa123 bb456 cc789'
p = r'[0-9]+'
info = re.search(p, s)
print(info.group())

# findall(pattern, string, flags=0)：返回匹配部分的列表
info = re.findall(p, s)
print(info)

# sub(pattern, repl, string, count=0, flags=0)
# 将字符串中匹配部分替换为其他值
s2 = re.sub(p, '999', s)
# s2 = re.sub(p, lambda match: str(int(match.group()) + 1), s)
print(s2)

# split(pattern, string, maxsplit=0, flags=0)
# 根据匹配分割字符串，返回分割字符串组成的列表
L = re.split(r' ', s)
print(L)


# 简单的网络爬虫
# response = urllib.request.urlopen('http://tieba.baidu.com/p/3599891436')
# html = response.read()
# print(html)

# 使用 Request
url = 'http://tieba.baidu.com/p/3002502381'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
html = resp.read()
# print(html)

pattern = re.compile(r'<img [\s\S]+?src="(http:[\s\S]+?)"')
url_list = re.findall(pattern, str(html))
print(len(url_list))
i = 1
for url in url_list:
    # print(url_list)
    img_path = 'D:/demo/imgs/' + '%d.jpg' % i
    # urllib.request.urlretrieve(url, img_path)  # 远程下载
    i += 1
