#!/usr/bin/env python3

import _thread
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
    print("start loop", nloop, "at:", ctime())
    sleep(nsec)
    print("loop", nloop, "done at:", ctime())
    lock.release()

def main():
    print("starting at:", ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()  #相当于上锁操作
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked():pass  #循环接受开锁操作

    print("all done at:", ctime())

if __name__ == '__main__':
    main()