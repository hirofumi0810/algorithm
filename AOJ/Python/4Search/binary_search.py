# -*- coding: utf-8 -*-

# 二分探索の計算量はO(logn)となる
# 各要素について二分探索を行ってO(qlogn)のアルゴリズムで解くことができる


def binary_search(n, A):
    count = 0
    left = 0
    right = len(A)
    while left < right:
        mid = int((left + right) / 2)
        if A[mid] == n:
            return True
        elif A[mid] > n:
            right = mid
        else:
            left = mid + 1
    return False


if __name__ == '__main__':
    n = input()
    S = map(int, raw_input().split())
    q = input()
    T = map(int, raw_input().split())

    count = 0
    for i in xrange(len(T)):
        if binary_search(T[i], S):
            count += 1
    print count
