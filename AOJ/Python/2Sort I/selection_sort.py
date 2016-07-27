# -*- coding: utf-8 -*-

# 合計の比較演算の回数は常にN(N-1)/2 となることから，選択ソートの計算量はN^2に比例し，オーダーがO(N^2) のアルゴリズムとなる


def selection_sort(A, N):
    change = 0
    for i in xrange(N):
        minj = i
        for j in xrange(i, N, 1):
            if A[j] < A[minj]:
                minj = j
        if minj != i:
            temp = A[minj]
            A[minj] = A[i]
            A[i] = temp
            change += 1
    return (A, change)


if __name__ == "__main__":
    N = input()
    A = map(int, raw_input().split())
    # A = [5, 2, 4, 6, 1, 3]
    # N = len(a)
    result, change = selection_sort(A, N)
    print ' '.join(map(str, result))
    print change
