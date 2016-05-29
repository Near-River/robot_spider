#############################################################################
from bs4 import BeautifulSoup
from urllib import request

# Beautiful Soup4的使用
#   将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象
#       对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment .

soup = BeautifulSoup('<html><head></head><body>Hello World!'
                     '<a href="/index.html" class="cls1 cls2">点击</a></body></html>',
                     "html.parser")
# Tag 对象操作
tag = soup.a
# print(type(tag))
# print(tag)
# print(tag.name)
# print(tag.attrs)  # 返回值为数据字典型
del tag['href']  # 删除节点属性
# print(tag)
print(soup)

# 多值属性
attrs = soup.a['class']
# print(attrs)

# NavigableString 对象：可以遍历的字符串
# print(type(tag.string))
# print(tag.string)
# print(tag.get_text())
# tag中包含的字符串不能编辑,但是可以被替换成其它的字符串
tag.string.replace_with('Click!')
# print(tag.string)

# BeautifulSoup 对象：表示的是一个文档的全部内容
# print(soup)
# print(soup.name)

# Comment 对象：注释及特殊字符串
soup2 = BeautifulSoup('<b><!--Hey, buddy. Want to buy a used parser?--></b>', "html.parser")
comment = soup2.b.string
# print(type(comment))
# print(comment)
# print(soup2.b.prettify())


# 搜索节点find_add(name, attrs, string)
url = 'http://www.baidu.com'
resp = request.urlopen(url)
html_doc = resp.read().decode('utf-8')

b_soup = BeautifulSoup(html_doc, 'html.parser')
links = b_soup.find_all('a')
for link in links:
    print(link)
