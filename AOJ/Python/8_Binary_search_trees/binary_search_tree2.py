#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' 二分探索木2 '''

from binary_search_tree1 import BinarySearchTree


if __name__ == '__main__':
    N = int(input())

    tree = BinarySearchTree()

    for _ in range(N):
        command = list(input().split())
        if command[0] == 'insert':
            tree.insert(tree, int(command[1]))
        elif command[0] == 'find':
            if tree.find(tree, int(command[1])):
                print('yes')
            else:
                print('no')
        elif command[0] == 'print':
            tree.print()
