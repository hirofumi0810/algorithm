#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' 水たまりの面積 '''


def compute_area(A):
    height = 0
    result = 0

    for i in range(len(A)):
        if A[i] == '\\':
            height += 1
        elif A[i] == '_':
            continue
        elif A[i] == '/':
            height -= 1
        else:
            print('error')

    return height
    # return result


if __name__ == '__main__':
    A = list(input())

    print(compute_area(A))
