# -*- coding: utf-8 -*-
# 简单的网络爬虫: 模拟浏览器登陆苏大选课系统

import re, time
import http.cookiejar
import urllib.request
import urllib.parse
import xlwt
from PIL import Image

# 构造请求头信息 header
URL = 'http://xk.suda.edu.cn/default5.aspx'
CheckCodeURL = 'http://xk.suda.edu.cn/CheckCode.aspx'
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-US;q=0.8,zh;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Accept-Encoding': 'gzip,deflate',
    'Host': 'xk.suda.edu.cn',
    'Referer': 'http://xk.suda.edu.cn/default5.aspx'
}


def getOpener(header):
    # 设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header_lst = []
    for key, value in header.items():
        elem = (key, value)
        header_lst.append(elem)
    opener.addheaders = header_lst
    return opener


# 获取验证码
def get_captcha(opener):
    global CheckCodeURL
    t = str(int(time.time() * 1000))
    captcha_url = CheckCodeURL
    r = opener.open(captcha_url)
    with open('check_code.jpg', 'wb') as f:
        f.write(r.read())
    # 用pillow 的 Image 显示验证码
    with Image.open('check_code.jpg') as im:
        im.show()
    captcha = input("Captcha: ")
    return captcha


def suda_xk_login():
    global URL, header
    opener = getOpener(header)
    opener.open(URL)

    # 组装post数据
    account = input('Sid: ')
    password = input('Pwd: ')
    captcha = get_captcha(opener)

    # 构造Post数据
    postDict = {
        '__VIEWSTATE': 'dDwtMTUwMzUyMTg2NDt0PDtsPGk8MT47PjtsPHQ8O2w8aTwzPjtpPDU+Oz47bDx0PHQ8OztsPGk8Mj47Pj47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LmNsb3NlKClcOzs+Pj47Oz47Pj47Pj47PpejivgYcy+AWRtYqJL/JZazxGz6',
        'TextBox1': account,
        'TextBox2': password,
        'TextBox3': captcha,
        'Button1': '',
        'hidPdrs': '',
        'hidsc': ''
    }

    # 需要给Post数据编码
    postData = urllib.parse.urlencode(postDict).encode()
    resp = opener.open(URL, postData)
    # print(resp.read().decode('gb2312'))


def suda_xk_load_score():
    ScoreUrl = 'http://xk.suda.edu.cn/xscjcx_dq.aspx?xh=1327403010&xm=%D1%EE%CF%F4&gnmkdm=N121604'
    headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,en-US;q=0.8,zh;q=0.5,en;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Accept-Encoding': 'gzip,deflate',
        'Host': 'xk.suda.edu.cn',
        'Referer': 'http://xk.suda.edu.cn/xscjcx_dq.aspx?xh=1327403010&xm=%D1%EE%CF%F4&gnmkdm=N121604',
        'Cookie': 'yunsuo_session_verify=d083715be7b906ad320f92e204eefcd1; ASP.NET_SessionId=tdj5zf55t2pire55qdndru55; AD_jsdx_cookie=20111155'
    }
    opener = getOpener(headers)
    postDict = {
        '__VIEWSTATE': 'dDwxMDk5MDkzODA4O3Q8cDxsPHRqcXI7PjtsPDE7Pj47bDxpPDE+Oz47bDx0PDtsPGk8MT47aTw3PjtpPDk+Oz47bDx0PHQ8O3Q8aTwxNz47QDzlhajpg6g7MjAwMS0yMDAyOzIwMDItMjAwMzsyMDAzLTIwMDQ7MjAwNC0yMDA1OzIwMDUtMjAwNjsyMDA2LTIwMDc7MjAwNy0yMDA4OzIwMDgtMjAwOTsyMDA5LTIwMTA7MjAxMC0yMDExOzIwMTEtMjAxMjsyMDEyLTIwMTM7MjAxMy0yMDE0OzIwMTQtMjAxNTsyMDE1LTIwMTY7MjAxNi0yMDE3Oz47QDzlhajpg6g7MjAwMS0yMDAyOzIwMDItMjAwMzsyMDAzLTIwMDQ7MjAwNC0yMDA1OzIwMDUtMjAwNjsyMDA2LTIwMDc7MjAwNy0yMDA4OzIwMDgtMjAwOTsyMDA5LTIwMTA7MjAxMC0yMDExOzIwMTEtMjAxMjsyMDEyLTIwMTM7MjAxMy0yMDE0OzIwMTQtMjAxNTsyMDE1LTIwMTY7MjAxNi0yMDE3Oz4+Oz47Oz47dDw7bDxpPDA+O2k8MT47aTwyPjs+O2w8dDw7bDxpPDA+Oz47bDx0PHA8bDxpbm5lcmh0bWw7PjtsPDIwMTUtMjAxNuWtpuW5tOesrDLlrabmnJ/lrabkuaDmiJDnu6k7Pj47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjs+O2w8dDxwPGw8aW5uZXJodG1sOz47bDzlrablj7fvvJoxMzI3NDAzMDEwOz4+Ozs+O3Q8cDxsPGlubmVyaHRtbDs+O2w85aeT5ZCN77ya5p2o6JCnOz4+Ozs+O3Q8cDxsPGlubmVyaHRtbDs+O2w85a2m6Zmi77ya6K6h566X5py656eR5a2m5LiO5oqA5pyv5a2m6ZmiOz4+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+Oz47bDx0PHA8bDxpbm5lcmh0bWw7PjtsPOS4k+S4mu+8mui9r+S7tuW3peeoi++8iOW1jOWFpeW8j+i9r+S7tuS6uuaJjeWfueWFu++8iTs+Pjs7Pjt0PHA8bDxpbm5lcmh0bWw7PjtsPOihjOaUv+ePre+8muiuoTEz5bWM5YWl5byPMjs+Pjs7Pjs+Pjs+Pjt0PEAwPHA8cDxsPFBhZ2VDb3VudDtfIUl0ZW1Db3VudDtfIURhdGFTb3VyY2VJdGVtQ291bnQ7RGF0YUtleXM7PjtsPGk8MT47aTwwPjtpPDA+O2w8Pjs+Pjs+O0AwPDs7Ozs7Ozs7Ozs7Ozs7Ozs7QDA8cDxsPFZpc2libGU7PjtsPG88dD47Pj47Ozs7Pjs7Ozs7Pjs7Ozs7Ozs7Oz47Oz47Pj47Pj47PrO+GlatLJJR443Aq7EPcHoLfcq8',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        'ddlxn': '全部',  # 学年
        'ddlxq': '全部',  # 学期
        'btnCx': ' 查 询 '
    }
    postData = urllib.parse.urlencode(postDict).encode()
    resp = opener.open(ScoreUrl, postData)

    data = resp.read().decode('gb2312')
    # print(data)
    parse_data(data)


