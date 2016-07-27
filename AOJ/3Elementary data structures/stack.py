# -*- coding: utf-8 -*-

# pop，pushともにスタックポインタの加算・減算と代入演算を考慮して，O(1)となる


operators = {"+": lambda x, y: x + y,
             "-": lambda x, y: x - y,
             "*": lambda x, y: x * y,
             "/": lambda x, y: float(x) / y}


def calculation(A):
    stack = []

    for i in xrange(len(A)):
        if isinstance(A[i], str):
            op_right = stack.pop()
            op_left = stack.pop()
            stack.append(operators[A[i]](op_left, op_right))
        elif isinstance(A[i], int):
            stack.append(int(A[i]))
    return stack[-1]

if __name__ == '__main__':
    A = raw_input().split()
    for i in xrange(len(A)):
        if not A[i] in ['+', '-', '*', '/']:
            A[i] = int(A[i])

    print calculation(A)
