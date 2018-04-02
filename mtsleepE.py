#!/usr/bin/env python

import threading
from time import sleep, ctime
from myThread import MyThread

loops = [4, 2]
# 派生thread的子类，并创建子类的实例


def loop(nloop, nsec):
    print("start loop", nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:    # 创建线程
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()  # 启动线程

    for i in nloops:
        threads[i].join()   # 等待所有进程结束  又称自旋锁

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
