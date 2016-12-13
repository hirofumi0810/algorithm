#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' 辞書 '''


class Dictionary(object):
    """ Dictionary """

    def __init__(self):
        self.dict = {}

    def insert(self, x):
        self.dict[x] = 0

    def find(self, x):
        if x in self.dict.keys():
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    N = int(input())

    d = Dictionary()

    for _ in range(N):
        command, key = list(input().split())
        if command == 'insert':
            d.insert(key)
        elif command == 'find':
            d.find(key)
