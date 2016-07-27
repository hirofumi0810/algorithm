# -*- coding: utf-8 -*-

memo = ['' for i in xrange(45)]
dp = [0 for i in xrange(45)]


# 再帰だと計算量はO(2^n)になる
def recursion(n):
    if n == 0 or n == 1:
        return 1

    return recursion(n - 1) + recursion(n - 2)


# メモ化を行えば計算量はO(n)まで削減できる
def memo_search(n):
    if memo[n] != '':
        return memo[n]
    else:
        if n == 0 or n == 1:
            memo[n] = 1
            return 1
        memo[n] = memo_search(n - 1) + memo_search(n - 2)
        return memo[n]


# 動的計画法でも計算量はO(n)となる
def dynamic_programming(n):
    for i in xrange(n + 1):
        if i == 0 or i == 1:
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    n = input()
    # print recursion(n)
    # print memo_search(n)
    print dynamic_programming(n)
