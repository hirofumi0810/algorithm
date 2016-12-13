#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' 二分木 '''


class BinaryTree(object):
    """ binary tree """

    def __init__(self, root=None):
        self.value = root
        self.left = None
        self.right = None

    def insert_left(self, x):
        self.left = x

    def insert_right(self, x):
        self.right = x

    def delete(self, x):
        # code
        print(1)


if __name__ == '__main__':
    N_node = int(input())

    # 該当するまで保存
    node_dict = {}

    for i in range(N_node):
        i_node, left, right = list(map(int, input().split()))
        if i == 0:
            tree = BinaryTree(i_node, left, right)
        else:
            if tree.left == i_node:
                tree.left = BinaryTree(left)
            elif tree.right == i_node:
                tree.right = BinaryTree(right)
            else:
                node.dict[i_node] = (left, right)
