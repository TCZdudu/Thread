#!/usr/bin/env python3

from myThread import MyThread
from time import ctime, sleep


def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return (fib(x-1) + fib(x-2))


def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x * fac(x-1))


def sum1(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x + sum1(x-1))


funcs = [fib, fac, sum1]
n = 12


def main():
    nfuncs = range(len(funcs))
    print('*** Single thread')
    for i in nfuncs:
        print('statring', funcs[i].__name__, 'at:', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime())

    print('\n *** MULTIPLE THREADS')
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()  # 启动线程

    for i in nfuncs:
        threads[i].join()   # 等待所有进程结束  又称自旋锁
        print(threads[i].get_result())

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
