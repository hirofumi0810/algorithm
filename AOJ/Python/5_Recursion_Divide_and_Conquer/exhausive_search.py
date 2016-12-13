#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' 全探索 '''

# 各要素を選ぶか選ばないかで2^n通りあるので
# 計算量：O(2^n)
# 深さ優先探索

# DPでやんないと通らない


def check(n, target, i, sum):
    if i == n:
        return sum == target

    # A[i]を使う場合
    if check(n, target, i + 1, sum + A[i]):
        return True

    # A[i]を使わない場合
    if check(n, target, i + 1, sum):
        return True

    # A[i]を使っても使わなくてもtargetを作れない
    return False

    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    for b in B:
        if check(n, b, 0, 0):
            print('yes')
        else:
            print('no')
