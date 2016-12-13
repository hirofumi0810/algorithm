#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' 選択ソート '''

# 比較演算の回数は常にn(n-1)/2なので
# 計算量:O(n^2)
# 交換回数は最大でn-1回で，バブルソートよりも少ない


def selection_sort(A, N):
    swap_num = 0  # 交換回数

    for i in range(N):
        minj = i
        for j in range(i, N, 1):
            if A[j] < A[minj]:
                minj = j
        # swap
        if i != minj:
            tmp = A[i]
            A[i] = A[minj]
            A[minj] = tmp
            swap_num += 1

    return (A, swap_num)


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    # A = [5, 2, 4, 6, 1, 3]
    # N = len(A)
    array_sorted, swap_num = selection_sort(A, N)
    print(' '.join(map(str, array_sorted)))
    print(swap_num)
