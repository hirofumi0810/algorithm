S = [3, 6, 7, 1, 3, 5, 8, 10, 2, 1]
T = 11


def find(A, sum):
    B = {}
    for i in range(len(A)):
        B[sum - A[i]] = i
        if A[i] in B.keys():
            return (i, B[A[i]])

    return (100, 100)

print(find(S, T))
