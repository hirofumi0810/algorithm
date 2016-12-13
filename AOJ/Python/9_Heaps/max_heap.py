#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' 最大ヒープ '''


def max_heap(A, i):
    l = left(i)
    r = right(i)
      // 左の子、自分、右の子で値が最大のノードを選ぶ
      if l ≤ H and A[l] > A[i]
         largest = l
      else
          largest = i
      if r ≤ H and A[r] > A[largest]
       largest = r

     if largest ≠ i　// i の子の方が値が大きい場合
         A[i] と A[largest] を交換
         maxHeapify(A, largest) // 再帰的に呼び出し

def build_max_heap(A, H):
    for i in range(int(H / 2), 0, -1):
        print(i)
        # max_heap(A, i)

if __name__ == '__main__':
    H = int(input())
    A = list(map(int, input().split()))

    build_max_heap(A, H)
