# -*- coding: utf-8 -*-

# n個の要素の配列に対してq回の線形探索を行って，O(qn)のアルゴリズムで解くことができる


def linear_search(S, T):
    count = 0
    for i in xrange(len(T)):
        if T[i] in S:
            count += 1
    return count

if __name__ == '__main__':
    n = input()
    S = map(int, raw_input().split())
    q = input()
    T = map(int, raw_input().split())

    print linear_search(S, T)
