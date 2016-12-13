#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' スタック '''

# 計算量：O(1)


operators = {"+": lambda x, y: x + y,
             "-": lambda x, y: x - y,
             "*": lambda x, y: x * y,
             "/": lambda x, y: x / y}


def compute(A):
    stack = []

    for i in range(len(A)):
        # 演算子
        if isinstance(A[i], str):
            op_right = stack.pop()
            op_left = stack.pop()
            # 計算してスタックに戻す
            stack.append(operators[A[i]](op_left, op_right))

        # オペランド
        if isinstance(A[i], int):
            stack.append(A[i])

    return stack[-1]

if __name__ == '__main__':
    A = list(input().split())
    # A = list("1 2 + 3 4 - *".split())

    for i in range(len(A)):
        if not A[i] in ['+', '-', '*', '/']:
            A[i] = int(A[i])

    print(compute(A))
