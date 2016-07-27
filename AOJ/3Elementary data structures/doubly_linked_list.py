# -*- coding: utf-8 -*-

functions = {"insert": lambda x, l: insert(x, l),
             "delete": lambda x, l: delete(x, l),
             "deleteFirst": lambda x, l: deleteFirst(x, l),
             "deleteLast": lambda x, l: deleteLast(x, l)}


# 連結リストの先頭にキーxを持つ要素を継ぎ足す
def insert(x, l):
    l = [x] + l
    return l


# キーxを持つ最初の要素を連結リストから削除する
def delete(x, l):
    for i in xrange(len(l)):
        if l[i] == x:
            l.pop(i)
            break
    return l


# リストの先頭の要素を削除する
def deleteFirst(x, l):
    l.pop(0)
    return l


# リストの末尾の要素を削除する
def deleteLast(x, l):
    l.pop()
    return l


if __name__ == '__main__':
    # N = input()
    commands, args = [], []
    # column = [raw_input().split() for i in xrange(N)]
    f = open('ALDS1_3_C-in10.txt', 'r')
    column = [f_column for f_column in f]
    f.close()
    N = len(column) - 1

    for i in xrange(N):
        # command = raw_input().split()
        commands.append(column[i][0])
        if column[i][0] == "deleteFirst" or column[i][0] == "deleteLast":
            args.append(0)
        else:
            args.append(int(column[i][1]))

    result = []
    for i in xrange(len(commands)):
        result = functions[commands[i]](args[i], result)
    print ' '.join(map(str, result))
