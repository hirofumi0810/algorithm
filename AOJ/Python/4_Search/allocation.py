#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' 最大積載量 '''

# 幅優先探索


def search(weights, N_track, p):
    # 荷物の最小値がトラックの積載量を超えていたら不可能
    if min(weights) > p:
        return search(weights, N_track, p + 1)

    else:
        track_capability = [p for _ in range(N_track)]
        for i in range(len(weights)):
            for j in range(N_track):
                if track_capability[j] > weights[i]:
                    track_capability[j] -= weights[i]
                    break
                if j == N_track - 1:
                    return search(weights, N_track, p + 1)
        print(track_capability)
        return p

if __name__ == '__main__':
    N_package, N_track = list(map(int, input().split()))

    weights = []
    for _ in range(N_package):
        weights.append(int(input()))

    print(search(weights, N_track, 1))
