# 管理待爬取和已爬取的URL集合
class UrlManager(object):
    def __init__(self):
        self.urls = set()  # 待爬取的URL集合
        self.over_urls = set()  # 已爬取的URL集合

    def add_url(self, root_url):
        if root_url is None:
            return
        if root_url not in self.over_urls and root_url not in self.urls:
            self.urls.add(root_url)

    def has_more_url(self):
        return len(self.urls) > 0

    def get_url(self):
        new_url = self.urls.pop()
        self.over_urls.add(new_url)
        return new_url

    def add_urls(self, new_urls):
        if new_urls is None or len(new_urls) <= 0:
            return
        for url in new_urls:
            self.add_url(url)
