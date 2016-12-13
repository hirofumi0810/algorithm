#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' 線形探索 '''

# n個の要素の配列に対してq回の探索を行った場合
# 計算量：O(qn)
# 番兵をを用いると定数倍高速化


def linear_search(S, T):
    count = 0
    for t in T:
        if t in S:
            count += 1
    return count

if __name__ == '__main__':
    NS = int(input())
    S = list(map(int, input().split()))
    NT = int(input())
    T = list(map(int, input().split()))

    print(linear_search(S, T))
