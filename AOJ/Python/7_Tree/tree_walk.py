#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' 木の巡回 '''


class BinaryTree(object):
    """ binary tree """

    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def return_leaf(self, x):
        """ 該当する葉が存在すれば，そのノードを返す """

    def insert_left(self, x):
        self.left = x

    def insert_right(self, x):
        self.right = x

    def delete(self, x):
        # code
        print(1)

    def preorder(self):
        """ 先行順巡回で出力 """
        print('preorder')

    def inorder(self):
        """ 中間順巡回で出力 """
        print('inorder')

    def postorder(self):
        """ 後行順巡回で出力 """
        print('postorder')


if __name__ == '__main__':
    N_node = int(input())

    # 対応するノードをつないでいく
    for i in range(N_node):
        i_node, left, right = list(map(int, input().split()))
        # 根
        if i == 0:
            tree = BinaryTree(i_node, left, right)
        # その他
        else:
            tree.insert(i_node)
