#! /usr/bin/env python
# -*- coding: utf-8 -*-

''' キュー '''

# リングバッファを用いれば
# 計算量：O(1)


def round_robin_scheduling(process_name, process_time, quantum):
    result = []
    elapsed_time = 0

    while len(process_name) > 0:
        p_name = process_name.pop(0)
        p_time = process_time.pop(0)

        if p_time > quantum:
            elapsed_time += quantum
            process_name.append(p_name)
            process_time.append(p_time - quantum)
        else:
            elapsed_time += p_time
            result.append(p_name + ' ' + str(elapsed_time))

    return result


if __name__ == '__main__':
    N_p, quantum = map(int, input().split())
    p_name, p_time = [], []
    for _ in range(N_p):
        p = list(input().split())
        p_name.append(p[0])
        p_time.append(int(p[1]))

    result = round_robin_scheduling(p_name, p_time, quantum)

    for i in range(len(result)):
        print(result[i])
