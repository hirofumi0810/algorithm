# -*- coding: utf-8 -*-

# 最悪の場合，iのループの各処理がi回行われるので，1+2+...+N-1=N(N-1)/2となり，O(N^2)のアルゴリズムとなる
# データが降順に並んでいる場合，計算量はO(N^2)になる
# データが昇順に並んでいる場合，A[j]の移動が必要ないため，おおよそN回の比較で済む
# 挿入ソートはある程度整列されたデータに対しては高速に動作する


def insertion_sort(A, N):
    process = [A]
    for i in xrange(1, N, 1):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        print A
        process.append(A)
    return (A, process)


if __name__ == "__main__":
    N = input()
    A = map(int, raw_input().split())
    result, process = insertion_sort(A, N)
    print process
    for i in range(len(process)):
        print ' '.join(map(str, process[i]))
