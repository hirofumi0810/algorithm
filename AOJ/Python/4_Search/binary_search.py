#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' 二分探索 '''

# n個の要素の配列に対してq回の探索を行った場合
# 計算量：O(qlogn)


def binary_search(key, A):
    imin, imax = 0, len(S)

    while imin < imax:
        mid = int((imin + imax) / 2)
        if A[mid] == key:
            return True
        elif key < A[mid]:
            imax = mid
        else:
            imin = mid + 1
    return False


if __name__ == '__main__':
    NS = int(input())
    S = list(map(int, input().split()))
    NT = int(input())
    T = list(map(int, input().split()))

    count = 0

    for t in T:
        if binary_search(t, S):
            count += 1
    print(count)
