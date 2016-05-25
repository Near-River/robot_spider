# # coding:utf-8

import urllib.request
import time
from threading import Thread, Lock
from queue import Queue


class Fetcher:
    def __init__(self, threads_num):
        self.opener = urllib.request.build_opener(urllib.request.HTTPHandler)
        self.lock = Lock()  # 线程锁
        self.q_req = Queue()  # 任务队列
        self.q_ans = Queue()  # 结果队列
        self.threads_num = threads_num
        for i in range(threads_num):
            t = Thread(target=self.deal_task)
            t.setDaemon(True)
            t.start()
        self.running = 0

    def __del__(self):  # 解构时需等待两个队列的任务完成
        time.sleep(0.5)
        self.q_req.join()
        self.q_ans.join()

    def task_left(self):
        return self.q_req.qsize() + self.q_ans.qsize() + self.running

    def push(self, task):
        self.q_req.put(task)

    def pop(self):
        return self.q_ans.get()

    def deal_task(self):
        while True:
            req = self.q_req.get()
            with self.lock:  # 保证该操作的原子性
                self.running += 1
            ans = self.get_data(req)
            self.q_ans.put(ans)
            with self.lock:
                self.running -= 1
            self.q_req.task_done()
            time.sleep(0.1)

    def get_data(self, req, retries=3):  # 失败后的重连机制
        data = ''
        try:
            data = self.opener.open(req, timeout=10).read()  # 设置超时时间为10秒
        except urllib.request.URLError as e:
            if retries > 0:
                return self.get_data(req, retries - 1)
            print('GET Failed.', req)
            print(e.reason)
        return data


if __name__ == '__main__':
    t1 = time.time()
    links = ['http://www.verycd.com/base/movie/page%d/' % i for i in range(1, 11)]
    f = Fetcher(10)
    for url in links:
        f.push(url)
    while f.task_left():
        content = f.pop()
        print(len(content))
    t2 = time.time()
    print('Cost Time: %s' % (t2 - t1))
