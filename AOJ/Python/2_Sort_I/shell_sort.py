#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' シェルソート '''


# 計算量：O()

def shell_sort():

    return (A, swap_num)

if __name__ == '__main__':
    # N = int(input())
    # A = list(map(int, input().split()))
    A = [5, 2, 4, 6, 1, 3]
    N = len(A)
    array_sorted, swap_num = shell_sort(A, N)
    print(' '.join(map(str, array_sorted)))
    print(swap_num)
