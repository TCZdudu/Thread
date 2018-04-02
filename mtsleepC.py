#!/usr/bin/env python

import threading
from time import sleep, ctime

loops = [4, 2]  # 创建Thread实例，传给他一个参数。


def loop(nloop, nsec):
    print("start loop", nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:    # 创建线程
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()  # 启动线程

    for i in nloops:
        threads[i].join()   # 等待所有进程结束  又称自旋锁

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