def parse_data(data):
    """
    解析信息的模板：
       <tr class="datelisthead">
    		<td>学年</td><td>学期</td><td>课程代码</td><td>课程名称</td><td>课程性质</td><td>课程归属</td><td>学分</td><td>平时成绩</td><td>期中成绩</td><td>期末成绩</td><td>实验成绩</td><td>成绩</td><td>补考成绩</td><td>是否重修</td><td>开课学院</td><td>绩点</td><td>备注</td><td>补考备注</td>
    	</tr>
    	<tr>
    		<td>2013-2014</td><td>1</td><td>coms1003</td><td>c语言程序设计</td><td>大类基础课程</td><td>&nbsp;</td><td>5.00</td><td>&nbsp;</td><td>&nbsp;</td><td>79</td><td>&nbsp;</td><td>79</td><td>&nbsp;</td><td>&nbsp;</td><td>计算机科学与技术学院</td><td>3.20</td><td>&nbsp;</td><td>&nbsp;</td>
    	</tr>
    	<tr class="alt">
    		<td>2013-2014</td><td>1</td><td>emst1002</td><td>计算机基础</td><td>大类基础课程</td><td>&nbsp;</td><td>2.50</td><td>80</td><td>&nbsp;</td><td>80</td><td>80</td><td>80</td><td>&nbsp;</td><td>&nbsp;</td><td>计算机科学与技术学院</td><td>3.30</td><td>&nbsp;</td><td>&nbsp;</td>
    	</tr><tr>
    """
    title_pattern = re.compile(
        r'<tr class="datelisthead">.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',
        flags=re.DOTALL)
    pattern = re.compile(
        r'<tr.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',
        flags=re.DOTALL)
    titles = title_pattern.findall(data)  # 存放表格头信息
    title_data = titles[0]
    content = pattern.findall(data)
    score_data = content[1:]  # 存放表格列信息
    # print(score_data[0])
    save_data(title_data, score_data)


def save_data(titles, score_data):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("成绩表")
    style = xlwt.easyxf('font: bold 1')
    for i in range(len(titles)):
        sheet.col(i).width = 256 * 20
    # 写入标题
    for i in range(len(titles)):
        sheet.write(0, i, titles[i], style)
    # 写入成绩数据
    for i in range(len(score_data)):
        for j in range(len(titles)):
            data = str(score_data[i][j]).replace('&nbsp;', '')
            sheet.write(i + 1, j, data)

    workbook.save('score.xls')


if __name__ == '__main__':
    suda_xk_login()
    suda_xk_load_score()
