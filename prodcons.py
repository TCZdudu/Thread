#!/usr/bin/env python

from random import randint
from time import sleep
from queue import Queue
from myThread import MyThread


def writeQ(queue):
    print('producing object for Q...', end=' ')
    queue.put('xxx', 1)
    print('size now', queue.qsize())


def readQ(queue):
    val = queue.get(1)
    print('consumed object from Q... size now', queue.qsize())


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))


funcs = [writer, reader]
nfuncs = range(len(funcs))


def main():
    nloops = randint(2, 5)
    q = Queue(32)
    threads = []

    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()  # 启动线程

    for i in nfuncs:
        threads[i].join()   # 等待所有进程结束  又称自旋锁

    print('all DONE')


if __name__ == '__main__':
    main()
