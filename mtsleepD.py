#!/usr/bin/env python

import threading
from time import sleep, ctime

loops = [4, 2]
# 创建thread实例，传给他一个可调用的类实例


class ThreadFunc():

    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print("start loop", nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:    # 创建线程
        t = threading.Thread(target=ThreadFunc(
            loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()  # 启动线程

    for i in nloops:
        threads[i].join()   # 等待所有进程结束  又称自旋锁

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
