#!/usr/bin/env python

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime


lock = Lock()
MAX = 5
candytray = BoundedSemaphore(5) # 设置最大资源数


def refill():
    lock.acquire()
    print('Refilling candy...', end=' ')
    try:
        candytray.release() # 计数器加一
    except ValueError:
        print('full, skipping')
    else:
        print('OK')
    lock.release()


def buy():
    lock.acquire()
    print('Buying candy...', end=' ')
    if candytray.acquire(False):    # 传递False使其在资源数为0时不阻塞而是返回false
        print('OK')
    else:
        print('empty, skipping')
    lock.release()


def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))


def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))


def main():
    print('starting at:', ctime())
    nloops = randrange(2, 6)
    print('THE CANDY MACHINE (full with {} bars'.format(MAX))
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()
    Thread(target=producer, args=(nloops,)).start()


@register
def atexit():
    print('all done at:', ctime())


if __name__ == '__main__':
    main()
