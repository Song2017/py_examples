"""
https://docs.python.org/zh-cn/3/library/concurrent.futures.html
1。 Future(待执行对象) 类将可调用对象封装为异步执行
concurrent.futures 模块的主要特色是 ThreadPoolExecutor 和 ProcessPoolExecutor 类，
这两个类实现的接口能分别在不同的线程 或进程中执行可调用的对象。
这两个类在内部维护着一个工作线程或进 程池，以及要执行的任务队列
Executor.submit(...) 方法创建期物，以及如何使用 concurrent.futures.as_completed(...) 函数迭代运行结束的期 物

2。IO密集型工作 - 阻塞型I/O和GIL
CPython 解释器本身就不是线程安全的，因此有全局解释器锁（GIL）， 一次只允许使用一个线程执行 Python 字节码
标准库中所有执行阻塞型 I/O 操作的函数，在等待操作系统返回 结果时都会释放 GIL。
I/O 密集型 Python 程序能从中受益：一个 Python 线程等待网络响 应时，阻塞型 I/O 函数会释放 GIL，再运行一个线程
为什么Python 线程适合 I/O 密集 型应用
标准库中每个使用 C 语言编写的 I/O 函数都会释放 GIL，因 此，当某个线程在等待 I/O 时，
Python 调度程序会切换到另一个线程。

3。 CPU 密集型工作
ProcessPoolExecutor 类把工作分配给多个 Python 进程处理
CPU 密集型处理，使用这个模块 能绕开 GIL，利用所有可用的 CPU 核心。
使用 Python 处理 CPU 密集型工作，应该试试 PyPy（http://pypy.org）
借助 concurrent.futures.ProcessPoolExecutor 类使用多进程，以此绕 开 GIL

4。 多线程和多进程并发的低层实现（但却更灵活）threading 和 multiprocessing 模块
这两个模块代表在 Python 中使用线程和进程的传统方式

multiprocessing实现进程间传递信息
import multiprocessing

multiprocessing.RLock()
multiprocessing.Condition()
multiprocessing.Queue
multiprocessing.Pipe()
"""
import collections
import os
from concurrent import futures
import tqdm

import requests


def download_one(cc):
    try:
        url = 'http://flupy.org/data/flags/{cc}/{cc}.gif'.format(cc=cc.lower())
        resp = requests.get(url)
        if resp.status_code != 200:  # <1>
            resp.raise_for_status()
        image = resp.content
    except requests.exceptions.HTTPError as exc:  # <2>
        res = exc.response
        if res.status_code == 404:
            msg = 'not found'
        else:
            raise
    else:
        path = os.path.join("./downloads", cc.lower() + '.gif')
        with open(path, 'wb') as fp:
            fp.write(image)
        msg = 'OK'
    return msg


def download_many_threading(cc_list: list):
    """
    多线程并发下载
    """
    counter = collections.Counter()
    todos = []
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        for cc in cc_list:
            future = executor.submit(download_one, cc)
            todos.append(future)

        done_iter = futures.as_completed(todos, timeout=30)
        done_iter = tqdm.tqdm(done_iter, total=len(cc_list))  # 进度条
        for ft in done_iter:
            try:
                res = ft.result()
            except requests.exceptions.HTTPError as _:
                error_msg = 'HTTP {res.status_code} - {res.reason}'
            except requests.exceptions.ConnectionError as _:
                error_msg = 'Connection error'
            else:
                error_msg = ''
            if error_msg:
                res = error_msg
            counter[res] += 1
    return counter


if __name__ == '__main__':
    POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
                'MX PH VN ET EG DE IR TR CD FR').split()
    print(download_many_threading(POP20_CC))
