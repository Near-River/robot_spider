# 接收待爬取URL，将网页内容下载为字符串，传送给解析器
from urllib import request


class UrlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return
        req = request.Request(new_url)
        resp = request.urlopen(req)
        if resp.getcode() == 200:
            html_doc = resp.read()
            # print(html_doc.decode('utf-8'))
            return html_doc
        return
