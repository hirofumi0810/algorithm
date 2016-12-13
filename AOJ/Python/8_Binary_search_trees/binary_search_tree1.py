#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' 二分探索木1 '''


class BinarySearchTree(object):
    """ Binary Search Tree """

    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def insert(self, node, x):
        # 葉
        if node == None:
            print('leaf')
            node = BinarySearchTree()
            node.value = x
            return node

        # 根
        elif node.value == None:
            print('root')
            node.value = x
            return node

        else:
            print('inner')
            # 左側に挿入
            if x < node.value:
                # 右辺は左側の子にxを挿入した後の部分木が返ってくる
                node.left = self.insert(node.left, x)
            # 右側に挿入
            else:
                node.right = self.insert(node.right, x)
            return node

    def print(self):
        print(1)

    def find(self, node, x):
        if node == None:
            return False
        elif x == node.value:
            return True
        elif x < node.value:
            return node.find(node.left, x)
        elif node.value < x:
            return node.find(node.right, x)

    def delete(self, x):
        print(1)

if __name__ == '__main__':
    N = int(input())

    tree = BinarySearchTree()

    for _ in range(N):
        command = list(input().split())
        if command[0] == 'insert':
            tree.insert(tree, int(command[1]))
        elif command[0] == 'print':
            tree.print()
