#-*- coding: utf-8 -*-


def insertion_sort(A):
    print ' '.join(map(str, A))
    for i in xrange(1, N, 1):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        print ' '.join(map(str, A))
    return A


if __name__ == "__main__":
    N = input()
    A = map(int, raw_input().split())
    result = insertion_sort(A)
