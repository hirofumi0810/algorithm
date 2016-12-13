#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' プライオリティーキュー '''

import heapq


class PQueue(object):
    """ Priority Queue """

    def __init__(self):
        self.pqueue = []

    def insert(self, x):
        # self.pqueue.append(x)
        heapq.heappush(self.pqueue, -x)

    def extractMax(self):
        # return self.pqueue.pop(self.pqueue.index(max(self.pqueue)))
        return -heapq.heappop(self.pqueue)


if __name__ == '__main__':

    pqueue = PQueue()
    result = []

    while True:
        line = input()
        if line == 'end':
            break

        if line.split()[0] == 'insert':
            pqueue.insert(int(line.split()[1]))
        elif line.split()[0] == 'extract':
            result.append(pqueue.extractMax())

    for i in range(len(result)):
        print(result[i])
