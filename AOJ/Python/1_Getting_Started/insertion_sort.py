#! /usr/bin/env python
#-*- coding: utf-8 -*-

''' 挿入ソート '''

# 最悪の場合，比較を1,2,...,n-1=n(n-1)/2回行うから
# 計算量：O(n^2)


def insertion_sort(A, N):

    for i in range(N):
        tmp = A[i]
        j = i - 1

        while j >= 0 and A[j] > tmp:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = tmp

        print(' '.join(map(str, A)))

    return A


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    # N = 6
    # A = [5, 2, 4, 6, 1, 3]
    array_sorted = insertion_sort(A, N)
