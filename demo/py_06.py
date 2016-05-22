# -*- coding: utf-8 -*-
import re

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
