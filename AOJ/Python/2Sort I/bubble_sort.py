# -*- coding: utf-8 -*-


def bubble_sort(A, N):
    change = 0
    for i in xrange(N - 1):
        for j in xrange(N - 1, i, -1):
            if A[j - 1] > A[j]:
                temp = A[j - 1]
                A[j - 1] = A[j]
                A[j] = temp
                change += 1
    return (A, change)


if __name__ == "__main__":
    N = input()
    A = map(int, raw_input().split())
    # A = [5, 2, 4, 6, 1, 3]
    # N = len(A)
    result, change = bubble_sort(A, N)
    print ' '.join(map(str, result))
    print change
