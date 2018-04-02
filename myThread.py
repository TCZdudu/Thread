#!/usr/bin/env python

import threading
from time import sleep, ctime

loops = [4, 2]
# 派生thread的子类，并创建子类的实例


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        super().__init__()
        self.name = name
        self.func = func
        self.args = args

    def get_result(self):
        return self.res

    def run(self):
        print('stareting', self.name, 'at', ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finish at:', ctime())
