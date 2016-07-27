# -*- coding: utf-8 -*-


def is_prime(number):
    if number == 2:
        return True
    elif number < 2 or number % 2 == 0:
        return False
    else:
        i = 3
        while i <= pow(number, 0.5):
            if number % i == 0:
                return False
            i += 2
        return True


if __name__ == '__main__':
    N = input()
    numbers = [input() for i in xrange(N)]
    count = 0
    for i in xrange(len(numbers)):
        if is_prime(numbers[i]):
            count += 1
    print count
