# -*- coding: utf-8 -*-


def round_robin_scheduling(process_name, process_time, q):
    result = []
    elapsed_time = 0

    while len(process_name) > 0:
        # print process_name
        # print process_time
        if process_time[0] <= q:
            elapsed_time += process_time[0]
            process_time.pop(0)
            result.append(process_name.pop(0) + ' ' + str(elapsed_time))
        else:
            elapsed_time += q
            process_name.append(process_name.pop(0))
            process_time.append(process_time.pop(0) - q)
    return result


if __name__ == '__main__':
    N, q = map(int, raw_input().split())
    process_name, process_time = [], []
    for i in xrange(N):
        process = raw_input().split()
        process_name.append(process[0])
        process_time.append(int(process[1]))
    result = round_robin_scheduling(process_name, process_time, q)
    for i in xrange(len(result)):
        print result[i]
