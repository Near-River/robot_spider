# -*- coding: utf-8 -*-
from lib2to3.pgen2 import parse
from urllib import request
import http.cookiejar
from threading import Thread
from queue import Queue
from time import sleep
from urllib.parse import urlencode

# 网络爬虫
# =========================================================================

resp = request.urlopen('http://www.baidu.com')
# print(resp.getcode())  # 获取请求状态码
# print(resp.read().decode('utf-8'))  # 获取网页内容

req = request.Request('http://www.baidu.com')
# data：向服务器提交需要用户输入的数据  header：向服务器提交一个http的头信息
req.add_header('user-agent', 'Mozilla/5.0')

# =========================================================================
# 添加特殊情景的处理器：
#   1.需要用户登录：HTTPCookieProcessor
#   2.需要代理服务器：ProxyHandler
#   3.使用https加密访问的：HTTPSHandler
#   4.url之间自动的跳转关系：HTTPRedirectHandler


cj = http.cookiejar.CookieJar()  # 创建cookie对象
cookie_support = request.build_opener(request.HTTPCookieProcessor(cj))  # 创建opener
request.install_opener(cookie_support)  # 给request安装opener
resp2 = request.urlopen('http://www.baidu.com')  # 使用带有cookie的request访问网页
# print(resp2.read().decode('utf-8'))
for cookie in cj:
    # print(cookie)
    pass

# 使用代理服务器
# proxy_support = request.ProxyHandler({'http': 'http://xx.xx.xx.xx:xx'})
# opener = request.build_opener(proxy_support, request.HTTPHandler)
# request.install_opener(opener)
#
# content = request.urlopen('http://www.baidu.com/').read().decode('utf-8')
# print(content)

# =========================================================================
# 表单的处理：post请求
# post_data = urlencode({
#     'username': 'Near',
#     'password': '123456',
# })
# print(post_data)
#
# req2 = request.Request(
#     url='http://www.verycd.com/',
#     data=post_data
# )
# content = request.urlopen(req2).read()
# print(content)

# get请求
# get_data = 'password=123456&username=Near'
# full_url = 'http://xxxxxxxxxxxxxxx/index?%s' % get_data
# req = request.Request(full_url)


# 伪装成浏览器访问
# post_data = urlencode({})
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
# }
# req = request.Request(
#     url='http://secure.verycd.com/signin/*/http://www.verycd.com/',
#     data=post_data,
#     headers=headers
# )

# =========================================================================
# 反”反盗链”：把headers的referer改成该网站即可，
# headers = {
#     'Referer': 'http://www.cnbeta.com/articles'
# }
# 用selenium直接控制浏览器来进行站点访问，类似的还有pamie，watir，...


# 模拟多线程并发抓取
# q是任务队列    NUM是并发线程总数  JOBS是有多少任务
q, NUM, JOBS = Queue(), 3, 10


# 具体处理函数，负责处理单个任务
def do_somthing(arguments):
    print(arguments)


# 工作进程，负责不断从队列中取数据并处理
def working():
    while True:
        arguments = q.get()
        do_somthing(arguments)
        sleep(1)
        q.task_done()


# fork NUM个线程等待队列
for i in range(NUM):
    t = Thread(target=working)
    t.setDaemon(True)  # 设置为守护线程
    t.start()
# 把JOBS排入队列
for i in range(JOBS):
    q.put('Job：%d' % (i + 1))
# 等待所有JOBS完成
q.join()  # join()：Blocks until all items in the Queue have been gotten and processed.
